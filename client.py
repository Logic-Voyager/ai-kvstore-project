# client.py

import socket

class KeyValueClient:
    def __init__(self, host='127.0.0.1', port=5000):
        self.server_address = (host, port)

    def send_command(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall(command.encode())
            response = sock.recv(1024).decode().strip()
            return response

    def examples(self):
        # Some examples:
        commands = [
            "SET name Shruti",
            "GET name",
            "SET age 18",
            "GET age",
            "MSET country India city Delhi",
            "MGET country city",
            "DELETE name",
            "FLUSH",
            "GET name" 
        ]
        
        print("Running examples:")
        for command in commands:
            response = self.send_command(command)
            print(f"> {command}\n{response}")
        print("Examples completed.\n")

    def interactive_mode(self):
        print("Enter commands (GET, SET, DELETE, FLUSH, MGET, MSET), or 'exit' to quit.")
        while True:
            command = input("> ")
            if command.lower() == 'exit':
                break
            response = self.send_command(command)
            print(response)

if __name__ == "__main__":
    client = KeyValueClient()
    client.examples()   # Run the examples
    client.interactive_mode()  # Start interactive mode

'''
# CLIENT 
The client connects to the server, sends commands, and receives responses.
1. KeyValueClient class: Manages the connection to the server. It uses self.server_address to store the server's IP and port.
2. send_command method: Connects to the server, sends a command, and returns the server's response. It uses a with
 statement to ensure the socket closes after each command.
3. examples method: Sends a series of predefined commands to the server and prints the responses. This helps in 
quickly verifying the server's functionality.
4. interactive_mode method: Provides a command-line interface for user interaction. Users can type commands, which 
the method sends to the server and displays responses.
5. __main__ block: When executed, it runs the examples first and then enters interactive mode for additional commands.
'''