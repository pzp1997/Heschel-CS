##visual window
scene = display(title="Single Pendulum", background = color.white)
scene.select()

##user inputs
angle = str(input("What should the starting position of the bob be (in degrees)? "))
while angle.isdecimal() == False:
    print("You must input an integer.")
    angle = str(input("What should the starting position of the bob be? "))
anglemax = radians(int(angle))

strlen = str(input("What should the length of the string be? "))
while strlen.isdecimal() == False:
    print("You must input an integer.")
    strlen = str(input("What should the length of the string be? "))
strlen = int(strlen)

##objects
bob = cylinder(pos=location, radius = 1.5, axis = (0, 0, 0.25), color = color.red)
string = cylinder(pos=(0, 0, .125), radius = .05, axis = location, color = color.white)

##variables
m1 = 5.972000000000000000000000000
m2 = 
r2 = 6371
G = .0000000000667
g = 
x = 0
y = anglemax*sin(((g/strlen)**1/2)*t)
