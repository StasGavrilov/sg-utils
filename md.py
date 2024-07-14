import time

class MD:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client

    def status(self):
        show_command = 'cat /proc/mdstat'

        try:
            output = self.ssh_client.execute_command(show_command)
            print("Output of 'cat /proc/mdstat':")
            print(output)
        except Exception as e:
            print(f'Failed to execute command: {show_command} - {e}')

    def _adjust_sync_speed(self, speed):
        md_devices = ['md0', 'md1', 'md2']
        for md_device in md_devices:
            command = f'echo {speed} > /sys/block/{md_device}/md/sync_speed_min'
            try:
                self.ssh_client.execute_command(command)
            except Exception as e:
                print(f'Failed to execute command: {command} - {e}')

    def increase(self):
        self._adjust_sync_speed(2000000)
        print('Speed increased.')

    def decrease(self):
        self._adjust_sync_speed(1000)
        print('Speed decreased.')

    def check_speed_increased(self):
        show_command = 'cat /proc/mdstat'
        min_required_speed = 150000
        max_attempts = 5
        attempt = 0

        while attempt < max_attempts:
            try:
                output = self.ssh_client.execute_command(show_command)
                lines = output.splitlines()
                for line in lines:
                    if 'speed=' in line:
                        parts = line.split('speed=')
                        speed_info = parts[1].split()[0]
                        current_speed_str = ''.join(filter(str.isdigit, speed_info))
                        if current_speed_str.isdigit():
                            current_speed = int(current_speed_str)
                            if current_speed >= min_required_speed:
                                print(f'Speed is increased to {current_speed} K/sec.')
                                return True
                print(f'Speed check attempt {attempt + 1}/{max_attempts}: Speed is not increased yet.')
            except Exception as e:
                print(f'Failed to execute command: {show_command} - {e}')

            attempt += 1
            time.sleep(3)

        print(f'Exceeded maximum attempts. Speed is not increased to {min_required_speed} K/sec.')
        return False
