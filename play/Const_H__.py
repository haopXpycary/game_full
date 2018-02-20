from playMode import *
	
#--headfor----------------------------------------------
Right = 1
Left = 2
Up = 3
Down = 4

#--press key----------------------------------------------
RIGHT = "6"
LEFT  = "4"
UP    = "2"
DOWN  = "8"
FIRE  = "5"
TP    = "3"
WJQF  = "+"
QPZD  = "-"
DEBUG = ":"
ADDEXP = "'"

MaxScrX = 41
MaxScrY = 15
FULLSCRCHAR = " "
if hideScr:
    FULLSCRCHAR = "#"

MaxHealthAdder = 2
MaxExpAdder    = 2
MaxMoneyAdder  = 3

debugMode = 0

levelUp = lambda n:n**2

#最少150%
levelAdd = 1.5

#--adderKind----------------------------------------------
healthAdder = 1
expAdder    = 2
moneyAdder  = 3

#--color----------------------------------------------
BLACK     = "\033[30m"
RED       = "\033[31m"
GREEN     = "\033[32m"
YELLOW    = "\033[33m"
BLUE      = "\033[34m"
PERPLE    = "\033[35m"
DEEPGREEN = "\033[36m"
WHITE     = "\033[37m"

#--前缀----------------------------------------------
PLAYER = "p"
HEALTH = "h"
EXP    = "e"
MONEY  = "m"
AFIRE  = "f"