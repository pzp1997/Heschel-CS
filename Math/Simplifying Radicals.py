rad = input('What is the radical? ') #the radical itself
co = 1
num = 2

indicator = 'no'
stop = 'no'

if rad == 0:
	print'0'
	stop = 'yes'
	
if rad < 0:
	indicator = 'yes'
	rad = rad * -1

while (num**2 <= rad or rad == 1) and stop == 'no': #important part of script, where the fun starts
	if rad == 1:
		break
	while rad%(num**2) == 0:
		rad = rad/(num**2)
		co = co*num
	if num == 2:
		num = num + 1 
	elif num > 2:
		num = num + 2
		
	
if stop == 'no':
	if indicator == 'yes':
		if rad == 1:
			print co, 'i'
		else:
			print co, 'root', rad, 'i'
	else:
		if rad ==1:
			print co
		else:
			print co, 'root', rad
	