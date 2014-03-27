## Address Book.py by Palmer Paul, Started: February 16, 2014
## Written in Python 3.3.4

## Dependencies: Python 3, JSON module

## To do (in order of importance)
#handling of keys with same name
    #delete function support needed
#edit function
    #present current data and let user modify it
    #delete old data
    #create a new contact with updated data
#GUI
#make a "better" search that can account for typos and multiple keys (i.e. Search: Palmer Paul)
#command line compatibility
#splat the contact categories
    #make contact_list_first and contact_list_list dictionaries with the value equal to a list of the categories


## Import statement(s)
try:
    import json
except ImportError:
    print("Error: The JSON module, which this program depends on to run is not installed. To use this program, please install the latest version of this module.")
    raise SystemExit

## Gets data from file filename. If filename doesn't exist, it will be created.
filename = "data.txt"

try:
    fp_read = open(filename, "r")
    try:
        data_read = json.load(fp_read)
    except ValueError:
        data_read = [{}, [], []]
    fp_read.close()
except (FileNotFoundError, IOError):
    create = open(filename, "w")
    create.close()
    data_read = [{}, [], []]

address_book = data_read[0]
contact_list_first = data_read[1]
contact_list_last = data_read[2]

## Basic functions called by the program
def save_data():
    data_write = [address_book, contact_list_first, contact_list_last]
    fp_write = open(filename, "w")
    json.dump(data_write, fp_write)
    fp_write.close()

def clear_data():
    fp_write = open(filename, "w")
    json.dump([{}, [], []], fp_write)
    fp_write.close()

def better_input(s):
    i = input(s)
    if len(i) == 0:
        return i
    else:
        while i[0].isspace():
            i = i[1:]
        while i[-1].isspace():
            i = i[:-1]
        return i
    
def same_info(info):
    valid = False
    x = 0
    while valid == False:
        try:
            info = info + str(x)
            address_book[info]
            x += 1
            info = info[:-1]
        except KeyError:
            valid = True
    return info

def number_check(phonenumber):
    valid = False
    while valid == False:
        try:
            address_book[phonenumber]
            print("Error: This number is assigned to " + address_book[phonenumber]["first_name"] + " \"" + address_book[phonenumber]["nick"] + "\" " + address_book[phonenumber]["last_name"] + ".")
            phonenumber = better_input("Phone Number: ")
        except KeyError:
            valid = True
            while len(phonenumber) != 10 or phonenumber.isdigit() == False:
                if len(phonenumber) == 11 and phonenumber[0] == "1":
                    phonenumber_temp = ""
                    for x in range(1, len(phonenumber)):
                        phonenumber_temp = phonenumber_temp + phonenumber[x]
                    phonenumber = phonenumber_temp
                else:
                    print("Error: Invalid phone number!")
                    print("Phone numbers must be exactly 10 digits long.")
                    phonenumber = better_input("Phone Number: ")
                    number_check(phonenumber)
    return phonenumber

def email_check(email):
    valid = False
    while valid == False:
        try:
            address_book[email]
            print("Error: This email address is assigned to " + address_book[email]["first_name"] + " \"" + address_book[email]["nick"] + "\" " + address_book[email]["last_name"] + ".")
            email = better_input("Email address: ")
        except KeyError:
            valid = True
            while not "@" in email or not "." in email or not email[0].isalnum() or not email[-1].isalpha():
                print("Error: Invalid email!")
                email = better_input("Email address: ")
                email_check(email)
    return email

def specify(searchl):
    search = searchl[0]
    search_num = searchl[1]
    print("Multiple contacts found. Select which one you would like to delete by making your search more specific.")
    print()
    specific_list = search_contact("Specify: ", False)
    specific = specific_list[0]
    if specific == False:
        print("The information you entered did not match any of the contacts found.")
    else:
        specific_num = specific_list[1]
        for x in range(search_num):
            search = search + str(x)
            for y in range(specific_num):
                specific = specific + str(y)
                if address_book[search]["first_name"] == address_book[specific]["first_name"] and address_book[search]["nick"] == address_book[specific]["nick"] and address_book[search]["last_name"] == address_book[specific]["lasst_name"] and address_book[search]["phone"] == address_book[specific]["phone"] and address_book[search]["email"] == address_book[specific]["email"]:
                    print(address_book[search]["first_name"] + " \"" + address_book[search]["nick"] + "\" " + address_book[search]["last_name"])
                    print("Phone: " + address_book[search]["phone"])
                    print("Email: " + address_book[search]["email"])
                    delete_contact(search)

