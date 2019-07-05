#!/usr/bin/python3

import argparse
import random
import socket
import time
import threading

NUMBER_OF_PACKAGES = 3
MAX_NEW_PACKAGE_WAIT_TIME_SEC = 10

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

class Sender():
    client_ip = None
    client_port = None
    sock = None

    def __init__(self, ip, port):
        self.client_ip = ip
        self.client_port = port

    def stop_connection(self):
        self.sock.close()

    def init_connection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.client_ip, int(self.client_port)))

    def send_package(self, package):
        self.sock.send(package.encode("utf8"))
        gprint("package sent: %s" % package)

class SenderThread(threading.Thread):
    def run(self):
        sender = Sender(client_ip, client_port)

        sender.init_connection()
        self.generate_packages(sender)
        sender.stop_connection()

    def generate_packages(self, sender):
        times = NUMBER_OF_PACKAGES

        while times:
            times -= 1

            sender.send_package("dummy package")

            if times:
                time.sleep(random.randint(1, MAX_NEW_PACKAGE_WAIT_TIME_SEC))

def main():
    parse_command_line_arguments()

    gprint("Starting...\nServer port %d, client %s:%d" % (server_port, client_ip, client_port))

    sender_thread = SenderThread()

    sender_thread.start()
    sender_thread.join()

if __name__ == "__main__":
    main()
