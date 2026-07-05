
# Socket Programming

## Objective

This project demonstrates basic socket programming using Python. A client connects to a server and exchanges one message.

## Files

* client.py
* server.py

## Requirements

* Python 3

## How to Run

### Step 1

Run the server.

```
python server.py
```

### Step 2

Open another terminal.

Run the client.

```
python client.py
```

### Step 3

Type a message from the client.

The server receives it and sends a reply.

## Output

Client:

```
Client: Hello
Server: Hi
```

Server:

```
Server is waiting for connection...
Connected by ('127.0.0.1', 50314)
Client: Hello
Server: Hi
```

## Learning Outcome

* Basic socket programming
* TCP communication
* Sending and receiving messages
