import socket

HOST = "127.0.0.1"
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Waiting for client...")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    message = conn.recv(1024).decode()

    if message.lower() == "bye":
        print("Client disconnected.")
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "bye":
        break

conn.close()
server.close()
