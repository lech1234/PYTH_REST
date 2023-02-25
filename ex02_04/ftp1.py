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
    try:
        with paramiko.SSHClient() as ssh_client:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=hostname, username=username, port=port, password=password, look_for_keys=False)

            print('Creating SFTP client...')
            with ssh_client.open_sftp() as ftp_client:
                print('Contents of current directory:')
                for dir_item in ftp_client.listdir_iter('.'):
                    print(dir_item.longname)

                new_dir = 'pub/example'
                print(f'Changing  directory to: {new_dir}')
                ftp_client.chdir(new_dir)
                currrent_dir = ftp_client.getcwd()
                print(f'Current directory: {currrent_dir}')

                print('Downloading files...')
                for filename in ftp_client.listdir('.'):
                    if not filename.endswith('Small.png'):
                        print(f"Downloading file '{filename}': ", end='')
                        ftp_client.get(filename, 'remote/' + filename,
                                       callback=lambda current, total: print('#', end='' if current < total else '\n'))
                print('Closing SFTP client...')
            print('Closing SSH connection...')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
