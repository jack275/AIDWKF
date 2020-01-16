"""
在客户端有一个头像图片，编写程序将这个图片发送给
服务端。
温馨提示：  读出图片的内容--》发送给服务端
          接受客户端发过来的内容->写入到服务器文件
"""
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

f = open("boy.jpg",'wb')

# 一边接收内容，一边写入文件
while True:
    data = c.recv(1024)
    if data == "发送完了".encode():
        print(data.decode())
        break
    f.write(data)

f.close()
c.close()
s.close()









