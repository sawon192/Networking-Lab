import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)
print("Server is waiting for connection...")

conn, addr = server.accept()

print("Connected by:", addr)

message = conn.recv(1024).decode()
print("Client:", message)

reply = input("Server: ")
conn.send(reply.encode())

conn.close()
server.close()
