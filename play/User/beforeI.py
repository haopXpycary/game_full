import threading
import tty
import sys
import termios
import os

sys.path.append(__file__[:__file__.rfind("/",0,__file__.rfind("/"))])
import player

while 1:pass
class KeyboardListen(threading.Thread):
    def __init__(self,fun):
        super().__init__(self)
        
        self.ch   = False
        self.fun  = fun
    def run(self):
        while True:
            self.ch = self.fun(1)

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

#
per2 = player(0,0)
