# library for Mandrake | by vp1147
import os
from random import randint
import shared
import re
import math
import prop

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _GetchUnix()

def LogoGen():
    prop.RandLogo = randint(0,4) # Random logo generator

def clear(): # clear screen function
    os.system('cls||clear') # For Windows-Linux compatibility

def LogoType(): # game logo
    clear()
    with open('./design/logotype'+str(prop.RandLogo)+'.txt') as txt:
        print(txt.read())

def CheckForInt(x): # Following the "vp1147's box analogy"
    # <DEPRECATED>
    #pattern = re.compile("^[0-9][0-9]*\.?[0-9]*") # Int number pattern
    #confirm = re.search(pattern,str(z)) # Verify 'z'
    #if not confirm:
    #    return False # return function value 'False' --> boolean
    #elif confirm:
    #    return True
    try:
        int(x)
    except ValueError:
        return False
    except:
        return True

def CheckForFloat(x): # Leitura de saída:
    try:              # True --> É float
        float(x)      # False --> Não é float
    except ValueError:
        return False
    except:
        return True

def CheckForNegSqrt(x): # NegSqrt disabled. Func deprecated
    try:
        math.sqrt(x)
    except ValueError:
        return True
    return False
