# library for Mandrake | by vp1147
import os
from random import randint
import shared
import re
import math

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
    global randLogo
    randLogo = randint(0,4) # logo def

def clear(): # clear screen function
    os.system('cls||clear')

def LogoType(): # game logo
    clear()
    with open('./design/logotype'+str(randLogo)+'.txt') as txt:
        print(txt.read())

def CheckForInt(z):
    # <DEPRECATED>
    #pattern = re.compile("^[0-9][0-9]*\.?[0-9]*") # Int number pattern
    #confirm = re.search(pattern,str(z)) # Verify 'z'
    #if not confirm:
    #    return False # return function value 'False' --> boolean
    #elif confirm:
    #    return True
    try:
        int(z)
    except ValueError:
        return False
    except:
        return True

def CheckForFloat(z):
    try:
        float(z)
    except ValueError:
        return False
    except:
        return True

def CheckForNegSqrt(r):
    try:
        math.sqrt(r)
    except ValueError:
        return True
    return False
