#!/usr/bin/env python
from pwn import *
import os
elf = ELF(./filebin)
for key, address in elf.symbols.iteritems():
	print key, hex(address)
elf.asm( elf.symbols['alarm'],'ret' )
elf.asm( elf.symbols['calculate_key'], 'mov eax,%s\nret\n' % (hex( number & 0xFFFFFFFF)))
elf.save('./new')
os.system('chmod +x ./new')
p = process('./new')
p.poll(True)
print p.recvall()