## Commands called by user
def add_contact():
    print("Add Contact")

    firstname = better_input("First name: ")
    while not firstname.isalpha():
        print("Error: Invalid first name!")
        print("First names must be only alphanumeric characters and cannot contain spaces.")
        firstname = better_input("First name: ")
    firstname = firstname.lower()
    firstname_format = firstname[0].upper() + firstname[1:].lower()
    firstname = same_info(firstname)

    lastname = better_input("Last name: ")
    while not lastname.isalpha():
        print("Error: Invalid last name!")
        print("Last names must be only alphanumeric characters and cannot contain spaces.")
        lastname = better_input("Last name: ")
    lastname = lastname.lower()
    lastname_format = lastname[0].upper() + lastname[1:].lower()
    lastname = same_info(lastname)

    nickname = better_input("Nickname: ")
    while nickname.isspace():
        print("Error: Invalid nickname!")
        print("Nicknames cannot be all spaces.")
        nickname = better_input("Nickname: ")
    nickname = same_info(nickname)

    phonenumber = better_input("Phone number: ")
    phonenumber = number_check(phonenumber)
    phonenumber_formatted = "(" + phonenumber[:3] + ")-" + phonenumber[3:6] + "-" + phonenumber[6:]

    emailaddress = better_input("Email address: ")
    emailaddress = email_check(emailaddress)

    contact_dict = {"first_name": firstname_format, "last_name": lastname_format, "nick": nickname, "phone": phonenumber_formatted, "email": emailaddress, "phone_raw": phonenumber}
    address_book[firstname] = contact_dict
    address_book[lastname] = contact_dict
    address_book[nickname] = contact_dict
    address_book[phonenumber_formatted] = contact_dict
    address_book[phonenumber] = contact_dict
    address_book[emailaddress] = contact_dict
    contact_list_first.append(firstname)
    contact_list_last.append(lastname)

def delete_contact(ui):
    if ui:
        search_list = search_contact("Delete: ", True)
        search = search_list[0]
    if not ui:
        search = ui
        search_num = ""
    if not search == False:
        search_num = search_list[1]
        search = search + str(search_num)
        if search_num == 0:
            confirm = better_input("WARNING: Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: ")
            confirm = confirm.lower()
            while confirm != "yes" and confirm != "no" and confirm != "y" and confirm != "n" and confirm != "delete" and confirm != "d":
                print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
                confirm = better_input("WARNING: Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: ")
                confirm = confirm.lower()
            if confirm == "yes" or confirm == "y" or confirm == "delete" or confirm == "d":
                contact_temp = address_book[search]
                try:
                    first_del = contact_temp["first_name"]
                    first_del = first_del.lower()
                    del address_book[first_del]

                    last_del = contact_temp["last_name"]
                    last_del = last_del.lower()
                    del address_book[last_del]

                    nick_del = contact_temp["nick"]
                    nick_del = nick_del.lower()
                    del address_book[nick_del]

                    phone_del = contact_temp["phone"]
                    del address_book[phone_del]

                    email_del = contact_temp["email"]
                    email_del = email_del.lower()
                    del address_book[email_del]

                    phone_raw_del = str(contact_temp["phone_raw"])
                    del address_book[phone_raw_del]

                    contact_list_first.remove(first_del)
                    contact_list_last.remove(last_del)
                except KeyError:
                    print("Error: This contact cannot be deleted.")
        elif search_num < 0:
            pass
        else:
            specify(search_list)

