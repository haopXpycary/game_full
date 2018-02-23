import os
import random
import copy
import threading
import time

from Const_H__ import *
from tools import *
from playMode import *
	
cp = copy.deepcopy
Test = 0

class player:
    def __init__(self,x,y):
        self.playerX   = x
        self.playerY   = y
        self.headfor   = Right
        
        self.health    = 20
        self.maxHealth = 20
        self.protect   = 1
        self.isAlive   = True
        self.hitHealth = 4
        
        self.exp       = 0
        self.level     = 1
        self.money     = 100
        
        self.magic     = 100
        self.maxMagic  = 100
        
        self.perch = ">"
        
    def move(self,x,y):
        self.playerX   = x
        self.playerY   = y

    def walk(self,headfor):
        if headfor == self.headfor:
            if headfor == Right:
                if self.playerX < MaxScrX:
                    self.playerX += 1
            
            if headfor == Left:
                if self.playerX > 0:
                    self.playerX -= 1
         
            if headfor == Down:
                if self.playerY < MaxScrY:
                    self.playerY += 1
         
            if headfor == Up:
                if self.playerY > 0:
                    self.playerY -= 1
        
        else:
            self.headfor = headfor
        
        if self.headfor == Right:
            self.perch = ">"
        elif self.headfor == Left:
            self.perch = "<"
        elif self.headfor == Up:
            self.perch = "^"
        elif self.headfor == Down:
            self.perch = "v"
        if hidePlayer:
            self.perch = FULLSCRCHAR
        
    def healthChange(self,health):
        if health < 0:
            if health + self.protect < 0:
                self.health += health
        else:
            self.health += health
        
        if self.health <= 0:
            self.health = 0
            self.isAlive = False
        if self.health >= self.maxHealth:
            self.health = self.maxHealth
            
    def addExp(self,exp):
        self.exp += exp
        if self.exp >= levelUp(self.level):
            self.exp = 0
            self.level += 1
            self.maxHealth = fofi(levelAdd*self.maxHealth)
            self.protect = fofi(levelAdd*self.protect)
            self.hitHealth = fofi(levelAdd*self.hitHealth)
            self.maxMagic = fofi(levelAdd*self.maxMagic)
    
    def decMp(self,mp):
        if self.magic >= mp:
            self.magic -= mp
            return True
        else:
            return False
    
    def tp(self):
        if self.decMp(20):
            for i in range(6):
                self.walk(self.headfor)
            
class AFire(threading.Thread):
    def __init__(self,x,y,headfor,hitHealth=3):
        super().__init__(self)
        
        if 0 <= x <= MaxScrX:
            self.fireX   = x
        else:
            self.fireX = 0
        if 0 <= y <= MaxScrY:
            self.fireY   = y
        else:
            self.fireY = 0
        self.headfor = headfor
        self.hitHealth = hitHealth
        self.hitWall = False
        self.stop    = False
        
        self.firech = ">"
        if self.headfor == Right:
            self.firech = ">"
        elif self.headfor == Left:
            self.firech = "<"
        elif self.headfor == Up:
            self.firech = "^"
        elif self.headfor == Down:
            self.firech = "v"
            
    def run(self):
        headfor = self.headfor
        if fireFast: SPEED = 0.02
        else:        SPEED = 0.2
        while not self.hitWall:
            if self.stop:break;
            
            if headfor == Right:
                if self.fireX < MaxScrX:
                    self.fireX += 1
                else:
                    self.hitWall = True
            elif headfor == Left:
                if self.fireX > 0:
                    self.fireX -= 1
                else:
                    self.hitWall = True
            elif headfor == Down:
                if self.fireY < MaxScrY:
                    self.fireY += 1
                else:
                    self.hitWall = True
            elif headfor == Up:
                if self.fireY > 0:
                    self.fireY -= 1
                else:
                    self.hitWall = True
            
            
            time.sleep(SPEED)
            #print(vars(self))

class Adder:
    def __init__(self,kind):
        self.adderX    = random.randint(1,MaxScrX-1)
        self.adderY    = random.randint(1,MaxScrY-1)
        self.kind = kind

class scrControl:
    def __init__(self):
        self.scr = []
        self.initscr(MaxScrX,MaxScrY)
        self.lastscr = cp(self.scr)
        self.colordict = dict()
        
    def initscr(self,x,y):
        self.x = x
        self.y = y
        for i in range(y):
            self.scr.append([])
            for j in range(x):
                self.scr[i].append(FULLSCRCHAR)
            
    def update(self,x,y,ch,color=WHITE):
        for i,j in zip(list(ch),range(len(ch))):
            if x+j+1 < self.x and y+1 < self.y:
                self.scr[y][x+j] = i
                self.colordict[(y,x+j)] = color
    
    def show(self):
        for i in range(self.y):
            for j in range(self.x):
                print("\033[%d;%dH%s" %(i+1,j+1,self.scr[i][j]))
    
    def updateShow(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.scr[i][j] != self.lastscr[i][j]:
                    try:
                        print(self.colordict[i,j])
                    except:
                        print(WHITE)
                    print("\033[%d;%dH%s" %(i+1,j+1,self.scr[i][j]))
                    print("\033[0m")
        self.lastscr = cp(self.scr)

class KeyboardListen(threading.Thread):
    def __init__(self,fun):
        super().__init__(self)
        
        self.ch   = False
        self.fun  = fun
    def run(self):
        while True:
            self.ch = self.fun(1)
        
if Test:
    p = player(0,0)
    print(vars(p))
    p.walk(Right)
    print(vars(p))
    p.walk(Left)
    print(vars(p))
    p.healthChange(40)
    print(vars(p))
    p.addExp(1000)
    print(vars(p))
    
    s = AFire(1,1,Left)
    s.start()
    s.join()
    
    A = scrControl()
    A.show()
    A.update(3,2,"hello")
    A.update(9,4,"hello")
    A.update(4,9,"hello")
    A.updateShow()