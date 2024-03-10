import socket


def server(host, port):
    with socket.socket() as server_socket:
        server_socket.bind((host, port))  # argument jest krotką
        server_socket.listen(1)
        print('Oczekiwanie na połączenie z klientem...')
        connection, (ip, port) = server_socket.accept()
        with connection:
            print(f'Połączenie z adresu {ip} na porcie {port}...')
            while True:
                client_message = connection.recv(1024).decode()  # odebranie danych od klienta
                if not client_message:
                    break
                print(f'[KLIENT]: {client_message}')
                server_message = input('[SERWER]? ')
                connection.send(server_message.encode())  # wysłanie danych serwera
        print('Połączenie z klientem zakończone...')


if __name__ == '__main__':
    hostname = socket.gethostname()
    server(hostname, 9876)  # sekcja05 startujemy lokalnie na porcie 9876
