# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import os
from random import randint
import shared
from math import sqrt
import prop
import sys

class _GetchUnix:
    def __init__(self):
        import tty

    def __call__(self):
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _GetchUnix()

def exit():
    sys.exit()

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

def SolveDelta(a,b,c): # Recebe a, b e c. Retorna o Delta.
    return ((b**2)-4*a*c)

def SolveBhaskara(a,b,c,FloatPrec): # Recebe a, b e c. Retorna as raízes.
    x1 = round(float(((b*-1)+sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    x2 = round(float(((b*-1)-sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    return x1,x2 # return tuple

def SolveFQuad(a,b,c,FloatPrec): # Recebe a, b e c. Retorna as raízes, coordenadas
    # do vértice e interseção com y.
    x1 = round(float(((b*-1)+sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    x2 = round(float(((b*-1)-sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    xv = round(float((b*-1)/(2*a)),FloatPrec)
    yv = round(float((SolveDelta(a,b,c)*-1)/(4*a)),FloatPrec)
    return x1,x2,xv,yv
    # interseção com y = c

def CheckForFloatList(List): # Verifica se valor em uma lista é float.
    for i in range(len(List)):
        if CheckForFloat(List[i]) == False:
            return False
        
def CheckForOneStringList(List,String): # Verifica se há string específica em uma lista.
    for i in range(len(List)):      # Leitura: True --> Há tal string. False --> Ñ há
        if List[i] == String:
            return True

def ReadTxt(File):
    with open(File) as txt:
        print(txt.read())
