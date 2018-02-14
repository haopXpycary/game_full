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
DEBUG = "+"

MaxScrX = 31
MaxScrY = 15
MaxHealthAdder = 1
MaxExpAdder    = 1

debugMode = 0

def levelUp(n):
    return 2*n**n
#最少150%
levelAdd = 1.5

#--adderKind----------------------------------------------
healthAdder = 1
expAdder    = 2

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
AFIRE  = "f"