class ConsolePrinter:
    def print_success(self, message):
        print(f'\033[92m{message}\033[0m')
        # Green

    def print_failure(self, message):
        print(f'\033[91m{message}\033[0m')
        # Red

    def print_warning(self, message):
        print(f'\033[93m{message}\033[0m')
        # Yellow