# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

# External libs
import os, math, sys
from random import randint
from math import sqrt
# import numpy as np
# import matplotlib.pyplot as plt

import shared, prop

def exit(): sys.exit()

def ReadTxt(File):
	with open(File, encoding='utf-8') as txt:
		print(txt.read())

def LogoGen(): prop.RandLogo = randint(0,13) # Random logo generator

def MinSize():
	if os.get_terminal_size(0).lines >= 18 and os.get_terminal_size(0).columns >= 100:
		return True
	else: return False

def LogoType(Path): # game logo
    clear()
    if MinSize() == True: ReadTxt((Path+'logotype'+str(prop.RandLogo)+'.txt'))
    else: print("<-- Mandrake -->")

def CheckForInt(x):
    # <DEPRECATED>
    #pattern = re.compile("^[0-9][0-9]*\.?[0-9]*") # Int number pattern
    #confirm = re.search(pattern,str(z)) # Verify 'z'
    #if not confirm:
    #    return False # return function value 'False' --> boolean
    #elif confirm:
    #    return True
	try: int(x)
	except ValueError: return False
	except: return True

def CheckForFloat(x): # Leitura de saída:
    try:              # True --> É float
        float(x)      # False --> Não é float
    except ValueError: return False
    except: return True

def CheckForNegSqrt(x): # NegSqrt disabled. Func deprecated
    try: math.sqrt(x)
    except ValueError: return True
    return False

def SolveBhaskara(a,b,c,FloatPrec): # Recebe a, b e c. Retorna as raízes e as coordenadas
                                 # do vértice.
    Delta = round((b**2)-4*a*c,FloatPrec)
    x1 = round((FloatFormat((b*-1)+round(math.sqrt(Delta),FloatPrec))/(2*a)),FloatPrec)
    x2 = round((FloatFormat((b*-1)-round(math.sqrt(Delta),FloatPrec))/(2*a)),FloatPrec)
    xv = round(((b*-1)/(2*a)),FloatPrec)
    yv = round(((Delta*-1)/(4*a)),FloatPrec)
    return Delta, x1, x2, xv, yv # Retorna tupla

def CheckForFloatList(List): # Verifica se valor em uma lista é float.
    for i in range(len(List)):
        if CheckForFloat(List[i]) == False: return False
        
def CheckForOneStringList(List,String): # Verifica se há string específica em uma lista.
    for i in range(len(List)):      # Leitura: True --> Há tal string. False --> Ñ há
        if List[i] == String: return True

def FloatFormat(x): return float(format((x),'8f'))# Corrige imprecisão ao operar valores flutuantes.

#class rl(Str):
#    def LangPath(Lang):
#        if shared.Lang == 'pt_br':
#            return ('./languages/pt_br')
#    def ReadJson(Str,Path): # Recebe local do .json e nome; retorna valor corresp. 
#        data = json.loads(open(Path).read())
#        return data[Str]
#rl(Str) = rl(Str)

def SolvePit(c1,c2): return math.sqrt((c1**2)+(c2**2)) # Recebe c1 e c2, retorna hip.

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
			if int(x/i) == (x/i) and x > 1:
				return False # Ñ é primo
	return True # É primo

def DivCheck(x):
	List = []
	for i in range(1,x):
		if int(x/i) == (x/i):
			List.append(i)
	return List

def Chudnovsky(disp, prec,maxK=70): 
	from decimal import Decimal as Dec, getcontext as gc
	gc().prec = prec
	K, M, L, X, S = 6, 1, 13591409, 1, 13591409
	for k in range(1, maxK+1):
		M = (K**3 - 16*K) * M // k**3 
		L += 545140134
		X *= -262537412640768000
		S += Dec(M * L) / X
		K += 12
		pi = 426880 * Dec(10005).sqrt() / S
	pi = Dec(str(pi)[:disp]) # drop few digits of precision for accuracy
	return pi

def AritMean(x): # X: tupla. Retorna média dos valores na tupla 'x'
	return sum(float(i) for i in x)/len(x)

def MultiplyList(x): # Multiply elements one by one. Traversal method.
	aux = 1
	for i in x:
		aux = aux * i
	return aux

def GeometricMean(x): return math.sqrt(MultiplyList(x))# Retorna a média geométrica da lista 'x'

def CalcFunction(f,x):	# Recebe uma função 'f' e uma tupla 'x'.
	List = []	# Retorna uma lista com os valores com f(x)
			# variando entre x[0] e x[1].
	for i in range(x[0],x[1]):
		List.append(f(i))
	return List

# TODO
#def PlotTool(f): # Plot a function using Matplotlib and Numpy
#	x = np.linspace(0, 2, 100)
#	plt.plot(x, float(f), label=str(f))
#	plt.xlabel('x')
#	plt.ylabel('y')
#	plt.legend()
#	plt.show()

def LinearPlot(x,List):
	Values = []
	for i in range(len(List)):
		Values.append(x*List[i])
	return Values

# TODO: Add a general-purpose function generator, solver and plotter
#		w/ Matplotlib and Numpy

if os.name == 'nt': # Caso executado sob arq, NT
	import msvcrt
	getch = msvcrt.getwch
	def clear(): os.system('cls')
elif os.name == 'posix': # Caso executado sob arq. Posix
	from getch import getch
	def clear(): os.system('clear')