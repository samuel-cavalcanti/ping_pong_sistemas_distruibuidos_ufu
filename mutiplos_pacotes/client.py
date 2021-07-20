#client.py

#!/usr/bin/python                      # This is client.py file

import socket                          # Import socket module




server_connection = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.
buffer_size_in_bits = 1024 

server_connection.connect((host, port))

print("first message")
data = server_connection.recv(buffer_size_in_bits)
print(data.decode())

print("second message")
data = server_connection.recv(buffer_size_in_bits)
print(data.decode())

server_connection.close()                              # Close the socket when done