#!/usr/bin/python3

import argparse

client_ip = None
client_port = None
server_port = None
verbosity = False

def gprint(message):
    if verbosity:
        print(message)

def parse_command_line_arguments():
    global client_ip, client_port, server_port, verbosity

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="print debug information", action="store_true")
    parser.add_argument("client_ip", help="client IP address")
    parser.add_argument("client_port", help="client port", type=int)
    parser.add_argument("server_port", help="server port", type=int)

    args = parser.parse_args()

    client_ip = args.client_ip
    client_port = args.client_port
    server_port = args.server_port
    verbosity = args.verbose

def main():
    parse_command_line_arguments()

    gprint("Starting...\nServer port %d, client %s:%d" % (server_port, client_ip, client_port))

if __name__ == "__main__":
    main()
