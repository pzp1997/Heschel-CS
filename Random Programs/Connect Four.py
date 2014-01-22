#Connect Four by Palmer Paul, 2014

print("Welcome to Connect Four")

col1 = [" ", " ", " ", " ", " ", " "]
col2 = [" ", " ", " ", " ", " ", " "]
col3 = [" ", " ", " ", " ", " ", " "]
col4 = [" ", " ", " ", " ", " ", " "]
col5 = [" ", " ", " ", " ", " ", " "]
col6 = [" ", " ", " ", " ", " ", " "]
col7 = [" ", " ", " ", " ", " ", " "]
board = [col1, col2, col3, col4, col5, col6, col7]
four_in_row = False

def print_board():
    print(" ___________________________ ")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[5] + " | " + col2[5] + " | " + col3[5] + " | " + col4[5] + " | " + col5[5] + " | " + col6[5] + " | " + col7[5] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[4] + " | " + col2[4] + " | " + col3[4] + " | " + col4[4] + " | " + col5[4] + " | " + col6[4] + " | " + col7[4] + " |")
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[3] + " | " + col2[3] + " | " + col3[3] + " | " + col4[3] + " | " + col5[3] + " | " + col6[3] + " | " + col7[3] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[2] + " | " + col2[2] + " | " + col3[2] + " | " + col4[2] + " | " + col5[2] + " | " + col6[2] + " | " + col7[2] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[1] + " | " + col2[1] + " | " + col3[1] + " | " + col4[1] + " | " + col5[1] + " | " + col6[1] + " | " + col7[1] + " |") 
    print("|___|___|___|___|___|___|___|")
    print("|   |   |   |   |   |   |   |")
    print("| " + col1[0] + " | " + col2[0] + " | " + col3[0] + " | " + col4[0] + " | " + col5[0] + " | " + col6[0] + " | " + col7[0] + " |") 
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
        if player == "X":
            print("PLAYER 1 WINS!")
        if player == "O":
            print("PLAYER 2 WINS!")
        global four_in_row
        four_in_row = True
                
    if row<=2:
        if board[userchoice][row+1] == player and board[userchoice][row+2] == player and board[userchoice][row+3] == player:
            win()
    if row>=3:
        if board[userchoice][row-1] == player and board[userchoice][row-2] == player and board[userchoice][row-3] == player:
            win()
    if userchoice<=3:
        if board[userchoice+1][row] == player and board[userchoice+2][row] == player and board[userchoice+3][row] == player:
            win()
    if userchoice>=3:
        if board[userchoice-1][row] == player and board[userchoice-2][row] == player and board[userchoice-3][row] == player:
            win()
    if userchoice<=3 and row<=2:
        if board[userchoice+1][row+1] == player and board[userchoice+2][row+2] == player and board[userchoice+3][row+3] == player:
            win()
    if userchoice<=3 and row>=3:
        if board[userchoice+1][row-1] == player and board[userchoice+2][row-2] == player and board[userchoice+3][row-3] == player:
            win()
    if userchoice>=3 and row<=2:
        if board[userchoice-1][row+1] == player and board[userchoice-2][row+2] == player and board[userchoice-3][row+3] == player:
            win()
    if userchoice>=3 and row>=3:
        if board[userchoice-1][row-1] == player and board[userchoice-2][row-2] == player and board[userchoice-3][row-3] == player:
            win()

def play_again():
    playagain = str(input("Would you like to play again? "))
    if  playagain.lower() == "yes" or playagain.lower() == "y":
        global col1
        col1 = [" ", " ", " ", " ", " ", " "]
        global col2
        col2 = [" ", " ", " ", " ", " ", " "]
        global col3
        col3 = [" ", " ", " ", " ", " ", " "]
        global col4
        col4 = [" ", " ", " ", " ", " ", " "]
        global col5
        col5 = [" ", " ", " ", " ", " ", " "]
        global col6
        col6 = [" ", " ", " ", " ", " ", " "]
        global col7
        col7 = [" ", " ", " ", " ", " ", " "]
        global board
        board = [col1, col2, col3, col4, col5, col6, col7]
        global four_in_row
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
        user_turn("X")
        if four_in_row == True:
            break
        print()
        print_board()
        print()
        print("Player 2")
        user_turn("O")
    play_again()

game()

