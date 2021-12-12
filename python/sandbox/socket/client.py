import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8888))
s.sendall(b"Hello, world")
data = s.recv(1024)
s.close()
print(f"полученные данные: {data}")
