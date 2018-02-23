import socket,threading
from time import sleep
from os import system
import beforeI

IPAddress = "127.0.0.1"
PORT = 5466

class socketListen(threading.Thread):
    def __init__(self):
        super().__init__(self)
        
        self.sock = socket.socket() 
        try:
            self.sock.connect((IPAddress,PORT))
        except:
            try:
                self.sock.connect((IPAddress,PORT))
                PORT += 1
            except:
                print("\033[0H","Please Make Sure You Had Made Port Opened.")
                exit(1)
        self.lastch = 0
        #print(self.sock)
   
    def run(self):
        while 1:
            try:
                self.sock.sendall("hello".encode())
                self.ch = self.sock.recv(4096).decode()
                sleep(0.2)
                #draw(self.ch,self.lastch)
            finally:
                self.sock = socket.socket() 
                try:
                    self.sock.connect((IPAddress,PORT))
                except:
                    print("\033[0H","Broken Pipe.")
                    exit(1)
    def send(self,st):
        pass
if __name__=="__main__":
    sl = socketListen()
    sl.start()