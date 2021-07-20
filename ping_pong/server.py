# server.py
#!/usr/bin/python3                           # This is server.py file

import socket                               # Import socket module

socket_server = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
''' # [Errno 98] Address already in use
https://docs.python.org/3/library/socket.html?highlight=socket#module-socket
segundo a referência, essa flag informa ao kernel para reusar o mesmo socket, que está em TIME_WAIT
sem precisar esperar o SO fechar a conexão
'''
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_server.bind((host, port))            # Bind to the port

number_of_connections = 1
buffer_size_in_bits = 1024
client_connection = None

def chat(client_connection:socket.socket):
     while True:
            print("Esperando mensagem")
            message_in_bytes = client_connection.recv(buffer_size_in_bits)
            message_string = message_in_bytes.decode()
            if message_string == "SAIR":
                client_connection.close()
                print("Conexão encerrada.")
                return

            print(f"Mensagem recebida: {message_in_bytes.decode()}")
            response = input("Digite resposta: ")
            client_connection.sendall(response.encode())
            print("Resposta enviada.")
 

# Now wait for client connections.
socket_server.listen(number_of_connections)
try:
    while True:
        client_connection: socket.socket
        addr: (str, int)
        # Establish connection with client.
        print(f"Esperando conexão: 127.0.0.1:{port}")
        client_connection, addr = socket_server.accept()
        print("Conectado")
        chat(client_connection)

except KeyboardInterrupt as erro:
    print(f"\nclosing server")
    socket_server.close()
    if client_connection:
        client_connection.close()
    exit(0)
