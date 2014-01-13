#Palmer Paul, 2014

#very crude pendulum...note, this is not a realistic representation
#I just used the equation of a semi-circle for the movement
#For some reason, the radius of the semi circle seems to shrink (it looks parabolic)
#At the beginning, the zoom is "messed up"

from visual import * #imports all functions from the visual module

scene = display(title="Pendulum", background = color.white)
scene.select()

x = str(input("What should the starting position of the bob be? "))
while str.isdigit(x) == False:
    print("You must input an integer.")
    x = str(input("What should the starting position of the bob be? "))
x = int(x)
xmax = x
x = -x

strlen = str(input("What should the length of the string be? "))
while str.isdigit(strlen) == False:
    print("You must input an integer.")
    strlen = str(input("What should the length of the string be? "))
strlen = int(strlen)

y = -(strlen-x**2)**1/2
location = vector(x, y, 0)
bob = cylinder(pos=location, radius = 1.5, axis = (0, 0, 0.25), color = color.red, make_trail = True, trsil_type="points", interval = 5, retain = 10)
string = cylinder(pos=(0, 0, .125), radius = .05, axis = location, color = color.white)
bob.trail_object.color=color.cyan

while True:
    rate(30) #important line to dictate the fps. necessary when making an object move
    if x<=xmax:
        y = -(strlen-x**2)**1/2
        bob.pos = (x, y, 0)
        string.axis = (x, y, 0)
        x += .1
    if x>xmax:
        while x>=-xmax:
            rate(30) #important line to dictate the fps. necessary when making an object move
            y = -(strlen-x**2)**1/2
            bob.pos = (x, y, 0)
            string.axis = (x, y, 0)
            x -= .1

