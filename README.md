# ai-kvstore-project
🧠 Project Title:
Concurrent In-Memory Key-Value Store with Gevent

📘 Project Overview
This project implements a concurrent in-memory key-value store using Python’s gevent library. It supports multiple client connections simultaneously and enables real-time command-based data manipulation, much like a simplified version of Redis.It includes both a server capable of handling multiple clients simultaneously and a client application that supports various commands like SET, GET, DELETE, FLUSH, MGET, and MSET.

Designed for academic purposes under the Placify Artificial Intelligence course, this project demonstrates efficient networking,custom protocol handling, concurrent request processing, and command parsing using Python.

🧩 Objectives
1. Build a simple in-memory database

2. Implement concurrent client handling using gevent

3. Develop a text-based protocol supporting key-value operations

4. Enable both batch and interactive modes of client-server communication

5. Explore asynchronous I/O concepts

🧩 Command	Description
SET key value - Store or update a key-value pair
GET key - Retrieve the value associated with a key
DELETE key - Remove a key from the store
FLUSH - Clear all data in the store
MSET k1 v1 k2 v2 - Set multiple key-value pairs at once
MGET k1 k2 ... - Retrieve values for multiple keys

🧩 How It Works
1. The server runs on a specified IP and port and listens for client connections.
2. Each connection is handled in a separate greenlet (lightweight thread).
3. The ProtocolHandler class interprets each incoming command.
4. Clients can use either a predefined list of commands or interactive input.

📖 Code Summary
1. server.py
Uses gevent.pool.Pool to manage up to 10 concurrent clients.
Handles client requests with a loop, sending parsed results via ProtocolHandler.

2. client.py
Connects to server and sends commands.
Provides example runs as well as an interactive command-line mode.

3. ProtocolHandler
Core logic for interpreting and executing commands.
Operates on an in-memory Python dictionary.

🔍 Learning Outcomes
Practical understanding of asynchronous I/O
Experience with socket programming in Python
Designing lightweight network protocols
Managing concurrent client sessions
Command parsing and protocol abstraction

🛠 Future Improvements
Add persistent storage using JSON or SQLite
Include additional commands: EXISTS, KEYS, INCR
Add server-side logging
Web interface using Flask for GUI interaction
Authentication layer

👩‍🎓 Author
Shruti
This project was developed as part of a project under Placify Internship

📄 License
Free to use for educational and academic purposes.