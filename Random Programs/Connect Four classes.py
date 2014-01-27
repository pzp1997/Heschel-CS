#Connect Four by Palmer Paul, 2014

##bugs
#used globals
#playagain-->no doesn't cause game to stop (regression caused by removing the var four_in_row)
    #necessary to remove that var to stop players from getting "multi-wins" on one game

print("Welcome to Connect Four")
print()

class foo:
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        self.p1char = "X"
        self.p2char = "O"
        self.p1name = "Player 1"
        self.p2name = "Player 2"
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0
        self.turns = 0

    def settings(self):
        print()
        print("Player 1")
        self.p1name = str(input("What is your name? "))
        self.p1char = str(input("Choose one character to \"represent you\" on the board: "))
        while len(self.p1char) != 1 or self.p1char == " ":
            if len(self.p1char) != 1:
                print("You must input a single character!")
                self.p1char = str(input("Choose one character to \"represent you\" on the board: "))
            elif self.p1char == " ":
                print("Your character cannot be a space!")
                self.p1char = str(input("Choose one character to \"represent you\" on the board: "))
            else:
                break
        print()
        print("Player 2")
        self.p2name = str(input("What is your name? "))
        while self.p2name.lower() == self.p1name.lower():
            print("Please choose a different name than " + self.p1name)
            self.p2name = str(input("What is your name? "))
        self.p2char = str(input("Choose one character to \"represent you\" on the board: "))
        while len(self.p2char) != 1 or self.p2char == " " or self.p2char == self.p1char:
            if len(self.p2char) != 1:
                print("You must input a single character!")
                self.p2char = str(input("Choose one character to \"represent you\" on the board: "))            
            elif self.p2char == " ":
                print("Your character cannot be a space!")
                self.p2char = str(input("Choose one character to \"represent you\" on the board: "))
            elif self.p2char == self.p1char:
                print("You can't choose the same character as " + self.p1name + "!")
                self.p2char = str(input("Choose one character to \"represent you\" on the board: "))
            else:
                break
        game()

        def user_turn(self, player):
            userchoice = str(input("Choose a column (1-7): "))
            while userchoice != "1" and userchoice != "2" and userchoice != "3" and userchoice != "4" and userchoice != "5" and userchoice != "6" and userchoice != "7":
                print("You must input a whole number between 1 and 7...")
                userchoice = str(input("Choose a column (1-7): "))
            userchoice = int(userchoice)-1
    
            for x in range(0, 6):
                if board[userchoice][x] == " ":
                    row = x
                    oard[userchoice][x] = player
                    turns+=1
                    break
                else:
                    if x>=5:
                        print("You cannot go in this column.")
                        row = False
                        user_turn(player)
                    else:
                        x+=1

            def win():
                global p1wins, p2wins, ties
                print_board()
                print()
                if player == self.p1char:
                    self.p1wins+=1
                    print(self.p1name.upper() + " WINS!")
                elif player == self.p2char:
                    self.p2wins+=1
                    print(self.p2name.upper() + " WINS!")
                print()
                print(self.p1name + ": " + str(self.p1wins) + " wins")
                print(self.p2name + ": " + str(self.p2wins) + " wins")
                print("Ties: " + str(self.ties))
                print()
                play_again()
         
    if row>=3 and board[userchoice][row-3] == player and board[userchoice][row-2] == player and board[userchoice][row-1] == player:
            win()
    if userchoice<=3 and board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
            win()
    if userchoice>=1 and userchoice<=4 and board[userchoice-1][row] == player and board[userchoice+1][row] == player and board[userchoice+2][row] == player:
            win()
    if userchoice>=2 and userchoice<=5 and board[userchoice-2][row] == player and board[userchoice-1][row] == player and board[userchoice+1][row] == player:
            win()
    if userchoice>=3 and board[userchoice-3][row] == player and board[userchoice-2][row] == player and board[userchoice-1][row] == player:
            win()
    if userchoice<=3 and row<=2 and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
            win()
    if userchoice>=1 and row>=1 and userchoice<=4 and row<=3 and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player:
            win()
    if userchoice>=2 and row>=2 and userchoice<=5 and row<=4 and board[userchoice-2][row-2] == player and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player:
            win()
    if userchoice>=3 and row>=3 and board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
            win()
    if userchoice<=3 and row>=3 and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
            win()
    if userchoice>=1 and row>=2 and userchoice<=4 and row<=4 and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player:
            win()
    if userchoice>=2 and row>=1 and userchoice<=5 and row<=3 and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player:
            win()
    if userchoice>=3 and row<=2 and board[userchoice-3][row+3] == player and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player:
            win()
    elif turns>=42:
        ties+=1
        print_board()
        print()
        print("TIE!")
        print()
        print(p1name + ": " + str(p1wins) + " wins")
        print(p2name + ": " + str(p2wins) + " wins")
        print("Ties: " + str(ties))
        print()
        play_again()
    
