## Address Book.py by Palmer Paul, 2014
## Written in Python 3.3.4

## To add (in order of importance)
#fix regression when print_all() with no contacts
#handling of keys with same name
#edit function
#GUI
#command line compatibility
#splat the contact categories

import json

filename = "data.txt"

fp_read = open(filename, "r")
data_read = json.load(fp_read)
fp_read.close()

address_book = data_read[0]
contact_list_first = data_read[1]
contact_list_last = data_read[2]

def save_data():
    data_write = [address_book, contact_list_first, contact_list_last]
    fp_write = open(filename, "w")
    json.dump(data_write, fp_write)
    fp_write.close()

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
    phonenumber_formatted = "("
    for x in range(3):
        phonenumber_formatted = phonenumber_formatted + phonenumber[x]
    phonenumber_formatted = phonenumber_formatted + ")-"
    for x in range(3, 6):
        phonenumber_formatted = phonenumber_formatted + phonenumber[x]
    phonenumber_formatted = phonenumber_formatted + "-"
    for x in range(6, 10):
        phonenumber_formatted = phonenumber_formatted + phonenumber[x]

    emailaddress = str(input("Email address: "))
    while not "@" in emailaddress or not "." in emailaddress:
        print("Error: Invalid email!")
        emailaddress = str(input("Email address: "))

    contact_dict = {"first_name": firstname, "last_name": lastname, "nick": nickname, "phone": phonenumber_formatted, "email": emailaddress, "phone_raw": phonenumber}
    address_book[firstname.lower()] = contact_dict
    address_book[lastname.lower()] = contact_dict
    address_book[nickname.lower()] = contact_dict
    address_book[phonenumber_formatted] = contact_dict
    address_book[phonenumber] = contact_dict
    address_book[emailaddress.lower()] = contact_dict
    contact_list_first.append(firstname.lower())
    contact_list_last.append(lastname.lower())

def delete_contact():
    search = search_contact()
    if search != False:
        confirm = str(input("Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: "))
        confirm = confirm.lower()
        while confirm != "yes" and confirm != "no" and confirm != "y" and confirm != "n" and confirm != "delete" and confirm != "d":
            print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
            confirm = str(input("Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: "))
            confirm = confirm.lower()
        if confirm == "yes" or confirm == "y" or confirm == "delete" or confirm == "d":
            try:
                first_del = address_book[search]["first_name"]
                first_del = first_del.lower()
                del address_book[first_del]
            except KeyError:
                first_del = False

            try:
                last_del = address_book[search]["last_name"]
                last_del = last_del.lower()
                del address_book[last_del]
            except KeyError:
                last_del = False

            try:
                nick_del = address_book[search]["nick"]
                nick_del = nick_del.lower()
                del address_book[nick_del]
            except KeyError:
                pass

            try:
                phone_del = address_book[search]["phone"]
                phone_del = phone_del.lower()
                del address_book[phone_del]
            except KeyError:
                pass

            try:
                email_del = address_book[search]["email"]
                email_del = email_del.lower()
                del address_book[email_del]
            except KeyError:
                pass

            try:
                phone_raw_del = address_book[search]["phone_raw"]
                phone_raw_del = phone_raw_del.lower()
                del address_book[phone_raw_del]
            except KeyError:
                pass

            try:
                contact_list_first.remove(first_del)
            except ValueError:
                pass

            try:
                contact_list_last.remove(last_del)
            except ValueError:
                pass

        if confirm == "no" or confirm == "n":
            pass

def search_contact():
    search = str(input("Search: "))
    search = search.lower()
    try:
        print(address_book[search]["first_name"] + " \"" + address_book[search]["nick"] + "\" " + address_book[search]["last_name"])
        print("Phone: " + address_book[search]["phone"])
        print("Email: " + address_book[search]["email"])
        return search
    except KeyError:
        print("Error: Contact not in address book!")
        return False


def print_all():
    if len(contact_list_first) == 0 and len(contact_list_last) == 0:
        print("No contacts in address book.")
        arg1 = False
    elif len(contact_list_first) == 0 and not len(contact_list_last) == 0:
        arg1 = "last"
    elif not len(contact_list_first) == 0 and len(contact_list_last) == 0:
        arg1 = "first"
    else:
        arg1 = str(input("Sort by first name or last name: "))
        arg1 = arg1.lower()

    if arg1 == False:
        pass
    elif arg1 == "first" or arg1 == "1" or arg1 == "f" or arg1 == "1st" or arg1 == "first name":
        contact_list_first.sort()
        for x in range(len(contact_list_first)):
            print(address_book[contact_list_first[x]]["first_name"] + " \"" + address_book[contact_list_first[x]]["nick"]  + "\" " + address_book[contact_list_first[x]]["last_name"])
            print("Phone: " + address_book[contact_list_first[x]]["phone"])
            print("Email: " + address_book[contact_list_first[x]]["email"])
            if x < len(contact_list_first)-1:
                print()
    elif arg1 == "last" or arg1 == "last name" or arg1 == "l":
        contact_list_last.sort()
        for x in range(len(contact_list_last)):
            print(address_book[contact_list_first[x]]["first_name"] + " \"" + address_book[contact_list_first[x]]["nick"]  + "\" " + address_book[contact_list_first[x]]["last_name"])
            print("Phone: " + address_book[contact_list_first[x]]["phone"])
            print("Email: " + address_book[contact_list_first[x]]["email"])
            if x < len(contact_list_last)-1:
                print()

def edit_contact():
    contact = search_contact()


while True:
    command = str(input("Would you like to ADD a contact, SEARCH for a contact, SHOW ALL contacts, DELETE a contact, or QUIT? "))
    command = command.lower()
    print()
    while command != "add" and command != "search" and command != "show all" and command != "delete" and command != "quit":
        print("Error: Command not recognized!")
        command = str(input("Would you like to ADD a contact, SEARCH for a contact, SHOW ALL contacts, DELETE a contact, or QUIT? "))
        command = command.lower()
        print()
    if command == "add":
        add_contact()
        print()
        print("Contact added!")
        save_data()
    elif command == "search":
        search_contact()
    elif command == "show all":
        print_all()
    elif command == "delete":
        delete_contact()
        save_data()
    elif command == "quit":
        save_data()
        quit()
    print()
