import json
import random
import socket
import time
import threading

import constants
from mgprint import gprint

class SenderThread(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)

        self.client_ip = ip
        self.client_port = port

    class Sender():
        def __init__(self, ip, port):
            self.client_ip = ip
            self.client_port = port

        def stop_connection(self):
            self.sock.close()

        def init_connection(self):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.client_ip, int(self.client_port)))

            gprint("sender connection created...")

        def send_package(self, package):
            self.sock.send(package.encode("utf8"))
            gprint("package sent: %s" % package)

    def run(self):
        gprint("starting sender...")

        self.sender = self.Sender(self.client_ip, self.client_port)

        self.sender.init_connection()
        self.generate_packages()
        self.sender.stop_connection()

    def generate_packages(self):
        times = constants.NUMBER_OF_PACKAGES

        while times:
            times -= 1

            self.sender.send_package(self.generate_package_json())

            if times:
                time.sleep(random.randint(1, constants.MAX_NEW_PACKAGE_WAIT_TIME_SEC))

    def generate_package_json(self):
        package = json.loads(constants.PACKAGE_TEMPLATE_JSON)

        package["name"] = random.choice(constants.PACKAGE_NAME_VARIANTS)
        package["amount"] = random.randint(1, 30)
        package["value"] = random.randint(1, 50)
        package["water"] = random.randint(1, 10)
        package["frequency"] = random.randint(1, 10)
        package["grow_time"] = random.randint(10, 30)

        return json.dumps(package)
