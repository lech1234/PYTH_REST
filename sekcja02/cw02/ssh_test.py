import paramiko
import configparser as cp


def main():
    print('Odczyt parametrów konfiguracyjnych połączenia...')
    config = cp.ConfigParser()
    config.read('../config/credentials.ini')
    remote = config['rebex']
    hostname = remote['hostname']
    port = int(remote['port'])
    username = remote['username']
    password = remote['password']

    print('Tworzenie klienta SSH...')
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('Łączenie...')
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False)
        print('Czekam na polecenia do wykonania zdalnie [lub <Enter> aby zakończyć]...')
        while True:
            command = input(f'{username}@{hostname}:$ ')
            if not command:
                break
            std_in, std_out, std_err = ssh_client.exec_command(command)
            response = std_out.read().decode('utf-8')
            print(response)
        print('Zamknięcie połączenia...')


if __name__ == '__main__':
    main()
