import sys
import os
import termios
import tty
import time

from player import *
from Const_H__ import *
#print(input())

#立即响应
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
getch = sys.stdin.read

#隐藏光标
print("\033[?25l",end="")


per = player(0,0)
adderL  = []
for i in range(MaxHealthAdder):
    adderL.append(Adder(healthAdder))
for i in range(MaxExpAdder):
    adderL.append(Adder(expAdder))
scr = scrControl()
scr.show()
perch = "->"

while True:
    #time.sleep(0.02)
    ch = getch(1)
    print("\b"*MaxScrX,end="")
    
    if ch == UP:
        per.walk(Up)
    elif ch == DOWN:
        per.walk(Down)
    elif ch == LEFT:
        per.walk(Right)
    elif ch == RIGHT:
        per.walk(Left)
    
    if per.headfor == Right:
        perch = "->"
    elif per.headfor == Left:
        perch = "<-"
        
    scr.update(per.playerX,per.playerY,perch)
    scr.updateShow()
    scr.update(per.playerX,per.playerY,"  ")

termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
