#### 自定义pwntools 加载指定libc 
#### 简化脚本
#### 使用方法：
##### 将glibc_all_in_one clone到~ 然后将bubble文件夹放到~/.local/lib/python2.7/site-packages/
python
```
from bubble import *
context.log_level = "debug"
b = bubble("./pwn1")
b.local("2.27-3ubuntu1.2_amd64")
p = b.run("process")
b.ru("?\n")
attach(p)
p.interactive()
```
