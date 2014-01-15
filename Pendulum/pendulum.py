#Palmer Paul, January 2014

##bugs
#did not account for acceleration due to gravity (the velocity is constant)
#at the beginning, the zoom is "messed up"
#need to fix starting position
#for some reason, the program will get stuck for certain values of theta
#need to find an alternative to str.isdigit() that will work with decimals

from visual import * #imports all functions from the visual module

##visual window
scene = display(title="Single Pendulum", background = color.white)
scene.select()

##user inputs
theta = str(input("What should the starting position of the bob be (in degrees)? "))
while theta.isdecimal() == False:
    print("You must input an integer.")
    theta = str(input("What should the starting position of the bob be? "))
theta = int(theta)
degtheta = theta
theta = radians(theta)
thetamax = theta

strlen = str(input("What should the length of the string be? "))
while strlen.isdecimal() == False:
    print("You must input an integer.")
    strlen = str(input("What should the length of the string be? "))
strlen = int(strlen)

##establishes vector "location"
x = strlen*cos(theta)
y = strlen*sin(theta)
location = vector(x, y, 0)

##objects
bob = cylinder(pos=location, radius = 1.5, axis = (0, 0, 0.25), color = color.red)
string = cylinder(pos=(0, 0, .125), radius = .05, axis = location, color = color.white)

##animation loop
while True:
    rate(100) #important line to dictate the fps. necessary when making an object move
    if theta<=thetamax:
        x = strlen*cos(theta)
        y = strlen*sin(theta)
        bob.pos = (x, y, 0)
        string.axis = (x, y, 0)
        theta -= .01
    if theta>thetamax:
        while x>-thetamax:
            rate(100) #important line to dictate the fps. necessary when making an object move
            x = strlen*cos(theta)
            y = strlen*sin(theta)
            bob.pos = (x, y, 0)
            string.axis = (x, y, 0)
            theta += .01

