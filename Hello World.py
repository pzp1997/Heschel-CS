#This is a test program to see how github.com works!

def repeat_print():
    x = str(input("Input whatever you want and press enter: "))
    y = str(input("Input an integer and press enter: "))
    while str.isdigit(y) == False:
        y = str(input("Input an integer and press enter: "))
    y = int(y)
    if y >= 1500:
        print("This might take a while...")
        large_y()
    print()
    for a in range(y):
        print(x)
    print()

def large_y():
    confirm = str(input("Are you sure you'd like to continue? "))
    if confirm.lower() == "yes" or confirm.lower() == "y":
        pass
    elif confirm.lower() == "no" or confirm.lower() == "n":
        repeat_print()
    else:
        print("Sorry, I couldn't understand you. Please respond with \"yes\" or \"no\" and press enter")
        large_y()

while True:
    repeat_print()
