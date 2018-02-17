import time

from before import *
from player import *
from Const_H__ import *
from myDict import *
from playMode import *
	
sumL = 1

showXY = 0
showFireNumber = 0

while True:
    ch = get.ch
    get.ch = 0
    
    if not per.isAlive and playerDeath: 
        print("\033[5;5Hyou died...")
        break;
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
        fireL.append(AFire(per.playerX,per.playerY,per.headfor,per.hitHealth))
        fireL[-1].start()
        time.sleep(0.1)
    elif ch == DEBUG:
        time.sleep(1)
        debugMode = True
    elif ch == ADDEXP:
        per.addExp(10**10)
        
    #--make adder----------------------------------------------
    for i in adderL:
        if i.kind == healthAdder:
            alldict[(i.adderX,i.adderY)] = HEALTH+"+"
        if i.kind == expAdder:
            alldict[(i.adderX,i.adderY)] = EXP+"*"
        if i.kind == moneyAdder:
            alldict[(i.adderX,i.adderY)] = MONEY+"$"
        
    #--player headfor----------------------------------------------
    if per.headfor == Right:
        perch = ">"
    elif per.headfor == Left:
        perch = "<"
    elif per.headfor == Up:
        perch = "^"
    elif per.headfor == Down:
        perch = "v"
    if hidePlayer:
        perch = FULLSCRCHAR
    alldict[(per.playerX,per.playerY)] = PLAYER+perch
    
    #--fire----------------------------------------------
    for i in fireL:
        if i.hitWall or i.stop:
            del fireL[fireL.index(i)]
            if showFireNumber:
                print("\033[1;0H",len(fireL))
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
    if sumL % 12 == 0 and randFire:
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
        elif j[0] == MONEY:
            mdict.append(i)
        elif j[0] == EXP:
            edict.append(i)
        elif j[0] == AFIRE:
            fdict.append(i)
    
    for i in edict:
        for j in pdict:
            if i == j:
                per.addExp(10)
                del adderL[adderL.index([x for x in adderL if x.kind == expAdder][edict.index(i)])]
                adderL.append(Adder(expAdder))
    for i in hdict:
        for j in pdict:
            if i == j:
                per.healthChange(10)
                del adderL[adderL.index([x for x in adderL if x.kind == healthAdder][hdict.index(i)])]
                adderL.append(Adder(healthAdder))
    for i in fdict:
        for j in pdict:
            if i == j:
                per.healthChange(-fireL[fdict.index(i)].hitHealth)
                fireL[fdict.index(i)].stop = True
    for i in mdict:
        for j in pdict:
            if i == j:
                per.money += 300
                del adderL[adderL.index([x for x in adderL if x.kind == moneyAdder][mdict.index(i)])]
                adderL.append(Adder(moneyAdder))
                
    #--updateScr-----------------------------------------
    for i,j in zip(alldict.keys(),alldict.values()):
        if j[0] == PLAYER:
            scr.update(i[0],i[1],j[1:],RED)
            continue
        elif j[0] == EXP:
            scr.update(i[0],i[1],j[1:],GREEN)
            continue
        elif j[0] == MONEY:
            scr.update(i[0],i[1],j[1:],YELLOW)
            continue
        scr.update(i[0],i[1],j[1:])
    scr.updateShow()
    
    #--back----------------------------------------------
    for i,j in zip(alldict.keys(),alldict.values()):
        scr.update(i[0],i[1],FULLSCRCHAR*(len(j)-1))
    
    #--clear----------------------------------------------
    alldict.clear()
    pdict = list()
    fdict = list()
    hdict = list()
    edict = list()
    mdict = list()
    
    #--show message----------------------------------------------
    print("\033[15;5H","level:%5d HP:%5d exp:%5d" %(per.level,per.health,per.exp))
    print("\033[1;33H","$%d" %per.money)
    if showXY:
        print("\033[15;30H","X:{} Y:{}".format(per.playerX,per.playerY))
    time.sleep(0.02)

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
exit()
