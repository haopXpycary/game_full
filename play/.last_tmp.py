import time

from random import randint
from sys import __stdin__,__stdout__
from before import *
from tools import *
from player import *
from Const_H__ import *
from myDict import *
from playMode import *

def skills(filename):
    f = open(__file__[:__file__.rfind("/")]+"/Skill/"+filename+".py","r")
    exec(compile("".join(f.readlines()),"","exec"))

sumL = 1
begin = time.time()

#显示坐标
showXY = 1
#显示屏幕中子弹数量
showFireNumber = 1
#显示实体伤害
showHit = 1
#显示技能伤害
showPlayerHit = 1

#屏幕中随机出现的子弹实体伤害3
#一定几率出现技能
#玩家级别越高，技能伤害越强，敌人实体伤害越弱
while True:
    ch = get.ch
    get.ch = 0
    
    if not per.isAlive and playerDeath: 
        print("\033[5;5Hyou died...")
        break;
    if not per2.isAlive and playerDeath: 
        print("\033[5;5Hyou win...")
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
    elif ch == TP:
        per.tp()
    elif ch == WJQF:
        skills("WJQF")
    elif ch == QPZD:
        skills("QPZD")          
    #--special key---
    elif ch == DEBUG:
        time.sleep(100)
        debugMode = True
    elif ch == ADDEXP:
        per.addExp(1000)
        
    #--randwalk---
    
    if sumL % 10 == 0:
        per2.addExp(1)
    swi = randint(1,4)
    for i in range(randint(1,3)):        
        per2.walk(swi)
        time.sleep(0.02)
    if sumL % 2 == 0:
        fireL.append(AFire(per2.playerX,per2.playerY,per2.headfor,per2.hitHealth))
        fireL[-1].start()

    if randint(1,150) == 1:skills("QPZD")
    #--make adder----------------------------------------------
    for i in adderL:
        if i.kind == healthAdder:
            alldict[(i.adderX,i.adderY)] = HEALTH+"+"
        if i.kind == expAdder:
            alldict[(i.adderX,i.adderY)] = EXP+"*"
        if i.kind == moneyAdder:
            alldict[(i.adderX,i.adderY)] = MONEY+"$"
        
    alldict[(per.playerX,per.playerY)] = PLAYER+per.perch
    
    #--fire----------------------------------------------
    for i in fireL:
        if i.hitWall or i.stop:
            del fireL[fireL.index(i)]
            if showFireNumber:
                print("\033[3;35HF%5d:" %len(fireL))
            continue
        alldict[(i.fireX,i.fireY)] = AFIRE+i.firech
    
    #--fire randomly----------------------------------------------
    sumL+=1
    if sumL % 2 == 0 and randFire:
        fireL.append(AFire(random.randint(1,MaxScrX),
        	                  random.randint(1,MaxScrY),
        	                  random.randint(1,4)))
        fireL[-1].start()
    
    #--check---player-------------------------------------------
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
                per.healthChange(20)
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
                
    alldict[(per2.playerX,per2.playerY)] = ENEMY+per2.perch        
    #--add---player--
    if per.magic < per.maxMagic and sumL % 3==0:
        per.magic+=1
    if per.health < per.maxHealth and sumL % 10==0 and playerWell:
        per.health+=1
    if magicFull:
        per.magic = per.maxMagic
        
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
        elif j[0] == ENEMY:
            scr.update(i[0],i[1],j[1:],BLUE)
            continue
        scr.update(i[0],i[1],j[1:])
    scr.updateShow()
            
    #--twoPlayerMode---
    if twoPlayer:
        send = dict()
        st = scr.scr
        for i in range(len(st)):
            for j in range(len(st[i])):
                if st[i][j]:
                    send[st[i][j]] = (i,j)
        sl.rt = send
        
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
    
    #--show message---player-------------------------------------------
    print("\033[15H","level:%5d HP:%5d MP:%5d exp:%5d" %(per.level,per.health,per.magic,per.exp))
    print("\033[1;35H","$%5d" %per.money)
    if showXY:
        print("\033[14;30H","X:{} Y:{}".format(per.playerX,per.playerY))
    now = time.time()-begin
    print("\033[2;35H%5.2f" %now)
    if showHit:
        print("\033[4;35H%5dA" %(per2.hitHealth-per.protect))
    if showPlayerHit:
        print("\033[5;35H%5dH" %(per.hitHealth-per.protect))
    time.sleep(0.01)

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
__stdin__.flush()
__stdout__.flush()
print("打扫战场中，请摁两下回车…")

scoreTime = time.strftime("%Y/%m/%d %H:%M:%S::")
scoreTime += "%.2f" %(now%1)
writeScore(scoreTime,now,per.level,per.way,per2.way)

get.stop = 1
exit()