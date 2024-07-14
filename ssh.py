import paramiko
import os

class SSHToVM:
    def __init__(self, host='', username='root', password=None, private_key_path=os.path.expanduser("~/.ssh/mfg_root_id")):
        self.host = host
        self.username = username
        self.password = password
        self.private_key_path = private_key_path
        self.ssh_client = None

        if paramiko:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        if self.ssh_client:
            try:
                if self.password:
                    self.ssh_client.connect(self.host, username=self.username, password=self.password)
                else:
                    self.ssh_client.connect(self.host, username=self.username, key_filename=self.private_key_path)

                print(f"SSH connection to {self.host} established.")
            except paramiko.AuthenticationException:
                print("Authentication failed. Please check your credentials.")
            except paramiko.SSHException as e:
                print(f"SSH connection error to {self.host}: {str(e)}")

    def execute_command(self, command):
        if self.ssh_client:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            return stdout.read().decode().strip()

    def close(self):
        if self.ssh_client:
            self.ssh_client.close()
            print(f"SSH connection to {self.host} closed.")