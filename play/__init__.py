import time

from before import *
from player import *
from Const_H__ import *

sumL = 1
color = WHITE
while True:
    ch = get.ch
    get.ch = 0
    
    if ch == UP:
        per.walk(Up)
    elif ch == DOWN:
        per.walk(Down)
    elif ch == LEFT:
        per.walk(Right)
    elif ch == RIGHT:
        per.walk(Left)
    elif ch == FIRE:
        fireL.append(AFire(per.playerX,per.playerY,per.headfor))
        fireL[-1].start()
        time.sleep(0.1)
        #fireL[-1].join()
        
    for i in adderL:
        if i.kind == healthAdder:
            alldict[(i.adderX,i.adderY)] = "+"
        if i.kind == expAdder:
            alldict[(i.adderX,i.adderY)] = "*"
    
    if per.headfor == Right:
        perch = ">"
    elif per.headfor == Left:
        perch = "<"
    elif per.headfor == Up:
        perch = "^"
    elif per.headfor == Down:
        perch = "v"
    alldict[(per.playerX,per.playerY)] = "p"+perch
    
    for i in fireL:
        if i.hitWall or i.stop:
            del i
            continue
        if i.headfor == Right:
            firech = ">"
        elif i.headfor == Left:
            firech = "<"
        elif i.headfor == Up:
            firech = "^"
        elif i.headfor == Down:
            firech = "v"
        alldict[(i.fireX,i.fireY)] = firech
    
    sumL+=1
    if sumL % 12 == 0:
        fireL.append(AFire(random.randint(1,MaxScrX),
        	                  random.randint(1,MaxScrY),
        	                  random.randint(1,4)))
        fireL[-1].start()
    
    
    for i,j in zip(alldict.keys(),alldict.values()):
        if j[0] == "p":
            scr.update(i[0],i[1],j[1:],RED)
            continue
        scr.update(i[0],i[1],j)
    scr.updateShow()
    for i,j in zip(alldict.keys(),alldict.values()):
        scr.update(i[0],i[1]," "*len(j))
    alldict.clear()
    print("\033[15;5H","level:{} HP:{} exp:{}".format(per.level,per.health,per.exp))
    time.sleep(0.02)
    
termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
