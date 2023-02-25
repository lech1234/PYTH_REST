import socket


def server(host, port):
    with socket.socket() as server_socket:
        server_socket.bind((host, port))  # argument jest krotką
        server_socket.listen(1)
        print('Waiting for connection...')
        connection, address = server_socket.accept()  # oczekiwanie na połączenie
        with connection:
            print(f'Connection from host {address[0]} on port {address[1]}...')
            while True:
                client_message = connection.recv(1024).decode()  # odebranie danych od klienta
                if not client_message:
                    break
                print(f'[C]: {client_message}')
                server_message = input('[S]: ')
                connection.send(server_message.encode())  # wysłanie danych serwera
        print('Disconnected...')


if __name__ == '__main__':
    hostname = socket.gethostname()
    server(hostname, 9876)  # serwer startujemy lokalnie na porcie 9876
