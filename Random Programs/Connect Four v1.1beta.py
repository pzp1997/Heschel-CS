#Connect Four by Palmer Paul, 2014

##bugs
#playagain>no: Uses quit(), which "gets the job done", but makes a message pop up

##features to add
#switch between who goes first
#add a basic computer (chooses a random column)
#print the "winning four in a row"
#put a limit on the length of the names (13 characters?)

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

def settings(p1name, p1char, p2name, p2char):
    print()
    print("Player 1")
    p1name = str(input("What is your name? "))
    while p1name == " " or p1name == "":
        print("That is not a valid name. Your name must contain at least one character (spaces don't count as a character).")
        p1name = str(input("What is your name? "))
    p1char = str(input("Choose one character to \"represent you\" on the board: "))
    while len(p1char) != 1 or p1char == " ":
        if len(p1char) != 1:
            print("You must input a single character!")
            p1char = str(input("Choose one character to \"represent you\" on the board: "))
        elif p1char == " ":
            print("Your character cannot be a space!")
            p1char = str(input("Choose one character to \"represent you\" on the board: "))
        else:
            break
    print()
    print("Player 2")
    p2name = str(input("What is your name? "))
    while p2name.lower() == p1name.lower() or p2name == " " or p2name == "":
        if p2name.lower() == p1name.lower():
            print("Please choose a different name than " + p1name)
        else:
            print("That is not a valid name. Your name must contain at least one character (spaces don't count as a character).")
        p2name = str(input("What is your name? "))
    p2char = str(input("Choose one character to \"represent you\" on the board: "))
    while len(p2char) != 1 or p2char == " " or p2char == p1char:
        if len(p2char) != 1:
            print("You must input a single character!")
            p2char = str(input("Choose one character to \"represent you\" on the board: "))            
        elif p2char == " ":
            print("Your character cannot be a space!")
            p2char = str(input("Choose one character to \"represent you\" on the board: "))
        elif p2char == p1char:
            print("You can't choose the same character as " + p1name + "!")
            p2char = str(input("Choose one character to \"represent you\" on the board: "))
        else:
            break
    game()
    
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
    
def user_turn(player, turns, ties):
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
                user_turn(player, turns, ties)
            else:
                x+=1

    def win(p1wins, p2wins, ties):
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
        play_again(board, turns)
         
    if row>=3 and board[userchoice][row-3] == player and board[userchoice][row-2] == player and board[userchoice][row-1] == player:
        win(p1wins, p2wins, ties)
    if userchoice<=3 and board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=1 and userchoice<=4 and board[userchoice-1][row] == player and board[userchoice+1][row] == player and board[userchoice+2][row] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=2 and userchoice<=5 and board[userchoice-2][row] == player and board[userchoice-1][row] == player and board[userchoice+1][row] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=3 and board[userchoice-3][row] == player and board[userchoice-2][row] == player and board[userchoice-1][row] == player:
        win(p1wins, p2wins, ties)
    if userchoice<=3 and row<=2 and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=1 and row>=1 and userchoice<=4 and row<=3 and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=2 and row>=2 and userchoice<=5 and row<=4 and board[userchoice-2][row-2] == player and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=3 and row>=3 and board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
        win(p1wins, p2wins, ties)
    if userchoice<=3 and row>=3 and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=1 and row>=2 and userchoice<=4 and row<=4 and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=2 and row>=1 and userchoice<=5 and row<=3 and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player:
        win(p1wins, p2wins, ties)
    if userchoice>=3 and row<=2 and board[userchoice-3][row+3] == player and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player:
        win(p1wins, p2wins, ties)
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
        play_again(board, turns)
        
def play_again(board, turns):
    board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
    turns = 0
    playagain = str(input("Would you like to play again (type \"settings\" to reconfigure the settings)? "))
    if  playagain.lower() == "yes" or playagain.lower() == "y":
        game()
    elif playagain.lower() == "no" or playagain.lower() == "n":
        quit()
    elif playagain.lower() == "settings" or playagain.lower() == "s" or playagain.lower() == "configure" or playagain.lower() == "config" or playagain.lower() == "c":
        settings(p1name, p1char, p2name, p2char)
    else:
        print("Sorry, I couldn't understand you. Please respond with \"yes\", \"no\", or \"settings\".")
        play_again(board, turns)
        
def game():
    while True:
        print_board()
        print()
        print(p1name)
        user_turn(p1char, turns, ties)
        print()
        print_board()
        print()
        print(p2name)
        user_turn(p2char, turns, ties)
    print()

config = str(input("Would you like to CONFIGURE the settings, or use the DEFAULT settings? "))
while config.lower() != "default" and config.lower() != "d" and config.lower() != "configure" and config.lower() != "c" and config.lower() != "config":
    print("Sorry, I didn't understand that. Please respond with \"configure\" or \"default\".")
    config = str(input("Would you like to CONFIGURE the settings, or use the DEFAULT settings? "))
if config.lower() == "configure" or config.lower() == "c" or config.lower() == "config":
    settings(p1name, p1char, p2name, p2char)
elif config.lower() == "default" or config.lower() == "d":
    game()
