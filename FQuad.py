# -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared
import prop
from math import sqrt
import utils

def QuadFMenu(GameMenu):
    utils.clear()
    print("<'exit' para sair>")
    print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
    while 1:
        QuadF(GameMenu)
        
def QuadF(GameMenu):
    a = utils.randint(shared.IntMin,shared.IntMax)
    b = utils.randint(shared.IntMin,shared.IntMax)
    c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
    x1rs, x2rs, xvrs, yvrs = utils.SolveFQuad(a,b,c,shared.FloatPrec) # Calcula
                                                                 # x1, x2, Xv e Yv.
    drs = utils.SolveDelta(a,b,c) # Calcula delta
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    dr = input("Delta = ")
    QuadFVerify(dr,drs,GameMenu)
    x1r = input("x1 = ")
    QuadFVerify(x1r,(x1rs,x2rs),GameMenu)
    x2r = input("x2 = ")
    QuadFVerify(x2r,(x1rs,x2rs),GameMenu)
    xvr = input("Xv = ")
    QuadFVerify(xvr,xvrs,GameMenu)
    yvr = input("Yv = ")
    QuadFVerify(yvr,yvrs,GameMenu)
    iyr = input("Interseção com y = ")
    QuadFVerify(iyr,c,GameMenu)

def QuadFVerify(x,r,GameMenu):
    if utils.CheckForFloat(x) == False:
        if x == 'exit': return GameMenu()
        else: return QuadF(GameMenu)
    if isinstance(r,tuple) == True: # Caso r for tupla
        r1,r2 = r
        if float(x) == r1 or float(x) == r2: print("Certo")
        else: print("O correto seria "+str(r1)+" ou "+str(r2)+".")
    else:
        if float(x) == r: print("Certo")
        else: print("O correto seria "+str(r)+".")
