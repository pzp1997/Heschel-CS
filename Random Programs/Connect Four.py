#Connect Four by Palmer Paul, 2014

print("Welcome to Connect Four")
print()

board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
four_in_row = False
p1char = "X"
p2char = "O"

def settings():
    config = str(input("Would you like to CONFIGURE the settings, or use the DEFAULT settings? "))
    if config.lower() == "configure" or config.lower() == "c":
        global p1char, p2char
        print()
        print("Player 1")
        p1char = str(input("Choose one character to \"represent you\" on the board: "))
        while len(p1char) != 1 or p1char == " ":
            if len(p1char) != 1:
                print("You must input a single character!")
                p1char = str(input("Choose one character to \"represent you\" on the board: "))            
            elif p1char == " ":
                print("Your character cannot be a space!")
                p1char = str(input("Choose one character to \"represent you\" on the board: "))
            else:
                pass
        print()
        print("Player 2")
        p2char = str(input("Choose one character to \"represent you\" on the board: "))
        while len(p2char) != 1 or p2char == " " or p2char == p1char:
            if len(p2char) != 1:
                print("You must input a single character!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))            
            elif p2char == " ":
                print("Your character cannot be a space!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))
            elif p2char == p1char:
                print("You can't choose the same character as Player 1!")
                p2char = str(input("Choose one character to \"represent you\" on the board: "))
            else:
                pass
    if config.lower() == "default" or config.lower() == "d":
        pass
    else:
        print("Sorry, I didn't understand that. Please respond with \"configure\" or \"default\".")
        settings()
    
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
    userchoice = str(input("Choose a column (1-7): "))
    while userchoice != "1" and userchoice != "2" and userchoice != "3" and userchoice != "4" and userchoice != "5" and userchoice != "6" and userchoice != "7":
        print("You must input a whole number between 1 and 7...")
        userchoice = str(input("Choose a column (1-7): "))
    userchoice = int(userchoice)-1
    
    for x in range(0, 6):
        if board[userchoice][x] == " ":
            row = x
            board[userchoice][x] = player
            break
        else:
            if x>=5:
                print("You cannot go in this column.")
                user_turn(player)
            else:
                x+=1

    def win():
        print_board()
        print()
        if player == p1char:
            print("PLAYER 1 WINS!")
        if player == p2char:
            print("PLAYER 2 WINS!")
        global four_in_row
        four_in_row = True
                
    if row<=2:
        if board[userchoice][row+1] == player and board[userchoice][row+2] == player and board[userchoice][row+3] == player:
            win()
    ##########
        if board[userchoice][row-1] == player and board[userchoice][row+1] == player and board[userchoice][row+2] == player:
            win()
    ##########
        if board[userchoice][row-2] == player and board[userchoice][row-1] == player and board[userchoice][row+1] == player:
            win()
    if row>=3:
        if board[userchoice][row-3] == player and board[userchoice][row-2] == player and board[userchoice][row-1] == player:
            win()
    if userchoice<=3:
        if board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
            win()
    ##########
        if board[userchoice-1][row] == player and board[userchoice+1][row] == player and board[userchoice+2][row] == player:
            win()
    ##########
        if board[userchoice-2][row] == player and board[userchoice-1][row] == player and board[userchoice+1][row] == player:
            win()
    if userchoice>=3:
        if board[userchoice-3][row] == player and board[userchoice-2][row] == player and board[userchoice-1][row] == player:
            win()
    if userchoice<=3 and row<=2:
        if board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
            win()
    ##########
        if board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player:
            win()
    ##########
        if board[userchoice-2][row-2] == player and board[userchoice-1][row-1] == player and board[userchoice+1][row+1] == player:
            win()
    if userchoice>=3 and row>=3:
        if board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
            win()
    if userchoice<=3 and row>=3:  
        if board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
            win()
    ##########
        if board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player:
            win()
    ##########
        if board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player and board[userchoice+1][row-1] == player:
            win()
    if userchoice>=3 and row<=2:
        if board[userchoice-3][row+3] == player and board[userchoice-2][row+2] == player and board[userchoice-1][row+1] == player:
            win()
            
def play_again():
    playagain = str(input("Would you like to play again? "))
    if  playagain.lower() == "yes" or playagain.lower() == "y":
        global board, four_in_row
        board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        four_in_row = False
        game()
    if playagain.lower() == "no" or playagain.lower() == "n":
        pass
    else:
        print("Sorry, I couldn't understand you. Please respond with \"yes\" or \"no\".")
        play_again()
        
def game():
    while four_in_row == False:
        print_board()
        print()
        print("Player 1")
        user_turn(p1char)
        if four_in_row == True:
            break
        print()
        print_board()
        print()
        print("Player 2")
        user_turn(p2char)
    play_again()

settings()
game()

