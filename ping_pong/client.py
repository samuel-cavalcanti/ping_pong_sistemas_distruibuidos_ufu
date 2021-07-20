# client.py

import socket                          # Import socket module


server_connection = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.
buffer_size_in_bits = 1024

print("Conectando-se ao servidor")
server_connection.connect((host, port))
print("Conectado")

while True:
    message = input("Digite uma mensagem: ")
    server_connection.sendall(message.encode())

    print(f"Mensagem enviada")
    print("Esperando resposta")
    message_in_bytes = server_connection.recv(buffer_size_in_bits)
    if not message_in_bytes:
        print("Desconectando.")
        exit(1)

    print(f"Resposta recebida :{message_in_bytes.decode()}")