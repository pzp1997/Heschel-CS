import json

class Contact(object):
    def __init__(self, first_name, last_name, nickname, phone_number, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.phone_number = phone_number
        self.email_address = email_address

    def print_info(self, name):
        myfile = open("address_book.txt", "r")
        text = myfile.read()
        text = text.split()
        for x in range(len(text)):
            if text[x] == name:
                print

        print(self.first_name + " " + "\"" + self.nickname + "\"" + " " + self.last_name)
        print("Phone Number: " + self.phone_number)
        print("Email Address: " + self.email_address)

    def address_book(self):
        text = open("address_book.txt", "w")
        text.write(self.first_name)
        text.write(self.last_name)
        text.write(self.nickname)
        text.write(self.phone_number)
        text.write(self.email_address)
        text.close()


def create_contact():
    print("Add Contact")

    firstname = str(input("First name: "))
    while " " in firstname or not firstname.isalnum():
        print("Error: Invalid first name!")
        print("First names must be only alphanumeric characters and cannot contain spaces.")
        firstname = str(input("First name: "))

    lastname = str(input("Last Name: "))
    while  " " in lastname or not lastname.isalnum():
        print("Error: Invalid last name!")
        print("Last names must be only alphanumeric characters and cannot contain spaces.")
        lastname = str(input("Last name: "))

    nickname = str(input("Nickname: "))
    valid_nick = False
    while valid_nick == False:
        for letter in range(len(nickname)):
            if nickname[letter] != " ":
                valid_nick = True
        if valid_nick == False:
            print("Error: Invalid nickname!")
            print("Nicknames cannot be all spaces.")
            nickname = str(input("Nickname: "))
    #nickname_temp = ""
    #for x in range(len(nickname)):
    #    if nickname[x] == " ":
    #        nickname_temp = nickname_temp + "_"
    #    else:
    #        nickname_temp = nickname_temp + nickname[x]
    #nickname = nickname_temp

    phonenumber = str(input("Phone Number: "))
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

    email = str(input("Email address: "))
    valid_email1 = False
    valid_email2 = False
    while valid_email1 == False or valid_email2 == False:
        for x in range(len(email)):
            if email[x] == "@":
                valid_email1 = True
            elif email[x] == ".":
                valid_email2 = True
        if valid_email1 == False or valid_email2 == False:
            print("Error: Invalid email!")
            email = str(input("Email address: "))

    new_contact = Contact(firstname, lastname, nickname, phonenumber, email)
    return new_contact