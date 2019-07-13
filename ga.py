#!/usr/bin/python3

import argparse
import socket

import garden
import mgprint
from mgprint import gprint
import receiver
import sender

client_ip = None
client_port = None
server_port = None

def parse_command_line_arguments():
    global client_ip, client_port, server_port

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="print debug information", action="store_true")
    parser.add_argument("client_ip", help="client IP address")
    parser.add_argument("client_port", help="client port", type=int)
    parser.add_argument("server_port", help="server port", type=int)

    args = parser.parse_args()

    client_ip = args.client_ip
    client_port = args.client_port
    server_port = args.server_port
    mgprint.set_verbosity(args.verbose)

def main():
    parse_command_line_arguments()

    gprint("START")
    gprint("server: %s:%d" % (socket.gethostbyname(socket.gethostname()), server_port))
    gprint("client: %s:%d" % (client_ip, client_port))

    my_garden = garden.Garden()
    sender_thread = sender.SenderThread(client_ip, client_port)
    receiver_thread = receiver.ReceiverThread(my_garden, server_port)

    sender_thread.start()
    receiver_thread.start()

    my_garden.start()

    sender_thread.join()
    receiver_thread.join()

    gprint("STOP")

if __name__ == "__main__":
    main()
