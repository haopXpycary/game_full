import socket,threading
from time import sleep

class socketListen(threading.Thread):
    def __init__(self):
        super().__init__(self)
        
        self.address = ""
        self.port = 5466
        self.CONNECT = 0
    
        self.serversocket = socket.socket() 
        try:
            self.serversocket.bind((self.address,self.port))
        except:
            try:
                print("Sorry.May be you have to connect the next.")
                self.serversocket.bind((self.address,self.port+1))
            except:
                print("No Post to open.")
        self.serversocket.listen(5)
        self.sock,self.addr = self.serversocket.accept()      
        self.ch = 0
        self.rt = ""
        self.CONNECT = 1
        
    def run(self):
        while 1:
            #print(self.ch)
            try:
                self.ch = self.sock.recv(4096).decode()
            except:
                self.sock,self.addr = self.serversocket.accept()      

            if self.CONNECT and self.rt:
                try:
                    self.sock.send(self.rt."""""")
                    sleep(0.02)
                    self.rt = ""
                    self.sock.close()
                finally:
                    self.sock,self.addr = self.serversocket.accept()      

if __name__=="__main__":
    sl = socketListen()
    sl.rt = "hi\n"
    sl.start()
    