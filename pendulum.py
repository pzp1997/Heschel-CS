#Palmer Paul, 2014

#very crude pendulum...note, this is not a realistic representation
#I just used the equation of a semi-circle for the movement
#I did not add a string
#For some reason, the radius of the semi circle seems to shrink
#At the beginning, the zoom is "messed up"
#I probably should have also used some more variables, but YOLO

from visual import * #imports all functions from the visual module 

x = -5
y = -(25-x**2)**1/2
location = vector(x, y, 0)
bob = cylinder(pos=location, radius = 1.5, axis = (0, 0, 0.25), color = color.red)

while True:
    rate(30) #important line to dictate the fps. necessary when making an object move
    if x<=5:
        y = -(25-x**2)**1/2
        bob.pos = (x, y, 0)
        x += .1
    if x>5:
        while x>=-5:
            rate(30) #important line to dictate the fps. necessary when making an object move
            y = -(25-x**2)**1/2
            bob.pos = (x, y, 0)
            x -= .1

