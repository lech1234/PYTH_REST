import paramiko
import paramiko_expect
import configparser as cp


# UWAGA:
# pliku ex02_config/credentials.ini trzeba utworzyć sekcję [sdf]
# i wpisać username i password własnego konta
def main():
    print('Reading connection parameters...')
    config = cp.ConfigParser()
    config.read('../ex02_config/credentials.ini')
    remote = config['sdf']
    hostname = remote['hostname']
    port = int(remote['port'])
    username = remote['username']
    password = remote['password']
    prompt = r'.*>\s*'

    print('Creating SSH client...')
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('Connecting...')
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
            print('Waiting for remote commands to run...')
            while True:
                command = input(f'{username}@{hostname}:$ ')
                if not command:
                    break
                interact.send(command)
                interact.expect(prompt)
                cmd_output = interact.current_output_clean
                print(cmd_output)
        print('Closing connection...')


if __name__ == '__main__':
    main()
