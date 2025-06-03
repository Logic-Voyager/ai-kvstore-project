# Assignment01 
# gevent library

# server.py

import gevent
from gevent import socket
from gevent.pool import Pool

class ProtocolHandler:
    def __init__(self):
        self.store = {}

    def handle_request(self, request):
        parts = request.strip().split()
        command = parts[0].upper()
        
        if command == 'SET' and len(parts) == 3:
            key, value = parts[1], parts[2]
            self.store[key] = value
            return f"OK"
        
        elif command == 'GET' and len(parts) == 2:
            key = parts[1]
            return self.store.get(key, "NULL")
        
        elif command == 'DELETE' and len(parts) == 2:
            key = parts[1]
            return "OK" if self.store.pop(key, None) else "NOT FOUND"
        
        elif command == 'FLUSH':
            self.store.clear()
            return "OK"
        
        elif command == 'MGET':
            keys = parts[1:]
            values = [self.store.get(key, "NULL") for key in keys]
            return ' '.join(values)
        
        elif command == 'MSET':
            if len(parts[1:]) % 2 != 0:
                return "ERROR"
            for i in range(0, len(parts[1:]), 2):
                key, value = parts[i+1], parts[i+2]
                self.store[key] = value
            return "OK"
        
        return "ERROR"

def handle_client(client_socket, handler):
    with client_socket:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            response = handler.handle_request(data)
            client_socket.sendall((response + "\n").encode())

def start_server(host='127.0.0.1', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    handler = ProtocolHandler()
    pool = Pool(10)  # Limit to 10 clients for simplicity

    while True:
        client_socket, _ = server_socket.accept()
        pool.spawn(handle_client, client_socket, handler)

if __name__ == "__main__":
    start_server()


'''
explaination: 
The server code is designed to manage a key-value store, handle multiple clients 
concurrently using gevent, and support various commands (GET, SET, DELETE, etc.).

gevent library: Provides tools for asynchronous networking and concurrency. Here, it enables 
the server to handle multiple clients at once.

Pool: Manages a pool of greenlets (lightweight threads) to limit the number of concurrent connections.

ProtocolHandler class: Manages the in-memory key-value store and processes commands. Each instance 
has a store attribute, which is a dictionary that acts as the key-value storage.

handle_request method: Processes client commands. It splits the incoming request into parts, interprets 
the command, and performs the appropriate action on the store.

1. SET key value: Adds or updates the key-value pair in the dictionary and returns "OK". 
2. GET key: Retrieves the value for a specified key. If the key doesn't exist, it returns "NULL".
3. DELETE key: Removes the specified key from the store. If the key is deleted, it returns "OK", otherwise "NOT FOUND".
4. FLUSH: Clears the entire store, returning "OK".
5. MGET key1 key2 ...: Retrieves values for multiple keys and returns them as a space-separated string. If a key doesn’t exist, 
it returns "NULL" for that key.
6. MSET key1 value1 key2 value2 ...: Sets multiple key-value pairs. If the input is incorrectly formatted, it returns "ERROR". 
Otherwise, it adds all pairs and returns "OK".

handle_client function: Receives requests from a client, processes them with ProtocolHandler, and sends back responses. 
The loop continues until the client disconnects.

start_server function: Sets up the server to listen on the specified IP and port. The SO_REUSEADDR option allows 
immediate reuse of the port after the server stops.

Pool and ProtocolHandler: ProtocolHandler is instantiated to manage the store, while Pool limits the number of 
concurrent clients (10 in this case).

pool.spawn: Starts a new greenlet for each client connection, allowing concurrent handling without blocking.
__main__ block: Starts the server when the script is run.


RUN COMMAND: To run this command, type python server.py in terminal.
'''