import socket


def client(host, port):
    print('Próba nawiązania połączenia z serwerem...')
    with socket.socket() as client_socket:  # utworzenie gniazda
        try:
            client_socket.connect((host, port))  # łączenie z serwerem
        except ConnectionError as e:
            print(e)
            return
        print(f'Połączono z serwerem {host} na porcie {port} [Wpisz: bye, aby zakończyć konwersację]...')
        client_message = input('[KLIENT]? ')  # pobranie komunikatu od klienta

        while client_message.lower().strip() != 'bye':
            client_socket.send(client_message.encode())  # wysłanie komunikatu klienta
            server_message = client_socket.recv(1024).decode()  # odebranie komunikatu odpowiedzi z serwera
            print(f'[SERWER]: {server_message}')

            client_message = input('[KLIENT]: ')
        print('Połączenie z serwerem zakończone...')


if __name__ == '__main__':
    hostname = socket.gethostname()
    client(hostname, 9876)  # klient łączy się z lokalnym serwerem na porcie 9876