def search_contact(s, p):
    if len(contact_list_first) == 0 and len(contact_list_last) == 0:
        print("Address book is empty.")
        return False
    else:
        search = better_input(s)
        search = search.lower()
        search_orig = search
        x = 0
        while True:
            if not search.isdigit():
                while search[-1].isdigit():
                    search = search[:-1]
                search = search + str(x)
            try:
                if p:
                    print(address_book[search]["first_name"] + " \"" + address_book[search]["nick"] + "\" " + address_book[search]["last_name"])
                    print("Phone: " + address_book[search]["phone"])
                    print("Email: " + address_book[search]["email"])
                    if x > 0:
                        print()
                    if search.isdigit():
                        search = search + "0"
                else:
                    address_book[search]
                    if search.isdigit():
                        search = search + "0"
            except KeyError:
                if search == "cancel" or search == "c":
                    return [False, -1]
                elif x == 0 and not search.isdigit():
                    print("Error: Contact not in address book!")
                    return [False, -1]
                else:
                    return [search_orig, x-1]
            x += 1


def print_all():
    if len(contact_list_first) == 0 and len(contact_list_last) == 0:
        print("Address book is empty.")
        arg1 = False
    elif len(contact_list_first) == 1 and len(contact_list_last) == 1:
        arg1 = "first"
    elif len(contact_list_first) == 0 and not len(contact_list_last) == 0:
        arg1 = "last"
    elif not len(contact_list_first) == 0 and len(contact_list_last) == 0:
        arg1 = "first"
    else:
        arg1 = better_input("Sort by first name or last name: ")
        arg1 = arg1.lower()
        while not arg1 == "first" and not arg1 == "1" and not arg1 == "f" and not arg1 == "1st" and not arg1 == "first name" and not arg1 == "last" and not arg1 == "l" and not arg1 == "lastname" and not arg1 == "cancel" and not arg1 == "c":
            print("Sorry, I didn't get that. Please respond with \"first\", \"last\", or \"cancel\".")
            arg1 = better_input("Sort by first name or last name: ")
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
            try:
                print(address_book[contact_list_last[x]]["first_name"] + " \"" + address_book[contact_list_last[x]]["nick"]  + "\" " + address_book[contact_list_last[x]]["last_name"])
                print("Phone: " + address_book[contact_list_last[x]]["phone"])
                print("Email: " + address_book[contact_list_last[x]]["email"])
                if x < len(contact_list_last)-1:
                    print()
            except (KeyError, ValueError):
                pass

def edit_contact():
    pass

## Main loop
while True:
    command = better_input("Would you like to ADD a contact, SEARCH for a contact, show ALL contacts, DELETE a contact, CLEAR the entire address book, or QUIT? ")
    command = command.lower()
    print()
    while command != "add" and command != "search" and command != "all" and command != "delete" and command != "quit" and command != "clear":
        print("Error: Command not recognized!")
        print()
        command = better_input("Would you like to ADD a contact, SEARCH for a contact, show ALL contacts, DELETE a contact, CLEAR the entire address book, or QUIT? ")
        command = command.lower()
        print()
        
    if command == "add":
        add_contact()
        save_data()
        print()
        print("Contact added!")
        
    elif command == "search":
        search_contact("Search: ", True)
        
    elif command == "all":
        print_all()
        
    elif command == "delete":
        delete_contact(True)
        save_data()
        
    elif command == "clear":
        confirm = better_input("WARNING: Are you sure you would like to delete all the contacts from your address book? ")
        confirm = confirm.lower()
        while confirm != "yes" and confirm != "no" and confirm != "y" and confirm != "n":
            print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
            confirm = better_input("WARNING: Are you sure you would like to delete all the contacts from your address book? ")
            confirm = confirm.lower()
        if confirm == "yes" or confirm == "y":
            confirm2 = better_input("WARNING #2: This action is irreversible, and you will lose all your data. Are you absolutely positive that you would like to continue? ")
            confirm2 = confirm2.lower()
            while confirm2 != "yes" and confirm2 != "no" and confirm2 != "y" and confirm2 != "n":
                print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
                confirm2 = better_input("WARNING: This action is irreversible, and you will lose all your data. Are you absolutely positive that you would like to continue? ")
                confirm2 = confirm2.lower()
            if confirm2 == "yes" or confirm2 == "y":
                clear_data()
                address_book = {}
                contact_list_first = []
                contact_list_last = []
                print("All data has been cleared.")

    elif command == "quit":
        save_data()
        print("Quitting...")
        raise SystemExit
    print()
