#!/usr/bin/python3

full_names = ["Fergus Smith","Shaun Coins","Hugo Bear","Bowie Taylor","Sophie Driver","Steven Kerb"]

for name in full_names:
    temp = name.split(' ')
    
    #print first and last name as is
    print(temp[0] + ' ' + temp[1])

    #concatenate first and last name
    print(temp[0] + temp[1])

    #concatenate first and last name with a period between
    print(temp[0] + '.' + temp[1])

    #concatenate first and last name with a hyphen between
    print(temp[0] + '-' + temp[1])

    #concatenatefirst inital last name
    print(temp[0][0] + temp[1])

    #concatenate first 3 letters of first name and first 3 letters of last name
    print(temp[0][0:3] + temp[1][0:3])
