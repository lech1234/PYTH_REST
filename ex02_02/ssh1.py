import paramiko
import configparser as cp


def main():
    print('Reading connection parameters...')
    config = cp.ConfigParser()
    config.read('../ex02_config/credentials.ini')
    remote = config['rebex']
    hostname = remote['hostname']
    port = int(remote['port'])
    username = remote['username']
    password = remote['password']

    print('Creating SSH client...')
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('Connecting...')
        ssh_client.connect(hostname=hostname, port=port, username=username, password=password, look_for_keys=False)
        print('Waiting for remote commands to run...')
        while True:
            command = input(f'{username}@{hostname}:$ ')
            if not command:
                break
            std_in, std_out, std_err = ssh_client.exec_command(command)
            response = std_out.read().decode('utf-8')
            print(response)
        print('Closing connection...')


if __name__ == '__main__':
    main()
