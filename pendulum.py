#Palmer Paul, 2014

#very crude pendulum...note, this is not a realistic representation
#I just used the equation of a semi-circle for the movement
#I did not add a string (the physical object, not the variable)
    #added a string!
#For some reason, the radius of the semi circle seems to shrink (it looks parabolic)
#At the beginning, the zoom is "messed up"
#I probably should have also used some more variables, but YOLO

from visual import * #imports all functions from the visual module 

x = -5
strlen = 25
y = -(strlen-x**2)**1/2
location = vector(x, y, 0)
bob = cylinder(pos=location, radius = 1.5, axis = (0, 0, 0.25), color = color.yellow, make_trail = True, trsil_type="points", interval = 5, retain = 10)
string = cylinder(pos=(0, 0, .125), radius = .05, axis = location, color = color.white)
bob.trail_object.color=color.cyan

while True:
    rate(30) #important line to dictate the fps. necessary when making an object move
    if x<=5:
        y = -(strlen-x**2)**1/2
        bob.pos = (x, y, 0)
        string.axis = (x, y, 0)
        x += .1
    if x>5:
        while x>=-5:
            rate(30) #important line to dictate the fps. necessary when making an object move
            y = -(strlen-x**2)**1/2
            bob.pos = (x, y, 0)
            string.axis = (x, y, 0)
            x -= .1

