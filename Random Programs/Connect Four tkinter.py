#!/usr/bin/env python

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        self.userchoice = 0
        self.numturns = 0
        self.turn = "X"

    def createWidgets(self):
        self.text = tk.Text(self)
        self.text.pack(side="top")
        
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

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def print_board(self):
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
                row = x
                if self.turn == "X":
                    self.board[self.userchoice][x] = "X"
                    self.turn = "O"
                elif self.turn == "O":
                    self.board[self.userchoice][x] = "O"
                    self.turn = "X"
                self.text.delete(1.0, tk.END)
                self.print_board()
                self.numturns+=1
                break
            else:
                if x>=5:
                    row = False
                else:
                    x+=1

    def row1_event(self):
        self.userchoice = 0
        self.place_piece()

    def row2_event(self):
        self.userchoice = 1
        self.place_piece()

    def row3_event(self):
        self.userchoice = 2
        self.place_piece()

    def row4_event(self):
        self.userchoice = 3
        self.place_piece()
        
    def row5_event(self):
        self.userchoice = 4
        self.place_piece()

    def row6_event(self):
        self.userchoice = 5
        self.place_piece()

    def row7_event(self):
        self.userchoice = 6
        self.place_piece()

root = tk.Tk()
app = Application(master=root)
app.master.title("Connect Four")
app.mainloop()
