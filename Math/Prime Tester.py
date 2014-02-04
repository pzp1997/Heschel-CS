#Prime Tester by Palmer Paul, 2013

#Input a number to check if it's prime, composite, or neutral

while True:
    usernum = str(input("Input a number to check if it is prime or composite: "))
    num = 2

    while str.isdigit(usernum) == False:
        print("You must input a positive integer...")
        usernum = str(input("Input a number to check if it is prime or composite: "))
    usernum = int(usernum)

    if usernum == 1:
        print("Neutral")
    if usernum == 2 or usernum == 3:
        print ("Prime")
    else:
        while num<=usernum**1/2:
            if usernum%num == 0:
                print ("Composite")
                break
            elif usernum%num != 0:
                num = num + 1
                if num > usernum**1/2:
                    print ("Prime")
            if usernum == 2:
                print ("Prime")

    
