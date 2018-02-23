from Const_H__ import *
#四舍五入
def fofi(x):
    if x % 1 >= 0.5:
        return x - x%1 + 1
    else:
        return x - x%1

def pvars(*argc,**argv):
    def pvar(cls):
        if debugMode:
            print(cls.__name__)
            print(vars(cls(*argc,**argv)))
    return pvar

def skills(filename):
    f = open(__file__[:__file__.rfind("/")]+"/Skill/"+filename+".py","r")
    exec(compile("".join(f.readlines()),"","exec"))
#skills("WJQF")