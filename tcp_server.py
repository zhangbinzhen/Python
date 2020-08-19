from socket import *
"""
    Tcp服务端流程基础实例
"""

# 创建tcp套接字,其实默认的值就是流式套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 绑定地址
tcp_socket.bind(("0.0.0.0",8889))
# 设置监听套接字，让tcp套接字可以被连接
# 这个监听队列大小一般在windwows、mac系统写10-15,在Linux系统写基本没用，是系统自动决定的
tcp_socket.listen(5)
# 处理客户端连接
print("等待客户端连接")
connfd,addr = tcp_socket.accept()
print("连接：",addr)
data = connfd.recv(1024)
print("接收数据为：",data.decode())

connfd.send("谢谢!".encode())

connfd.close()

tcp_socket.close()