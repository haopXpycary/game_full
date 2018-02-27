'''
bgard.py --一个简易的工作表程序
'''

class bgard:
    def __init__(self,L=[]):
        self.gard = L
        self._toBeStr()
        self._regard()
        self._getXY()
        self.finish()
        
    def finish(self):
        self._toBeStr()
        self._regard()
        self._getXY()

    def addXLine(self,value=[""],x=-1):
        while len(value) < len(self.gard):
            value.append("")
            
        if x == -1:
            for i,j in zip(range(len(value)),range(len(self.gard))):
                self.gard[i].append(value[i])
            return
            
        for i,j in zip(range(len(value)),range(len(self.gard))):
            self.gard[i].insert(x,value[i])
        
    def removeXLine(self,x=-1):
        for i in range(len(self.gard)):
            self.gard[i][x] = ""
        
    def addYLine(self,value=[],y=-1):
        while len(value) < len(self.gard[0]):
            value.append("")
            
        if y == -1: 
            self.gard.append(value)
            return
        self.gard.insert(y,value) 
        
    def removeYLine(self,y=-1):
        del self.gard[y]
        
    def setValue(self,x,y,value):
        self.gard[y][x] = value
        
    def removeValue(self,x,y):
        self.gard[y][x] = ""
    
    def _regard(self):
        maxX = 0
        for i in range(len(self.gard)):
            if len(self.gard[i]) > maxX:
                maxX = len(self.gard[i])
       
        for i in range(len(self.gard)):
            while len(self.gard[i]) < maxX:
                self.gard[i].append("")
                
    def _toBeStr(self):
        for i in range(len(self.gard)):
            for j in range(len(self.gard[i])):
                self.gard[i][j] = str(self.gard[i][j])
    
    def _getXY(self):
        self._Y = len(self.gard)
        
        self._X = []
        maxX = 0
        for i in range(len(self.gard[0])):
            for j in range(self._Y):
                if len(self.gard[j][i]) > maxX:
                    maxX = len(self.gard[j][i])
            self._X.append(maxX)
            maxX = 0
    
    def _makeLine(self):
        self._line = "+"
        for i in self._X:
            self._line += "-"*(i+2)+"+"
            
    def _makeValueLine(self):
        self._lineValue = []
        lineValue = "|"
        
        for i in range(len(self.gard)):
            for j in range(len(self.gard[i])):
                lineValue += self.gard[i][j].center(self._X[j]+2)
                lineValue += "|"
            self._lineValue.append(lineValue)
            lineValue = "|"
            
    def _paste(self):
        self._pic = [self._line]
        for i in self._lineValue:
            self._pic.append(i)
            self._pic.append(self._line)
            
    def _show(self):
        print("\n".join(self._pic))
        
    def show(self):
        self.finish()
        self._getXY()
        self._makeLine()
        self._makeValueLine()
        self._paste()
        self._show()
       
a = bgard([[1,3],[4,5,6],["hello","you","sister"]])
a.show()
a.addYLine([1,2,3])
a.addXLine(list(range(12)))
a.show()