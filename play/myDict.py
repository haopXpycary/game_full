class dict():
    def __init__(self):
        self.lip = []
    
    def __setitem__(self,key,value):
        self.lip.append((key,value))
    
    def __getitem__(self,name):
        for i in self.lip:
            if i[0] == name:
                return i[1]
    def clear(self):
        self.lip = []
    
    def values(self):
        sweet = []
        for i in self.lip:
            sweet.append(i[1])
        return sweet
    
    def keys(self):
        sweet = []
        for i in self.lip:
            sweet.append(i[0])
        return sweet

    def show(self):
        return self.lip