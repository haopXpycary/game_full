import time

from before import *
from player import *
from Const_H__ import *
from myDict import *

sumL = 1

showXY = 0
showHXY = 1
while True:
    ch = get.ch
    get.ch = 0
    
    #--getch----------------------------------------------
    if ch == UP:
        per.walk(Up)
    elif ch == DOWN:
        per.walk(Down)
    elif ch == LEFT:
        per.walk(Left)
    elif ch == RIGHT:
        per.walk(Right)
    elif ch == FIRE:
        fireL.append(AFire(per.playerX,per.playerY,per.headfor))
        fireL[-1].start()
        time.sleep(0.1)
        #fireL[-1].join()
    elif ch == DEBUG:
        time.sleep(1)
        debugMode = True
        
    #--make adder----------------------------------------------
    for i in adderL:
        if i.kind == healthAdder:
            alldict[(i.adderX,i.adderY)] = HEALTH+"+"
        if i.kind == expAdder:
            alldict[(i.adderX,i.adderY)] = EXP+"*"
        
    #--player headfor----------------------------------------------
    if per.headfor == Right:
        perch = ">"
    elif per.headfor == Left:
        perch = "<"
    elif per.headfor == Up:
        perch = "^"
    elif per.headfor == Down:
        perch = "v"
    alldict[(per.playerX,per.playerY)] = PLAYER+perch
    
    #--fire----------------------------------------------
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
        alldict[(i.fireX,i.fireY)] = AFIRE+firech
    
    #--fire randomly----------------------------------------------
    sumL+=1
    if sumL % 12 == 0:
        fireL.append(AFire(random.randint(1,MaxScrX),
        	                  random.randint(1,MaxScrY),
        	                  random.randint(1,4)))
        fireL[-1].start()
    
    #--check----------------------------------------------
    for i,j in zip(alldict.keys(),alldict.values()):
        if j[0] == PLAYER:
            pdict.append(i)
        elif j[0] == HEALTH:
            hdict.append(i)
        elif j[0] == EXP:
            edict.append(i)
        elif j[0] == AFIRE:
            fdict.append(i)
        
    for i in edict:
        for j in pdict:
            if i == j:
                per.addExp(10)
    for i in hdict:
        for j in pdict:
            if i == j:
                per.healthChange(10)
    for i in fdict:
        for j in pdict:
            if i == j:
                per.healthChange(-2)
    
    #--updateScr-----------------------------------------
    for i,j in zip(alldict.keys(),alldict.values()):
        if j[0] == PLAYER:
            scr.update(i[0],i[1],j[1:],RED)
            continue
        elif j[0] == EXP:
            scr.update(i[0],i[1],j[1:],GREEN)
            continue
        scr.update(i[0],i[1],j[1:])
    scr.updateShow()
    
    #--back----------------------------------------------
    for i,j in zip(alldict.keys(),alldict.values()):
        scr.update(i[0],i[1]," "*(len(j)-1))
    
    #--clear----------------------------------------------
    alldict.clear()
    pdict = list()
    fdict = list()
    hdict = list()
    edict = list()
    
    #--show message----------------------------------------------
    print("\033[15;5H","level:{} HP:{} exp:{}".format(per.level,per.health,per.exp))
    if showXY:
        print("\033[15;30H","X:{} Y:{}".format(per.playerX,per.playerY))
    time.sleep(0.02)

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)