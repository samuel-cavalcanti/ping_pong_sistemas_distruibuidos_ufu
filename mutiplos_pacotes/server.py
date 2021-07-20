# server.py
#!/usr/bin/python3                           # This is server.py file

import socket                               # Import socket module

socket_server = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
socket_server.bind((host, port))                        # Bind to the port

print(f"server listing: 127.0.0.1:{port}")

socket_server.listen(5)                                 # Now wait for client connections.
try:

    while True:
        client_connection: socket.socket
        addr: (str, int)
        # Establish connection with client.
        client_connection, addr = socket_server.accept()
    
        print(f'Got connection from {addr}')
        client_connection.send('Thank you for connecting'.encode())
        client_connection.send('Come back often'.encode())
        client_connection.close()                                # Close the connection

except KeyboardInterrupt as erro:
    print(f"\nclosing server")
    socket_server.close()
    exit(0)

