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
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    x1r = input("x1 = ")
    if x1r == 'exit': return GameMenu()
    x2r = input("x2 = ")
    if x1r == 'exit': return GameMenu()
    xvr = input("Xv = ")
    if x1r == 'exit': return GameMenu()
    yvr = input("Yv = ")
    if x1r == 'exit': return GameMenu()
    iyr = input("Interseção com y = ")
    if x1r == 'exit': return GameMenu()
    r = [x1r,x2r,xvr,yvr,iyr]
    if utils.CheckForFloatList(r) == False:
        return QuadF(GameMenu)
    if (float(x1r) == x1rs and float(x2r) == x2rs) or (float(x1r) == x2rs and float(x2) == x1rs)  and float(xvr) == xvrs and float(yvr) == yvrs and iyr == c:
        print("Certo") # Difícil acontecer :)
    else:
        print("O certo seria "+str(x1rs)+", "+str(x2rs)+", "+str(xvrs)+", "+str(yvrs)+", "+str(c))
