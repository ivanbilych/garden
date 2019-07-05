#!/usr/bin/python3

import argparse
import json
import random
import socket
import time
import threading

NUMBER_OF_PACKAGES = 3
MAX_NEW_PACKAGE_WAIT_TIME_SEC = 10

PACKAGE_TEMPLATE_JSON = """
{
    "name": "",
    "amount": "",
    "value": "",
    "water": "",
    "frequency": "",
    "grow_time": ""
}
"""

PACKAGE_NAME_VARIANTS = (
    "Rose",
    "Violet",
    "Cactus",
    "Cherry",
    "Pineapple",
    "Watermelon",
    "Cucumber",
    "Tomato",
    "Orange",
    "Banana"
)

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

class SenderThread(threading.Thread):
    sender = None

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

    def run(self):
        self.sender = self.Sender(client_ip, client_port)

        self.sender.init_connection()
        self.generate_packages()
        self.sender.stop_connection()

    def generate_packages(self):
        times = NUMBER_OF_PACKAGES

        while times:
            times -= 1

            self.sender.send_package(self.generate_package_json())

            if times:
                time.sleep(random.randint(1, MAX_NEW_PACKAGE_WAIT_TIME_SEC))

    def generate_package_json(self):
        package = json.loads(PACKAGE_TEMPLATE_JSON)

        package["name"] = random.choice(PACKAGE_NAME_VARIANTS)
        package["amount"] = random.randint(1, 30)
        package["value"] = random.randint(1, 50)
        package["water"] = random.randint(1, 10)
        package["frequency"] = random.randint(1, 10)
        package["grow_time"] = random.randint(10, 30)

        return json.dumps(package)

def main():
    parse_command_line_arguments()

    gprint("Starting...\nServer port %d, client %s:%d" % (server_port, client_ip, client_port))

    sender_thread = SenderThread()

    sender_thread.start()
    sender_thread.join()

if __name__ == "__main__":
    main()
