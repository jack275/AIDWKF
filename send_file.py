from socket import *
import time

s = socket()
s.connect(('127.0.0.1',8888))

# 读取目标文件，发送
f = open('xz.jpeg','rb')

while True:
    # 边读边发
    data = f.read(1024)
    if not data:
        time.sleep(0.1)
        s.send("发送完了".encode())
        break
    s.send(data)



f.close()
s.close()
