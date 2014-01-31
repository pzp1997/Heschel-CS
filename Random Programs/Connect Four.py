#Connect Four by Palmer Paul, 2014

##bugs
#used globals
#playagain>no: Uses quit(), which "gets the job done", but makes a message pop up
#p1name/p2name can be multiple spaces
#when one player, the computer doesn't go first

##features to add
#put a limit on the length of the names (13 characters?)
#when one player, player can choose if they want to go first or second in the first game

from random import randint

print("Welcome to Connect Four")
print()

board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
p1char = "X"
p2char = "O"
p1name = "Player 1"
p2name = "Player 2"
p1wins = 0
p2wins = 0
ties = 0
turns = 0
numplayers = 2

def settings():
    global p1name, p1char, p2name, p2char, numplayers
    print()
    numplayers = str(input("TWO players or ONE player: "))
    while numplayers.lower() != "one" and numplayers.lower() != "1" and numplayers.lower() != "o" and numplayers.lower() != "two" and numplayers.lower() != "2" and numplayers.lower() != "t" and numplayers.lower() != "one player" and numplayers.lower() != "two players":
        numplayers = str(input("Please input \"one\" or \"two\": "))
    if numplayers.lower() == "one" or numplayers.lower() == "1" or numplayers.lower() == "o" or numplayers.lower() == "one player":
        numplayers = 1
    elif numplayers.lower() == "two" or numplayers.lower() == "2" or numplayers.lower() == "t" or or numplayers.lower() == "two players":
        numplayers = 2
    print()
    if numplayers == 2:
        print("Player 1")
    p1name = str(input("What is your name? "))
    while p1name == " " or len(p1name) == 0:
        print("That is not a valid name. Your name must contain at least one character (spaces don't count as a character).")
        p1name = str(input("What is your name? "))
    p1char = str(input("Choose one character to \"represent you\" on the board: "))
    while len(p1char) != 1 or p1char == " " or p1char == "-" or p1char == "|" or p1char == "/" or p1char == "\\":
        if len(p1char) != 1:
            print("You must input a single character!")
            p1char = str(input("Choose one character to \"represent you\" on the board: "))
        elif p1char == " ":
            print("Your character cannot be a space!")
            p1char = str(input("Choose one character to \"represent you\" on the board: "))
        elif p1char == "-" or p1char == "|" or p1char == "/" or p1char == "\\":
            print("Sorry, that is not a valid character.")
            p1char = str(input("Choose one character to \"represent you\" on the board: "))
    if numplayers == 2: 
        print()
        print("Player 2")
        p2name = str(input("What is your name? "))
        while p2name.lower() == p1name.lower() or p2name == " " or len(p2name) == 0:
            if p2name.lower() == p1name.lower():
                print("Please choose a different name than " + p1name)
            else:
                print("That is not a valid name. Your name must contain at least one character (spaces don't count as a character).")
            p2name = str(input("What is your name? "))
        p2char = str(input("Choose one character to \"represent you\" on the board: "))
        while len(p2char) != 1 or p2char == " " or p2char == p1char or p2char == "-" or p2char == "|" or p2char == "/" or p2char == "\\":
            if len(p2char) != 1:
                print("You must input a single character!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))            
            elif p2char == " ":
                print("Your character cannot be a space!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))
            elif p2char == p1char:
                print("You can't choose the same character as " + p1name + "!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))
            elif p2char == "-" or p2char == "|" or p2char == "/" or p2char == "\\":
                print("Sorry, that is not a valid character.")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))
    if numplayers == 1:
        p2name = "Computer"
        p2char = str(input("Choose one character to \"represent the computer\" on the board: "))
        while len(p2char) != 1 or p2char == " " or p2char == p1char:
            if len(p2char) != 1:
                print("You must input a single character!")
                p2char = str(input("Choose one character to \"represent the computer\" on the board: "))            
            elif p2char == " ":
                print("The computer's character cannot be a space!")
                p2char = str(input("Choose one character to \"represent the computer\" on the board: "))
            elif p2char == p1char:
                print("You can't make the computer's character the same character as yours!")
                p2char = str(input("Choose one character to \"represent the computer\" on the board: "))
    game(p1wins, p2wins, ties)
    
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
    global turns, ties, numplayers
    if numplayers == 1 and player == p2char:
        userchoice = randint(1, 7)
    else:
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
        board[userchoice][row-3] = "|"
        board[userchoice][row-2] = "|"
        board[userchoice][row-1] = "|"
        board[userchoice][row] = "|"
        win()
    if userchoice<=3 and board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
        board[userchoice][row] = "-"
        board[userchoice+1][row] = "-"
        board[userchoice+2][row] = "-"
        board[userchoice+3][row] = "-"
        win()
    if userchoice>=1 and userchoice<=4 and board[userchoice-1][row] == player and board[userchoice+1][row] == player and board[userchoice+2][row] == player:
        board[userchoice-1][row] = "-"
        board[userchoice][row] = "-"
        board[userchoice+1][row] = "-"
        board[userchoice+2][row] = "-"
        win()
    if userchoice>=2 and userchoice<=5 and board[userchoice-2][row] == player and board[userchoice-1][row] == player and board[userchoice+1][row] == player:
        board[userchoice-2][row] = "-"
        board[userchoice-1][row] = "-"
        board[userchoice][row] = "-"
        board[userchoice+1][row] = "-"
        win()
    if userchoice>=3 and board[userchoice-3][row] == player and board[userchoice-2][row] == player and board[userchoice-1][row] == player:
        board[userchoice-3][row] = "-"
        board[userchoice-2][row] = "-"
        board[userchoice-1][row] = "-"
        board[userchoice][row] = "-"
        win()
    if userchoice<=3 and row<=2 and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
        board[userchoice][row] = "/"
        board[userchoice+1][row+1] = "/" 
        board[userchoice+2][row+2] = "/"
        board[userchoice+3][row+3] = "/"
        win()
    if userchoice>=1 and row>=1 and userchoice<=4 and row<=3 and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player:
        board[userchoice-1][row-1] = "/"
        board[userchoice][row] = "/"
        board[userchoice+1][row+1] = "/"
        board[userchoice+2][row+2] = "/"
        win()
    if userchoice>=2 and row>=2 and userchoice<=5 and row<=4 and board[userchoice-2][row-2] == player and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player:
        board[userchoice-2][row-2] = "/"
        board[userchoice-1][row-1] = "/"
        board[userchoice][row] = "/"
        board[userchoice+1][row+1] = "/"
        win()
    if userchoice>=3 and row>=3 and board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
        board[userchoice][row] = "/"
        board[userchoice-1][row-1] = "/"
        board[userchoice-2][row-2] = "/"
        board[userchoice-3][row-3] = "/"
        win()
    if userchoice<=3 and row>=3 and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
        board[userchoice][row] = "\\"
        board[userchoice+1][row-1] = "\\"
        board[userchoice+2][row-2] = "\\"
        board[userchoice+3][row-3] = "\\"
        win()
    if userchoice>=1 and row>=2 and userchoice<=4 and row<=4 and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player:
        board[userchoice-1][row+1] = "\\"
        board[userchoice][row] = "\\"
        board[userchoice+1][row-1] = "\\"
        board[userchoice+2][row-2] = "\\"
        win()
    if userchoice>=2 and row>=1 and userchoice<=5 and row<=3 and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player:
        board[userchoice-2][row+2] = "\\"
        board[userchoice-1][row+1] = "\\"
        board[userchoice][row] = "\\"
        board[userchoice+1][row-1] = "\\"
        win()
    if userchoice>=3 and row<=2 and board[userchoice-3][row+3] == player and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player:
        board[userchoice-3][row+3] = "\\"
        board[userchoice-2][row+2] = "\\"
        board[userchoice-1][row+1] = "\\"
        board[userchoice][row] = "\\"
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
    playagain = str(input("Would you like to play again (to reconfigure settings, input \"settings\")? "))
    if  playagain.lower() == "yes" or playagain.lower() == "y":
        global board, turns
        board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        turns = 0
        game(p1wins, p2wins, ties)
    elif playagain.lower() == "no" or playagain.lower() == "n":
        quit()
    elif playagain.lower() == "settings" or playagain.lower() == "s" or playagain.lower() == "configure" or playagain.lower() == "config" or playagain.lower() == "c":
        board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        turns = 0
        settings()
    else:
        print("Sorry, I couldn't understand you. Please respond with \"yes\" or \"no\".")
        play_again()
        
def game(p1wins, p2wins, ties):
    global numplayers
    while True:
        print_board()
        print()
        if (p1wins+p2wins+ties)%2 != 0:
            if numplayers == 2:
                print(p2name)
            user_turn(p2char)
        else:
            print(p1name)
            user_turn(p1char)
        if numplayers == 2:   
            print_board()
            print()
        if (p1wins+p2wins+ties)%2 != 0:
            print(p1name)
            user_turn(p1char)
        else:
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
    game(p1wins, p2wins, ties)
