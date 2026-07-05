import socket

HOST = "127.0.0.1"
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Calculator Server Running...")

conn, addr = server.accept()

print("Connected:", addr)

expression = conn.recv(1024).decode()

try:
    result = str(eval(expression))
except:
    result = "Invalid Expression"

conn.send(result.encode())

conn.close()
server.close()
