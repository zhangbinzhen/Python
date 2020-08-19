from socket import *

ADDR = ("0.0.0.0",8889)

tcp_socket = socket()

tcp_socket.connect(ADDR)

msg = input(">>")

tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
print("接受：",data.decode())


tcp_socket.close()
