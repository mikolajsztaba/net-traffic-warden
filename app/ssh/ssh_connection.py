"""
SSH CONNECTION DOCSTRING
"""
import paramiko


def connect_to_ssh(hostname, port, username, password):
    """
    :param hostname:
    :param port:
    :param username:
    :param password:
    :return:
    """
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh_client.connect(hostname, port=port,
                           username=username, password=password)

        return ssh_client
    except paramiko.SSHException as error:
        print("Error connecting to SSH:", str(error))
        return None


def execute_ssh_command(ssh_client, command):
    """
    :param ssh_client:
    :param command:
    :return:
    """
    try:
        # Execute the command on the remote server
        stdin, stdout, stderr = ssh_client.exec_command(command)

        print(stdin, stderr)

        # Wait for the command to finish and get the return code
        return_code = stdout.channel.recv_exit_status()

        # Capture the command's output
        command_output = stdout.read().decode('utf-8')

        return return_code, command_output
    except paramiko.SSHException as error:
        print("Error executing SSH command:", str(error))
        return None, str(error)


def close_ssh_connection(ssh_client):
    """
    :param ssh_client:
    :return:
    """
    try:
        # Close the SSH connection
        ssh_client.close()
    except paramiko.SSHException as error:
        print("Error closing SSH connection:", str(error))
