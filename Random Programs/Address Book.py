## Address Book.py by Palmer Paul, Started: February 16, 2014
## Written in Python 3.3.4

## To do (in order of importance)
#handling of keys with same name
    #basic framework made, needs debugging
#edit function
    #present current data and let user modify it
    #delete old data
    #create a new contact with updated data
#GUI
#make a "better" search
#command line compatibility
#splat the contact categories
    #make contact_list_first and contact_list_list dictionaries with the value equal to a list of the categories

try:
    import json
except ImportError:
    print("Error: The JSON module, which this program depends on to run is not installed. To use this program, please install the latest version of this module.")
    raise SystemExit
        
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

address_book = data_read[0]
contact_list_first = data_read[1]
contact_list_last = data_read[2]

def save_data():
    data_write = [address_book, contact_list_first, contact_list_last]
    fp_write = open(filename, "w")
    json.dump(data_write, fp_write)
    fp_write.close()

def clear_data():
    fp_write = open(filename, "w")
    json.dump([{}, [], []], fp_write)
    fp_write.close()
    
def same_info(info):
    valid = False
    x = 0
    while valid == False:
        try:
            address_book[info]
            info = info + str(x)
            x += 1
        except KeyError:
            valid = True
    return info

def number_check(phonenumber):
    valid = False
    while valid == False:
        try:
            address_book[phonenumber]
            print("Error: This number is assigned to " + address_book[phonenumber]["first_name"] + " \"" + address_book[phonenumber]["nick"] + "\" " + address_book[phonenumber]["last_name"] + ".")
            phonenumber = str(input("Phone Number: "))
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
                    phonenumber = str(input("Phone Number: "))
                    number_check(phonenumber)
    return phonenumber

def email_check(email):
    valid = False
    while valid == False:
        try:
            address_book[email]
            print("Error: This email address is assigned to " + address_book[email]["first_name"] + " \"" + address_book[email]["nick"] + "\" " + address_book[email]["last_name"] + ".")
            email = str(input("Email address: "))
        except KeyError:
            valid = True
            while not "@" in email or not "." in email:
                print("Error: Invalid email!")
                email = str(input("Email address: "))
                email_check(email)
    return email


def add_contact():
    print("Add Contact")

    firstname = str(input("First name: "))
    while not firstname.isalpha():
        print("Error: Invalid first name!")
        print("First names must be only alphanumeric characters and cannot contain spaces.")
        firstname = str(input("First name: "))
    firstname = same_info(firstname)

    lastname = str(input("Last name: "))
    while not lastname.isalpha():
        print("Error: Invalid last name!")
        print("Last names must be only alphanumeric characters and cannot contain spaces.")
        lastname = str(input("Last name: "))
    lastname = same_info(lastname)

    nickname = str(input("Nickname: "))
    while nickname.isspace():
        print("Error: Invalid nickname!")
        print("Nicknames cannot be all spaces.")
        nickname = str(input("Nickname: "))
    nickname = same_info(nickname)

    phonenumber = str(input("Phone number: "))
    phonenumber = number_check(phonenumber)
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
    emailaddress = email_check(emailaddress)

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
    if not search == False:
        confirm = str(input("WARNING: Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: "))
        confirm = confirm.lower()
        while confirm != "yes" and confirm != "no" and confirm != "y" and confirm != "n" and confirm != "delete" and confirm != "d":
            print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
            confirm = str(input("WARNING: Are you sure you would like to delete " + str(address_book[search]["first_name"]) + " from your address book? Note that this action is irreversible: "))
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
        elif confirm == "no" or confirm == "n":
            pass

def search_contact():
    if len(contact_list_first) == 0 and len(contact_list_last) == 0:
        print("Address book is empty.")
        return False
    else:
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
        print("Address book is empty.")
        arg1 = False
    elif len(contact_list_first) == 1 and len(contact_list_last) == 1:
        arg1 = "first"
    elif len(contact_list_first) == 0 and not len(contact_list_last) == 0:
        arg1 = "last"
    elif not len(contact_list_first) == 0 and len(contact_list_last) == 0:
        arg1 = "first"
    else:
        arg1 = str(input("Sort by first name or last name: "))
        arg1 = arg1.lower()
        while not arg1 == "first" and not arg1 == "1" and not arg1 == "f" and not arg1 == "1st" and not arg1 == "first name" and not arg1 == "last" and not arg1 == "l" and not arg1 == "lastname" and not arg1 == "cancel" and not arg1 == "c":
            print("Sorry, I didn't get that. Please respond with \"first\", \"last\", or \"cancel\".")
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

while True:
    command = str(input("Would you like to ADD a contact, SEARCH for a contact, SHOW ALL contacts, DELETE a contact, CLEAR the entire address book, or QUIT? "))
    command = command.lower()
    print()
    while command != "add" and command != "search" and command != "show all" and command != "delete" and command != "quit" and command != "clear":
        print("Error: Command not recognized!")
        print()
        command = str(input("Would you like to ADD a contact, SEARCH for a contact, SHOW ALL contacts, DELETE a contact, CLEAR the entire address book, or QUIT? "))
        command = command.lower()
        print()
        
    if command == "add":
        add_contact()
        save_data()
        print()
        print("Contact added!")
        
    elif command == "search":
        search_contact()
        
    elif command == "show all":
        print_all()
        
    elif command == "delete":
        delete_contact()
        save_data()
        
    elif command == "clear":
        confirm = str(input("WARNING: Are you sure you would like to delete all the contacts from your address book? "))
        confirm = confirm.lower()
        while confirm != "yes" and confirm != "no" and confirm != "y" and confirm != "n":
            print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
            confirm = str(input("WARNING: Are you sure you would like to delete all the contacts from your address book? "))
            confirm = confirm.lower()
        if confirm == "yes" or confirm == "y":
            confirm2 = str(input("WARNING #2: This action is irreversible, and you will lose all your data. Are you absolutely positive that you would like to continue? "))
            confirm2 = confirm2.lower()
            while confirm2 != "yes" and confirm2 != "no" and confirm2 != "y" and confirm2 != "n":
                print("Sorry, I could not understand you. Please respond with \"yes\" or \"no\".")
                confirm2 = str(input("WARNING: This action is irreversible, and you will lose all your data. Are you absolutely positive that you would like to continue? "))
                confirm2 = confirm2.lower()
            if confirm2 == "yes" or confirm2 == "y":
                clear_data()
                print("All data has been cleared.")

    elif command == "quit":
        save_data()
        print("Quitting...")
        raise SystemExit
    print()
