from random import randint

age = randint(0, 120)

def game():
    guess = str(input("Guess how old Bill is: "))
    while guess.isdigit() == False:
        print("Your guess must be a counting number.")
        guess = str(input("Guess how old Bill is: "))
    guess = int(guess)
    if guess>120:
        print("Bill is younger than 120 years old.")
        game()
    if guess>age:
        print("Bill isn't that old!")
        game()
    elif guess<age:
        print("Bill is older than that!")
        game()
    elif guess == age:
        print("You win!")
        playagain()

def playagain():
    global age
    print()
    pa = str(input("Would you like to play again? "))
    while pa != "yes" and pa != "y" and pa != "no" and pa != "n":
        print("Please input \"yes\" or \"no\".")
        pa = str(input("Would you like to play again? "))
    if pa == "yes" or pa == "y":
        age = randint(0, 120)
        print()
        game()
    elif pa == "no" or pa == "n":
        pass

game()