def print_board():
    print(" ___________________________ ")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][5] + " | " + board[1][5] + " | " + board[2][5] + " | " + board[3][5] + " | " + board[4][5] + " | " + board[5][5] + " | " + board[6][5] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][4] + " | " + board[1][4] + " | " + board[2][4] + " | " + board[3][4] + " | " + board[4][4] + " | " + board[5][4] + " | " + board[6][4] + " |")
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][3] + " | " + board[1][3] + " | " + board[2][3] + " | " + board[3][3] + " | " + board[4][3] + " | " + board[5][3] + " | " + board[6][3] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][2] + " | " + board[1][2] + " | " + board[2][2] + " | " + board[3][2] + " | " + board[4][2] + " | " + board[5][2] + " | " + board[6][2] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][1] + " | " + board[1][1] + " | " + board[2][1] + " | " + board[3][1] + " | " + board[4][1] + " | " + board[5][1] + " | " + board[6][1] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + board[0][0] + " | " + board[1][0] + " | " + board[2][0] + " | " + board[3][0] + " | " + board[4][0] + " | " + board[5][0] + " | " + board[6][0] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("  1   2   3   4   5   6   7  ")
    
def user_turn(player):
    global turns, ties
    userchoice = str(input("Choose a column (1-7): "))
    while userchoice != "1" and userchoice != "2" and userchoice != "3" and userchoice != "4" and userchoice != "5" and userchoice != "6" and userchoice != "7":
        print("You must input a whole number between 1 and 7...")
        userchoice = str(input("Choose a column (1-7): "))
    userchoice = int(userchoice)-1
    
    for x in range(0, 6):
        if board[userchoice][x] == " ":
            row = x
            board[userchoice][x] = player
            turns+=1
            break
        else:
            if x>=5:
                print("You cannot go in this column.")
                row = False
                user_turn(player)
            else:
                x+=1

    def win():
        global p1wins, p2wins, ties
        print_board()
        print()
        if player == p1char:
            p1wins+=1
            print(p1name.upper() + " WINS!")
        elif player == p2char:
            p2wins+=1
            print(p2name.upper() + " WINS!")
        print()
        print(p1name + ": " + str(p1wins) + " wins")
        print(p2name + ": " + str(p2wins) + " wins")
        print("Ties: " + str(ties))
        print()
        play_again()
         
    if row>=3 and board[userchoice][row-3] == player and board[userchoice][row-2] == player and board[userchoice][row-1] == player:
            win()
    if userchoice<=3 and board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
            win()
    if userchoice>=1 and userchoice<=4 and board[userchoice-1][row] == player and board[userchoice+1][row] == player and board[userchoice+2][row] == player:
            win()
    if userchoice>=2 and userchoice<=5 and board[userchoice-2][row] == player and board[userchoice-1][row] == player and board[userchoice+1][row] == player:
            win()
    if userchoice>=3 and board[userchoice-3][row] == player and board[userchoice-2][row] == player and board[userchoice-1][row] == player:
            win()
    if userchoice<=3 and row<=2 and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
            win()
    if userchoice>=1 and row>=1 and userchoice<=4 and row<=3 and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player:
            win()
    if userchoice>=2 and row>=2 and userchoice<=5 and row<=4 and board[userchoice-2][row-2] == player and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player:
            win()
    if userchoice>=3 and row>=3 and board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
            win()
    if userchoice<=3 and row>=3 and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
            win()
    if userchoice>=1 and row>=2 and userchoice<=4 and row<=4 and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player:
            win()
    if userchoice>=2 and row>=1 and userchoice<=5 and row<=3 and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player:
            win()
    if userchoice>=3 and row<=2 and board[userchoice-3][row+3] == player and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player:
            win()
    elif turns>=42:
        ties+=1
        print_board()
        print()
        print("TIE!")
        print()
        print(p1name + ": " + str(p1wins) + " wins")
        print(p2name + ": " + str(p2wins) + " wins")
        print("Ties: " + str(ties))
        print()
        play_again()
        
def play_again():
    playagain = str(input("Would you like to play again? "))
    if  playagain.lower() == "yes" or playagain.lower() == "y":
        global board, turns
        board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        turns = 0
        game()
    elif playagain.lower() == "no" or playagain.lower() == "n":
        quit()
    elif playagain.lower() == "settings" or playagain.lower() == "s" or playagain.lower() == "configure" or playagain.lower() == "config" or playagain.lower() == "c":
        settings()
    else:
        print("Sorry, I couldn't understand you. Please respond with \"yes\" or \"no\".")
        play_again()
        
def game():
    while True:
        print_board()
        print()
        print(p1name)
        user_turn(p1char)
        print()
        print_board()
        print()
        print(p2name)
        user_turn(p2char)
    print()

config = str(input("Would you like to CONFIGURE the settings, or use the DEFAULT settings? "))
while config.lower() != "default" and config.lower() != "d" and config.lower() != "configure" and config.lower() != "c" and config.lower() != "config":
    print("Sorry, I didn't understand that. Please respond with \"configure\" or \"default\".")
    config = str(input("Would you like to CONFIGURE the settings, or use the DEFAULT settings? "))
if config.lower() == "configure" or config.lower() == "c" or config.lower() == "config":
    settings()
elif config.lower() == "default" or config.lower() == "d":
    game()
