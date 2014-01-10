#This is a test program to see how github.com works!

#Written by Palmer Paul, LE DAE 2014

def repeat_print(): #this is a function definition. when I write repeat_print() in the program, the indented code below will run
    x = str(input("Input whatever you want and press enter: ")) #asks user to input a string that will be printed
    y = str(input("Input an integer and press enter: ")) #asks user to input an integer (this will be the amount of times that the string is printed)
    while str.isdigit(y) == False: #checks to make sure if the integer is really an integer
        y = str(input("Input an integer and press enter: ")) #as long as it is not an integer, the program will ask the user for an integer
    y = int(y) #since the str.isdigit() function requires a string, we need to convert the variable that holds the integer, y, into the integer data type
    if y >= 1500: #if the integer is very big (greater than or equal to 1500), the indented code will run
        print("This might take a while...") #prints a message to the output window warning the user that the code can take a long time to run
        large_y() #calls the large_y() function (see below)
    print() #prints a blank line (basically, the same as pressing enter)
    for a in range(y): #in this example, the a is irrlevant. all this does is say that the indented code below should run the inputted integer times
        print(x) #prints the string
    print() #prints a blank line

def large_y(): #another function definition. note that this will only run if the user inputted integer, y, is greater than or equal to 1500
    confirm = str(input("Are you sure you'd like to continue? ")) #this asks the user if they would like to print the string, even though it might take awhile, or input a new string and integer
    if confirm.lower() == "yes" or confirm.lower() == "y": #.lower() converts a string to all lower case (in this case, the string contained in the variable confirm)
        pass #tells the interpreter to contine with the program, which would print the string over 1500 times (whatever integer the user inputted)
    elif confirm.lower() == "no" or confirm.lower() == "n": #same as two lines above
        repeat_print() #calls the funciton repeat_print(). in essence, "starts the program over again" from the top
    else: #if the user inputted anything other than yes, y, no, or n, the indented code will run
        print("Sorry, I couldn't understand you. Please respond with \"yes\" or \"no\" and press enter") #prints to the outpus window that the user must input yes or no. \ before a " allows you to use " " as characters, instead of as indicators of a string (note that \ won't print to the output window)
        large_y() #starts the function large_y() over again

while True: #the indented code below will run forever (or until the user quits the program by closing the output window)
    repeat_print() #calls the function repeat_print(). Basically, this line and the one above it are what causes the program to run
