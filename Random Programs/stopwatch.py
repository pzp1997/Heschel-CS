#Stopwatch by Palmer Paul, 2014

from time import sleep

s = 0
m = 0
h = 0

while True:
    if len(str(s)) == 1:
        strs = "0" + str(s)
    elif len(str(s)) > 1:
        strs = str(s)
    if len(str(m)) == 1:
        strm = "0" + str(m)
    elif len(str(m)) > 1:
        strm = str(m)
    if len(str(h)) == 1:
        strh = "0" + str(h)
    elif len(str(h)) > 1:
        strh = str(h)
        
    print(strh + ":" + strm + ":" + strs)
        
    s+=1
    if s>=60:
        s = 0
        m+=1
        if m>=60:
            m=0
            h+=1

    sleep(1)
