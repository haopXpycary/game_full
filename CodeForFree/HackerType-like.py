'''
HackerType-like.py --just press.It will print you want.
'''

FILE = __file__
MaxScrX = 43
MaxScrY = 15

import sys
import os
import termios
import tty
import threading
import time
	
class KeyboardListen(threading.Thread):
    def __init__(self,fun):
        super().__init__(self)
        
        self.ch   = False
        self.fun  = fun
        self.stop = False
    def run(self):
        while not self.stop:
            self.ch = self.fun(1)
            #time.sleep(0.01)
        
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
getch = sys.stdin.read

print("\033[?25l",end="")
os.system("clear")

get = KeyboardListen(getch)
get.start()

fileJinx = open(FILE,"r").readlines()
sumOfX = 0
sumOfY = 1

for i in fileJinx:
    for charIrwinInit in i:
        if sumOfX >= MaxScrX:
            sumOfX = 0
            sumOfY += 1
        if sumOfY > MaxScrY:
            sumOfY = MaxScrY
            print()
        if charIrwinInit != " ":
            sumOfX += 1
            while not get.ch:
                print("\033[%d;%dH" %(sumOfY,sumOfX)+charIrwinInit)
                if get.ch:break
            get.ch = 0
        else:
            sumOfX += 1
            print("\033[%d;%dH" %(sumOfY,sumOfX)+" ")
    sumOfY += 1
    sumOfX = 0