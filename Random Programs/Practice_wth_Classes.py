import tkinter as tk
import json

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.d_master = {}
        self.first_name = ""
        self.last_name = ""
        self.nickname = ""
        self.phone_number = ""
        self.email_address = ""

    def createWidgets(self):
        self.QUIT = tk.Button(self, text = "QUIT", command = self.quit)
        self.QUIT.pack(side="right")

        self.add_button = tk.Button(self, text = "Add Contact", command = self.add_contact())
        self.add_button.pack(side="right")

        self.print_all_button = tk.Button(self, text = "Address Book", command = self.print_all())
        self.print_all_button.pack(side="left")

        self.text_main = tk.Text(self)
        self.text_main.pack(side="left")

        self.text_error = tk.Text(self)
        self.text_error.pack(side="right")

        self.first_name_label = tk.Label(self, text = "First name")
        self.first_name_label.pack(side="right")

        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.pack(side="right")

        self.last_name_label = tk.Label(self, text = "Last name")
        self.last_name_label.pack(side="right")

        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack(side="right")

        self.nickname_label = tk.Label(self, text = "Nickname")
        self.nickname_label.pack(side="right")

        self.nickname_entry = tk.Entry(self)
        self.nickname_entry.pack(side="right")

        self.phone_number_label = tk.Label(self, text = "Phone number")
        self.phone_number_label.pack(side="right")

        self.phone_number_entry = tk.Entry(self)
        self.phone_number_entry.pack(side="right")

        self.email_label = tk.Label(self, text = "Email address")
        self.email_label.pack(side="right")

        self.email_entry = tk.Entry(self)
        self.email_entry.pack(side="right")

    def add_contact(self):
        self.error = False

        self.first_name = self.first_name_entry.get()
        while " " in self.first_name or not self.first_name.isalnum():
            self.text_error.insert(tk.END, "Error: Invalid first name!\nFirst names must be only alphanumeric characters and cannot contain spaces.\n")
            self.error = True
        self.error = False

        self.last_name = self.last_name_entry.get()
        while  " " in self.lastname or not self.lastname.isalnum():
            self.text_error.insert(tk.END, "Error: Invalid last name!\nLast names must be only alphanumeric characters and cannot contain spaces.\n")
            self.error = True
        self.error = False

        self.nickname = self.nickname_entry.get()
        self.phone_number = self.phone_number_entry.get()
        self.email_address = self.email_entry.get()

        dict_contact = {"firstname": self.first_name, "lastname": self.last_name, "nick": self.nickname, "phone": self.phone_number, "email": self.email_address}
        self.d_master[self.first_name] = dict_contact
        self.d_master[self.last_name] = dict_contact
        self.d_master[self.nickname] = dict_contact
        self.d_master[self.phone_number] = dict_contact
        self.d_master[self.phone_number] = dict_contact

        text = open("address_book.txt", "a")
        text.write(self.first_name + "\n")
        text.write(self.last_name + "\n")
        text.write(self.nickname + "\n")
        text.write(self.phone_number + "\n")
        text.write(self.email_address + "\n")
        text.write("\n")
        text.close()

    def print_all(self):
        myfile = open("address_book.txt", "r")
        text = myfile.read()
        #counter = 0
        #for x in range(len(text)):
        #    if text[x] == "\\" and text[x+1] == "n":
        #        counter += 1
        self.text_main.delete(1.0, tk.END)
        #for x in range(counter):
        #    self.text_main.insert(tk.END, myfile.readline() + "\n")
        self.text_main.insert(tk.END, text)

root = tk.Tk()
app = Application(master=root)
app.master.title("Address Book")
app.mainloop()
