from bubble import *
context.log_level = "debug"
b = bubble("./pwn1")
b.local("2.27-3ubuntu1.2_amd64")
p = b.run("process")
b.ru("?\n")
b.list("2.27")
p.interactive()