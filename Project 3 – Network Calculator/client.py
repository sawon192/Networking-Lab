import socket

HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

expression = input("Enter Expression: ")

client.send(expression.encode())

result = client.recv(1024).decode()

print("Answer:", result)

client.close()
