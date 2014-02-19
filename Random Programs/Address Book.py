## Address Book.py by Palmer Paul, 2014
## Written in Python 3.3.4

## To add (in order of importance)
#JSON support using File I/O
#delete function
#edit function
#GUI
#command line compatibility
#splat the contact categories

import json

address_book = {}
contact_list_first = []
contact_list_last = []

def add_contact():
    print("Add Contact")

    firstname = str(input("First name: "))
    while not firstname.isalpha():
        print("Error: Invalid first name!")
        print("First names must be only alphanumeric characters and cannot contain spaces.")
        firstname = str(input("First name: "))

    lastname = str(input("Last name: "))
    while not lastname.isalpha():
        print("Error: Invalid last name!")
        print("Last names must be only alphanumeric characters and cannot contain spaces.")
        lastname = str(input("Last name: "))

    nickname = str(input("Nickname: "))
    while nickname.isspace():
        print("Error: Invalid nickname!")
        print("Nicknames cannot be all spaces.")
        nickname = str(input("Nickname: "))

    phonenumber = str(input("Phone number: "))
    while len(phonenumber) != 10 or phonenumber.isdigit() == False:
        if len(phonenumber) == 11 and phonenumber[0] == "1":
            phonenumber_temp = ""
            for x in range(1, len(phonenumber)):
                phonenumber_temp = phonenumber_temp + phonenumber[x]
            phonenumber = phonenumber_temp
        else:
            print("Error: Invalid phone number!")
            print("Phone numbers must be exactly 10 digits long.")
            phonenumber = str(input("Phone Number: "))
    phonenumber_temp2 = "("
    for x in range(3):
        phonenumber_temp2 = phonenumber_temp2 + phonenumber[x]
    phonenumber_temp2 = phonenumber_temp2 + ")-"
    for x in range(3, 6):
        phonenumber_temp2 = phonenumber_temp2 + phonenumber[x]
    phonenumber_temp2 = phonenumber_temp2 + "-"
    for x in range(6, 10):
        phonenumber_temp2 = phonenumber_temp2 + phonenumber[x]
    phonenumber = phonenumber_temp2

    emailaddress = str(input("Email address: "))
    while not "@" in emailaddress or not "." in emailaddress:
        print("Error: Invalid email!")
        emailaddress = str(input("Email address: "))

    contact_dict = {"first_name": firstname, "last_name": lastname, "nick": nickname, "phone": phonenumber, "email": emailaddress}
    address_book[firstname.lower()] = contact_dict
    address_book[lastname.lower()] = contact_dict
    address_book[nickname.lower()] = contact_dict
    address_book[phonenumber.lower()] = contact_dict
    address_book[emailaddress.lower()] = contact_dict
    contact_list_first.append(firstname.lower())
    contact_list_last.append(lastname.lower())

def search_contact():
    search = str(input("Search: "))
    search = search.lower()
    try:
        print(address_book[search])
        #print(address_book[search][first_name] + " \"" + address_book[search][nick] + "\" " + address_book[search][last_name])
        #print(address_book[search][phone])
        #print(address_book[search][email])
    except KeyError:
        print("Error: Contact not in address book!")


def print_all():
    arg1 = str(input("Sort by first name or last name: "))
    arg1 = arg1.lower()
    if arg1 == "first" or arg1 == "1" or arg1 == "f" or arg1 == "1st" or arg1 == "first name":
        contact_list_first.sort()
        for x in range(len(contact_list_first)):
            print(address_book[contact_list_first[x]])
            #print(address_book[contact_list_first[x]][first_name] + " \"" + address_book[contact_list_first[x]][nick]  + "\" " + address_book[contact_list_first[x]][last_name])
            #print(address_book[contact_list_first[x]][phone])
            #print(address_book[contact_list_first[x]][email])
    if arg1 == "last" or arg1 == "last name" or arg1 == "l":
        contact_list_last.sort()
        for x in range(len(contact_list_last)):
            print(address_book[contact_list_last[x]])
            #print(address_book[contact_list_first[x]][first_name] + " \"" + address_book[contact_list_first[x]][nick]  + "\" " + address_book[contact_list_first[x]][last_name])
            #print(address_book[contact_list_first[x]][phone])
            #print(address_book[contact_list_first[x]][email])

while True:
    command = str(input("Would you like to ADD a contact, SEARCH for a contact, SHOW ALL contacts, or QUIT? "))
    command = command.lower()
    print()
    while command != "add" and command != "search" and command != "show all" and command != "quit":
        print("Error: Command not recognized!")
        command = str(input("Would you like to ADD a contact, SEARCH for a contact, or SHOW ALL contacts? "))
        command = command.lower()
    if command == "add":
        add_contact()
        print()
        print("Contact added!")
    elif command == "search":
        search_contact()
    elif command == "show all":
        print_all()
    elif command == "quit":
        quit()
    print()
