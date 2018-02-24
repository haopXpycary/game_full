from Const_H__ import *
from os import chdir

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

def writeScore(s_time,sec,level,way,e_way):
    chdir(__file__[:__file__.rfind("/")])
    with open("MaxScore.txt","a") as fMaxScore:
        fMaxScore.write("""
+---------+---------+-------------+------------------------------+
|Sec:%5.2f|Level:%3d|Way:%4d:%-4d|Time:%s|"""%(sec,level,way,e_way,s_time))