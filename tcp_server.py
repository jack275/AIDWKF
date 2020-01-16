"""
tcp 服务端流程
重点代码
"""

from socket import *

# 创建tcp套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 设置端口立即重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))

# 设置监听
sockfd.listen(3)

# 处理客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)

    # 收发消息
    while True:
        data = connfd.recv(1024)
        # 如果客户端退出则recv返回空
        if not data:
            break
        # if data == b'##':
        #     break
        print("Receive:",data.decode())
        n = connfd.send(b"Thanks")
        print("发送了%d个字节"%n)
    connfd.close()

#关闭套接字
sockfd.close()
