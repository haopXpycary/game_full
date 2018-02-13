import os
import random
import copy
import threading
import time

from Const_H__ import *
from tools import *

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
        while self.exp >= levelUp(self.level):
            self.level += 1
            self.health = fofi(levelAdd*self.health)
            self.maxHealth = fofi(levelAdd*self.maxHealth)
            self.protect = fofi(levelAdd*self.protect)
            self.hitHealth = fofi(levelAdd*self.hitHealth)


class AFire(threading.Thread):
    def __init__(self,x,y,headfor):
        super().__init__(self)
        
        self.fireX   = x
        self.fireY   = y
        self.headfor = headfor
        self.hitWall = False
        
    def run(self):
        headfor = self.headfor
        while not self.hitWall:
            if headfor == Right:
                if self.fireX < MaxScrX:
                    self.firerX += 1
                else:
                    self.hitWall = True
            if headfor == Left:
                if self.fireX > 0:
                    self.fireX -= 1
                else:
                    self.hitWall = True
            if headfor == Down:
                if self.fireY < MaxScrY:
                    self.fireY += 1
                else:
                    self.hitWall = True
            if headfor == Up:
                if self.fireY > 0:
                    self.fireY -= 1
                else:
                    self.hitWall = True
            time.sleep(0.2)
            print(vars(self))

class Adder:
    def __init__(self,kind):
        self.x    = random.randint(1,MaxScrX)
        self.y    = random.randint(1,MaxScrX)
        self.kind = kind

class scrControl:
    def __init__(self):
        self.scr = []
        self.initscr(MaxScrX,MaxScrY)
        self.lastscr = cp(self.scr)
    
    def initscr(self,x,y):
        self.x = x
        self.y = y
        for i in range(y):
            self.scr.append([])
            for j in range(x):
                self.scr[i].append(' ')
            
    def update(self,x,y,ch):
        for i,j in zip(list(ch),range(len(ch))):
            if x+j < self.x and y < self.y:
                self.scr[y][x+j] = i
    
    def show(self):
        for i in range(self.y):
            for j in range(self.x):
                print("\033[%d;%dH%s" %(i+1,j+1,self.scr[i][j]))
   
    def updateShow(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.scr[i][j] != self.lastscr[i][j]:
                    print("\033[%d;%dH%s" %(i+1,j+1,self.scr[i][j]))
        self.lastscr = cp(self.scr)
   
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