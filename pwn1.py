#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = cnitlrt
import sys
import os
from pwn import *
#context.log_level = 'debug'

binary = 'pwn1'
elf = ELF('pwn1')
libc = elf.libc
context.binary = binary

DEBUG = 1
if DEBUG:
  p = process(binary)
else:
  host = ""
  port =  0
  p = remote(host,port)
l64 = lambda      :u64(p.recvuntil("\x7f")[-6:].ljust(8,"\x00"))
l32 = lambda      :u32(p.recvuntil("\xf7")[-4:].ljust(4,"\x00"))
sla = lambda a,b  :p.sendlineafter(str(a),str(b))
sa  = lambda a,b  :p.sendafter(str(a),str(b))
lg  = lambda name,data : p.success(name + ": 0x%x" % data)
se  = lambda payload: p.send(payload)
rl  = lambda      : p.recv()
sl  = lambda payload: p.sendline(payload)
ru  = lambda a     :p.recvuntil(str(a))
gdb.attach(p)
p.interactive()
