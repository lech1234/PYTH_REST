import socket


def client(host, port):
    print('Trying to connect...')
    with socket.socket() as client_socket:  # instantiate
        client_socket.connect((host, port))  # connect to the server
        print(f'Connected to host {host} on port {port}...')
        client_message = input('[C]: ')  # take input

        while client_message.lower().strip() != 'bye':
            client_socket.send(client_message.encode())  # wysłanie komunikatu klienta
            server_message = client_socket.recv(1024).decode()  # odebranie komunikatu od serwera
            print(f'[S]: {server_message}')

            client_message = input('[C]: ')
        print('Disconnected...')


if __name__ == '__main__':
    hostname = socket.gethostname()
    client(hostname, 9876)  # klient łączy się z lokalnym serwerem na porcie 9876
