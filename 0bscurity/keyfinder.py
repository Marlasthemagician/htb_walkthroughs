#!/usr/bin/python3

with open("./loot/out.txt.orig", 'r', encoding='UTF-8') as f1:
    outchars = f1.read()

with open("./loot/check.txt", 'r', encoding='UTF-8') as f2:
    checkchars = f2.read()

key = ""
for char in range(len(checkchars)):
    for keyval in range(255):
        if ((ord(checkchars[char]) + keyval) % 255 == ord(outchars[char])):
            key = key + chr(keyval)

print(key)
