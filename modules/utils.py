# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

# External libs
import os, math, sys
from random import randint
from math import sqrt

import shared, prop

if os.name == 'nt': # Caso executado sob arq, NT
	import msvcrt
	getch = msvcrt.getwch
	def clear(): os.system('cls')
elif os.name == 'posix': # Caso executado sob arq. Posix
	from getch import getch
	def clear(): os.system('clear')

def exit():
    sys.exit()

def ReadTxt(File):
	with open(File, encoding='utf-8') as txt:
		print(txt.read())

def LogoGen():
	prop.RandLogo = randint(0,13) # Random logo generator

def LogoType(Path): # game logo
    clear()
    ReadTxt((Path+'logotype'+str(prop.RandLogo)+'.txt'))

def CheckForInt(x):
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
    x1 = round(float(((b*-1)+math.sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    x2 = round(float(((b*-1)-math.sqrt((b**2)-4*a*c))/(2*a)),FloatPrec)
    return x1,x2 # Retorna tupla

def SolveFQuad(a,b,c,FloatPrec): # Recebe a, b e c. Retorna as raízes e as coordenadas
                                 # do vértice.
    x1 = round((FloatFormat((b*-1)+round(math.sqrt(SolveDelta(a,b,c)),FloatPrec))/(2*a)),FloatPrec)
    x2 = round((FloatFormat((b*-1)-round(math.sqrt(SolveDelta(a,b,c)),FloatPrec))/(2*a)),FloatPrec)
    xv = round(((b*-1)/(2*a)),FloatPrec)
    yv = round(((SolveDelta(a,b,c)*-1)/(4*a)),FloatPrec)
    return x1,x2,xv,yv # Retorna tupla
    # interseção com y = c

def CheckForFloatList(List): # Verifica se valor em uma lista é float.
    for i in range(len(List)):
        if CheckForFloat(List[i]) == False:
            return False
        
def CheckForOneStringList(List,String): # Verifica se há string específica em uma lista.
    for i in range(len(List)):      # Leitura: True --> Há tal string. False --> Ñ há
        if List[i] == String:
            return True

def FloatFormat(x): # Corrige imprecisão ao operar valores flutuantes.
    return float(format((x),'8f'))

#class rl(Str):
#    def LangPath(Lang):
#        if shared.Lang == 'pt_br':
#            return ('./languages/pt_br')
#    def ReadJson(Str,Path): # Recebe local do .json e nome; retorna valor corresp. 
#        data = json.loads(open(Path).read())
#        return data[Str]
#rl(Str) = rl(Str)

def SolvePit(c1,c2): # Recebe c1 e c2, retorna hip.
	hip = math.sqrt((c1**2)+(c2**2))
	return hip

#def GenTR(Max): # Recebe valor max, retorna medidas correspondentes a um triângulo retângulo.
#	anga = randint(0,Max)
#	xtr = randint(0,Max)
#	ytr = (math.sin(anga)*xtr)
#	ztr = (math.cos(anga)*xtr)
#	return xtr, ytr, ztr, anga # Retorna tupla

def GenCircle(Min,Max,FloatPrec): # Recebe min/max. Retorna medidas correspondentes a um círculo.
	Pi = round((4*(4*math.atan(1/5)-math.atan(1/239))),FloatPrec) # Pi calculado pela fórmula de Machin.
	Radius = randint(Min,Max)
	Area = round(FloatFormat(Pi*(Radius**2)),FloatPrec)
	return Radius, Pi, Area # Retorna tupla

def GenQuad(Min,Max,FloatPrec): # Recebe min/max. Retorna medidas correspondentes a um quadrado.
	Side = randint(Min,Max)
	Area = round(Side**2)
	return Side, Area # Retorna tupla

def GenTriangle(Min,Max,FloatPrec): # Recebe min/max. Retorna valores correspodentes a um
                                    # triângulo
	Base = randint(Min,Max)
	Height = randint(Min,Max)
	Area = round(FloatFormat(((Base*Height)/2)),FloatPrec)
	return Base, Height, Area # Retorna tupla

def GenRectangle(Min,Max):# Recebe min/max. Retorna medidas correspondentes a um retângulo
	Base = randint(Min,Max)
	Height = randint(Min,Max)
	Area = Base*Height
	return Base, Height, Area

def CheckForN(x): # Leitura:
	if int(x) == x: return True # É natural
	else: return False # Ñ é natural

def CheckForPrime(x): # Leitura:
	for i in range(1,x):
		if i != 1:
			if int(x/i) == (x/i):
				return False # Ñ é primo
	return True # É primo