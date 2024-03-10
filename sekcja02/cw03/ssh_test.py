import paramiko
import paramiko_expect
import configparser as cp


# UWAGA:
# w pliku config/credentials.ini trzeba utworzyć sekcję [sdf]
# i wpisać username i password własnego konta
def main():
    print('Odczyt parametrów konfiguracyjnych połączenia...')
    config = cp.ConfigParser()
    config.read('../config/credentials.ini')
    remote = config['sdf']
    hostname = remote['hostname']
    port = int(remote['port'])
    username = remote['username']
    password = remote['password']
    prompt = r'.*>\s*'

    print('Tworzenie klienta SSH...')
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('Łączenie...')
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False)

        with paramiko_expect.SSHClientInteraction(ssh_client, timeout=10, display=False, newline='\n',
                                                  encoding='cp850') as interact:
            interact.expect('.*Please press your BACKSPACE key:.*')
            interact.send('', newline='\b')
            interact.expect(r'\(continue\)')
            interact.send('')
            interact.expect(r'\(continue\)')
            interact.send('')
            interact.expect(prompt)
            print('Czekam na polecenia do wykonania zdalnie [lub <Enter> aby zakończyć]...')
            while True:
                command = input(f'{username}@{hostname}:$ ')
                if not command:
                    break
                interact.send(command)
                interact.expect(prompt)
                response = interact.current_output_clean
                print(response)
        print('Zamknięcie połączenia...')


if __name__ == '__main__':
    main()
