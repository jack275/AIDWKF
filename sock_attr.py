"""
套接字属性
"""
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('172.40.91.224',8888))
s.listen(3)

c,addr = s.accept()

print(s.type)
print(s.family)
print(s.getsockname())
print(s.fileno())
print(c.getpeername())