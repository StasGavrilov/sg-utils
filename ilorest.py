class ILOREST:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client

    def server_info(self):
        show_command = 'ilorest serverinfo --firmware'

        try:
            output = self.ssh_client.execute_command(show_command)
            print(output)
        except Exception as e:
            print(f'Failed to execute command: {show_command} - {e}')