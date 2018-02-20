import socket,threading
from time import sleep
from os import system

class socketListen(threading.Thread):
    def __init__(self):
        super().__init__(self)
        
        self.sock = socket.socket() 
        self.sock.connect(("192.168.1.105",8080))
        self.lastch = 0
        print(self.sock)
   
    def run(self):
        while 1:
            try:
                self.sock.sendall("""GET /favicon.ico HTTP/1.1
Host: 127.0.0.1:5467
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; MI 4LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3
Accept: */*
Referer: http://127.0.0.1:5467/
Accept-Encoding: gzip, deflate
Accept-Language: en-US""".encode())
                self.ch = self.sock.recv(4096).decode()
                sleep(0.2)
                #draw(self.ch,self.lastch)
            finally:
                self.sock = socket.socket() 
                self.sock.connect(("192.168.1.100",8080))
    def send(self,st):
        pass
if __name__=="__main__":
    sl = socketListen()
    sl.start()