#!/opt/homebrew/bin/python3

import argparse

from handler import handlers

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script description")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for MD operations
    parser_md = subparsers.add_parser('md', help='MD operations')
    parser_md.add_argument("-d", "--device", dest='device', help="Hostname or IP address of the iBox")
    parser_md.add_argument("-i", '--increase', dest='increase', action='store_true', help='Increase MD sync speed')
    parser_md.add_argument("-r", '--decrease', dest='decrease', action='store_true', help='Decrease MD sync speed')
    parser_md.add_argument("-s", '--status', dest='status', action='store_true', help='Show MD status')
    parser_md.add_argument("-c", '--check', dest='check', action='store_true', help='Check if MD speed increased')
    parser_md.set_defaults(func=handlers['md'])

    # Subparser for Hex operations
    parser_hex = subparsers.add_parser('hex', help='Hexadecimal operations')
    parser_hex.add_argument("-x", "--hex", dest='hex', type=str, help="The hexadecimal address (e.g., 0xc).")
    parser_hex.set_defaults(func=handlers['hex'])

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()

