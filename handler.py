from md import MD
from ssh import SSHToVM
from hex import hex_to_decimal
from time_convert import time_convert
from ilorest import ILOREST

def add_device_argument(parser):
    parser.add_argument("-d", "--device", dest='device', help="Hostname or IP address of the iBox")

def handle_md(args):
    ssh_client = None
    if args.device:
        ssh_client = SSHToVM(host=args.device)
        ssh_client.connect()

    if ssh_client:
        md = MD(ssh_client)

        if args.increase:
            md.increase()
        elif args.decrease:
            md.decrease()
        elif args.status:
            md.status()
        elif args.check:
            md.check_speed_increased()

        ssh_client.close()

def handle_hex(args):
    hex_to_decimal(args.hex)

def handle_convert(args):
    time_convert(args.value, args.from_unit, args.to_unit)

def handle_ilorest(args):
    if args.device:
        ssh_client = SSHToVM(host=args.device)
        ssh_client.connect()

        ilorest = ILOREST(ssh_client)

        if args.info:
            ilorest.server_info()

        ssh_client.close()

handlers = {
    'md': handle_md,
    'hex': handle_hex,
    'convert': handle_convert,
    'ilorest': handle_ilorest,
}