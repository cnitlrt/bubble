#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import*
import os
from ret2dl_resolve import ret2dl_resolve
class bubble(object):
	def __init__(self,pwn_file = ""):
		if pwn_file:
			self.pwn_file = pwn_file
			self.context = context
			self.context.binary = pwn_file
			self.elf = ELF(pwn_file)
	def local(self,libc_path):
		self.libc_path = "~/glibc-all-in-one/libs/"+libc_path+"/"
		self.libc_version = re.findall("libs/(.*?)-",self.libc_path)[0]
		self.ld_libc_version = "ld-"+self.libc_version+".so"
		self.ld = self.libc_path + self.ld_libc_version
		cmd='patchelf --set-interpreter '+ self.ld+' '+"--set-rpath "+self.libc_path + " " + self.pwn_file
		os.system(cmd)
	def run(self,p_type):
		if p_type == "process":
			self.p = self.process()
		elif p_type == "remote":
			self.p = self.remote()
		return self.p
	def list(self,version = ""):
		self.version = version
		if version:
			for j in os.listdir("/home/cnitlrt/glibc-all-in-one/libs"):
				if version in j:
					print j
		else:
			for i in os.listdir("/home/cnitlrt/glibc-all-in-one/libs"):
				print i
	def process(self):
		self.process = process
		self.p_process = self.process(self.pwn_file)
		return self.p_process
	def build_remote(self,host,port):
		self.host = host
		self.port = port
	def remote(self):
		self.remote = remote
		self.p_remote = self.remote(self.host,self.port)
		return self.p_remote
	def ret2dl_resolve(self):
		self.ret2dl_resolve = ret2dl_resolve(self)
		return self.ret2dl_resolve
	def l64(self):
		return u64(self.p.recvuntil("\x7f")[-6:].ljust(8,"\x00"))
	def l32(self):
		return u32(self.p.recvuntil("\xf7")[-4:].ljust(4,"\x00"))
	def sla(self,a,b):
		self.p.sendlineafter(str(a),str(b))
	def sa(self,a,b):
		self.p.sendafter(str(a),str(b))
	def lg(self,name,data):
		self.p.success(name + ": 0x%x" % data)
	def ru(self,a):
		self.p.recvuntil(str(a))
	def se(self,a):
		self.p.send(a)