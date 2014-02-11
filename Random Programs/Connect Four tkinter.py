#Connect Four with Tkinter GUI by Palmer Paul, 2014

#!/usr/bin/env python

import tkinter as tk
from random import randint

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        self.userchoice = 0
        self.numturns = 0
        self.p1name = "Player 1"
        self.p1char = "X"
        self.p2name = "Player 2"
        self.p2char = "O"
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0
        self.turn = self.p1char

    def createWidgets(self):
        self.welcome_label = tk.Label(self)
        self.welcome_label["text"] = "Welcome to Connect Four"
        self.welcome_label.pack(side="top")
        
        self.text = tk.Text(self)
        self.text.pack(side="top")
        self.text.insert(tk.END, " ___________________________ \n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "  1   2   3   4   5   6   7  \n")
        
        self.row1_button = tk.Button(self)
        self.row1_button["text"] = "1"
        self.row1_button["command"] = self.row1_event
        self.row1_button.pack(side="left")

        self.row2_button = tk.Button(self)
        self.row2_button["text"] = "2"
        self.row2_button["command"] = self.row2_event
        self.row2_button.pack(side="left")

        self.row3_button = tk.Button(self)
        self.row3_button["text"] = "3"
        self.row3_button["command"] = self.row3_event
        self.row3_button.pack(side="left")

        self.row4_button = tk.Button(self)
        self.row4_button["text"] = "4"
        self.row4_button["command"] = self.row4_event
        self.row4_button.pack(side="left")

        self.row5_button = tk.Button(self)
        self.row5_button["text"] = "5"
        self.row5_button["command"] = self.row5_event
        self.row5_button.pack(side="left")

        self.row6_button = tk.Button(self)
        self.row6_button["text"] = "6"
        self.row6_button["command"] = self.row6_event
        self.row6_button.pack(side="left")

        self.row7_button = tk.Button(self)
        self.row7_button["text"] = "7"
        self.row7_button["command"] = self.row7_event
        self.row7_button.pack(side="left")

        self.settings_label = tk.Label(self)
        self.settings_label["text"] = "Settings"
        self.settings_label.pack(side="top")

        self.p1name_entry = tk.Entry(self)
        self.p1name_entry.pack(side="top")

        self.p1name_button = tk.Button(self)
        self.p1name_button["text"] = "Player 1 name"
        self.p1name_button["command"] = self.p1name_retrieve_input
        self.p1name_button.pack(side="top")

        self.p2name_entry = tk.Entry(self)
        self.p2name_entry.pack(side="top")

        self.p2name_button = tk.Button(self)
        self.p2name_button["text"] = "Player 2 name"
        self.p2name_button["command"] = self.p2name_retrieve_input
        self.p2name_button.pack(side="top")

        self.p1wins_label = tk.Label(self)
        self.p1wins_label.pack(side="right")

        self.p2wins_label = tk.Label(self)
        self.p2wins_label.pack(side="right")

        self.ties_label = tk.Label(self)
        self.ties_label.pack(side="right")

        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["command"] = root.destroy
        self.QUIT.pack(side="bottom")

    def print_board(self):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, " ___________________________ \n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][5] + " | " + self.board[1][5] + " | " + self.board[2][5] + " | " + self.board[3][5] + " | " + self.board[4][5] + " | " + self.board[5][5] + " | " + self.board[6][5] + " |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][4] + " | " + self.board[1][4] + " | " + self.board[2][4] + " | " + self.board[3][4] + " | " + self.board[4][4] + " | " + self.board[5][4] + " | " + self.board[6][4] + " |\n")
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][3] + " | " + self.board[1][3] + " | " + self.board[2][3] + " | " + self.board[3][3] + " | " + self.board[4][3] + " | " + self.board[5][3] + " | " + self.board[6][3] + " |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][2] + " | " + self.board[1][2] + " | " + self.board[2][2] + " | " + self.board[3][2] + " | " + self.board[4][2] + " | " + self.board[5][2] + " | " + self.board[6][2] + " |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][1] + " | " + self.board[1][1] + " | " + self.board[2][1] + " | " + self.board[3][1] + " | " + self.board[4][1] + " | " + self.board[5][1] + " | " + self.board[6][1] + " |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "|   |   |   |   |   |   |   |\n")
        self.text.insert(tk.END, "| " + self.board[0][0] + " | " + self.board[1][0] + " | " + self.board[2][0] + " | " + self.board[3][0] + " | " + self.board[4][0] + " | " + self.board[5][0] + " | " + self.board[6][0] + " |\n") 
        self.text.insert(tk.END, "|___|___|___|___|___|___|___|\n")
        self.text.insert(tk.END, "  1   2   3   4   5   6   7  \n")

    def place_piece(self):
        for x in range(0, 6):
            if self.board[self.userchoice][x] == " ":
                self.row = x
                if self.turn == self.p1char:
                    self.board[self.userchoice][x] = self.p1char
                elif self.turn == self.p2char:
                    self.board[self.userchoice][x] = self.p2char
                self.numturns+=1
                self.win_check()
                break
            else:
                if x>=5:
                    row = False
                else:
                    x+=1

    def win(self):
        self.print_board()
        if self.turn == self.p1char:
            self.p1wins+=1
            print(self.p1name.upper() + " WINS!")
        elif self.turn == self.p2char:
            self.p2wins+=1
            print(self.p2name.upper() + " WINS!")
        self.p1wins_label["text"] = self.p1name + ": " + str(self.p1wins) + " wins"
        self.p2wins_label["text"] = self.p2name + ": " + str(self.p2wins) + " wins"
        self.ties_label["text"] = "Ties: " + str(self.ties)
        #play_again()

    def win_check(self):
        if self.row>=3 and self.board[self.userchoice][self.row-3] == self.turn and self.board[self.userchoice][self.row-2] == self.turn and self.board[self.userchoice][self.row-1] == self.turn:
            self.board[self.userchoice][self.row-3] = "|"
            self.board[self.userchoice][self.row-2] = "|"
            self.board[self.userchoice][self.row-1] = "|"
            self.board[self.userchoice][self.row] = "|"
            self.win()
        if self.userchoice<=3 and self.board[self.userchoice+1][self.row] == self.turn and self.board[self.userchoice+2][self.row] == self.turn and self.board[self.userchoice+3][self.row] == self.turn:
            self.board[self.userchoice][self.row] = "-"
            self.board[self.userchoice+1][self.row] = "-"
            self.board[self.userchoice+2][self.row] = "-"
            self.board[self.userchoice+3][self.row] = "-"
            self.win()
        if self.userchoice>=1 and self.userchoice<=4 and self.board[self.userchoice-1][self.row] == self.turn and self.board[self.userchoice+1][self.row] == self.turn and self.board[self.userchoice+2][self.row] == self.turn:
            self.board[self.userchoice-1][self.row] = "-"
            self.board[self.userchoice][self.row] = "-"
            self.board[self.userchoice+1][self.row] = "-"
            self.board[self.userchoice+2][self.row] = "-"
            self.win()
        if self.userchoice>=2 and self.userchoice<=5 and self.board[self.userchoice-2][self.row] == self.turn and self.board[self.userchoice-1][self.row] == self.turn and self.board[self.userchoice+1][self.row] == self.turn:
            self.board[self.userchoice-2][self.row] = "-"
            self.board[self.userchoice-1][self.row] = "-"
            self.board[self.userchoice][self.row] = "-"
            self.board[self.userchoice+1][self.row] = "-"
            self.win()
        if self.userchoice>=3 and self.board[self.userchoice-3][self.row] == self.turn and self.board[self.userchoice-2][self.row] == self.turn and self.board[self.userchoice-1][self.row] == self.turn:
            self.board[self.userchoice-3][self.row] = "-"
            self.board[self.userchoice-2][self.row] = "-"
            self.board[self.userchoice-1][self.row] = "-"
            self.board[self.userchoice][self.row] = "-"
            self.win()
        if self.userchoice<=3 and self.row<=2 and self.board[self.userchoice+1][self.row+1] == self.turn and self.board[self.userchoice+2][self.row+2] == self.turn and self.board[self.userchoice+3][self.row+3] == self.turn:
            self.board[self.userchoice][self.row] = "/"
            self.board[self.userchoice+1][self.row+1] = "/" 
            self.board[self.userchoice+2][self.row+2] = "/"
            self.board[self.userchoice+3][self.row+3] = "/"
            self.win()
        if self.userchoice>=1 and self.row>=1 and self.userchoice<=4 and self.row<=3 and self.board[self.userchoice-1][self.row-1] == self.turn and self.board[self.userchoice+1][self.row+1] == self.turn and self.board[self.userchoice+2][self.row+2] == self.turn:
            self.board[self.userchoice-1][self.row-1] = "/"
            self.board[self.userchoice][self.row] = "/"
            self.board[self.userchoice+1][self.row+1] = "/"
            self.board[self.userchoice+2][self.row+2] = "/"
            self.win()
        if self.userchoice>=2 and self.row>=2 and self.userchoice<=5 and self.row<=4 and self.board[self.userchoice-2][self.row-2] == self.turn and self.board[self.userchoice-1][self.row-1] == self.turn and self.board[self.userchoice+1][self.row+1] == self.turn:
            self.board[self.userchoice-2][self.row-2] = "/"
            self.board[self.userchoice-1][self.row-1] = "/"
            self.board[self.userchoice][self.row] = "/"
            self.board[self.userchoice+1][self.row+1] = "/"
            self.win()
        if self.userchoice>=3 and self.row>=3 and self.board[self.userchoice-1][self.row-1] == self.turn and self.board[self.userchoice-2][self.row-2] == self.turn and self.board[self.userchoice-3][self.row-3] == self.turn:
            self.board[self.userchoice][self.row] = "/"
            self.board[self.userchoice-1][self.row-1] = "/"
            self.board[self.userchoice-2][self.row-2] = "/"
            self.board[self.userchoice-3][self.row-3] = "/"
            self.win()
        if self.userchoice<=3 and self.row>=3 and self.board[self.userchoice+1][self.row-1] == self.turn and self.board[self.userchoice+2][self.row-2] == self.turn and self.board[self.userchoice+3][self.row-3] == self.turn:
            self.board[self.userchoice][self.row] = "\\"
            self.board[self.userchoice+1][self.row-1] = "\\"
            self.board[self.userchoice+2][self.row-2] = "\\"
            self.board[self.userchoice+3][self.row-3] = "\\"
            self.win()
        if self.userchoice>=1 and self.row>=2 and self.userchoice<=4 and self.row<=4 and self.board[self.userchoice-1][self.row+1] == self.turn and self.board[self.userchoice+1][self.row-1] == self.turn and self.board[self.userchoice+2][self.row-2] == self.turn:
            self.board[self.userchoice-1][self.row+1] = "\\"
            self.board[self.userchoice][self.row] = "\\"
            self.board[self.userchoice+1][self.row-1] = "\\"
            self.board[self.userchoice+2][self.row-2] = "\\"
            self.win()
        if self.userchoice>=2 and self.row>=1 and self.userchoice<=5 and self.row<=3 and self.board[self.userchoice-2][self.row+2] == self.turn and self.board[self.userchoice-1][self.row+1] == self.turn and self.board[self.userchoice+1][self.row-1] == self.turn:
            self.board[self.userchoice-2][self.row+2] = "\\"
            self.board[self.userchoice-1][self.row+1] = "\\"
            self.board[self.userchoice][self.row] = "\\"
            self.board[self.userchoice+1][self.row-1] = "\\"
            self.win()
        if self.userchoice>=3 and self.row<=2 and self.board[self.userchoice-3][self.row+3] == self.turn and self.board[self.userchoice-2][self.row+2] == self.turn and self.board[self.userchoice-1][self.row+1] == self.turn:
            self.board[self.userchoice-3][self.row+3] = "\\"
            self.board[self.userchoice-2][self.row+2] = "\\"
            self.board[self.userchoice-1][self.row+1] = "\\"
            self.board[self.userchoice][self.row] = "\\"
            self.win()
        elif self.numturns>=42:
            self.ties+=1
            self.print_board()
            print("TIE!")
            self.p1wins_label["text"] = self.p1name + ": " + str(self.p1wins) + " wins"
            self.p2wins_label["text"] = self.p2name + ": " + str(self.p2wins) + " wins"
            self.ties_label["text"] = "Ties: " + str(self.ties)
            #play_again()
        else:
            self.print_board()
            if self.turn == self.p1char:
                self.turn = self.p2char
            elif self.turn == self.p2char:
                self.turn = self.p1char

    def play_again(self):
        pass

    def row1_event(self):
        self.userchoice = 0
        self.place_piece()
        if self.row != False:
            self.win_check()

    def row2_event(self):
        self.userchoice = 1
        self.place_piece()
        if self.row != False:
            self.win_check()

    def row3_event(self):
        self.userchoice = 2
        self.place_piece()
        if self.row != False:
            self.win_check()

    def row4_event(self):
        self.userchoice = 3
        self.place_piece()
        if self.row != False:
            self.win_check()
        
    def row5_event(self):
        self.userchoice = 4
        self.place_piece()
        if self.row != False:
            self.win_check()

    def row6_event(self):
        self.userchoice = 5
        self.place_piece()
        if self.row != False:
            self.win_check()

    def row7_event(self):
        self.userchoice = 6
        self.place_piece()
        if self.row != False:
            self.win_check()

    def p1name_retrieve_input(self):
        self.p1name = self.p1name_entry.get()

    def p2name_retrieve_input(self):
        self.p2name = self.p2name_entry.get()

root = tk.Tk()
app = Application(master=root)
app.master.title("Connect Four")
app.mainloop()
