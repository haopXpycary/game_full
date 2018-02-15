import sys
import os
import termios
import tty

from player import *
from Const_H__ import *
from myDict import *
	
#立即响应
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
getch = sys.stdin.read

#隐藏光标
print("\033[?25l",end="")
os.system("clear")

#监听键盘
get = KeyboardListen(getch)
get.start()

#屏幕初始化
scr = scrControl()
scr.show()

#玩家初始化
per = player(0,0)

#tool初始化
adderL  = []
fireL = []
for i in range(MaxHealthAdder):
    adderL.append(Adder(healthAdder))
for i in range(MaxExpAdder):
    adderL.append(Adder(expAdder))

alldict = dict() 
pdict   = list() #player
fdict   = list() #fire
hdict   = list() #healthAdder
edict   = list() #expAdder