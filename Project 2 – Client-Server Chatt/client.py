import socket

HOST = "127.0.0.1"
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:

    message = input("Client: ")
    client.send(message.encode())

    if message.lower() == "bye":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "bye":
        break

client.close()
