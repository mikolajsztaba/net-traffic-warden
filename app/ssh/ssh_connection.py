import paramiko


def connect_to_ssh(hostname, port, username, password):
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh_client.connect(hostname, port=port, username=username, password=password)

        return ssh_client
    except Exception as e:
        print("Error connecting to SSH:", str(e))
        return None


def execute_ssh_command(ssh_client, command):
    try:
        # Execute the command on the remote server
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Wait for the command to finish and get the return code
        return_code = stdout.channel.recv_exit_status()

        # Capture the command's output
        command_output = stdout.read().decode('utf-8')

        return return_code, command_output
    except Exception as e:
        print("Error executing SSH command:", str(e))
        return None, str(e)


def close_ssh_connection(ssh_client):
    try:
        # Close the SSH connection
        ssh_client.close()
    except Exception as e:
        print("Error closing SSH connection:", str(e))
