# -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared
import prop
import utils

def QuadFMenu():
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		a = utils.randint(shared.IntMin,shared.IntMax)
		b = utils.randint(shared.IntMin,shared.IntMax)
		c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
		x1rs, x2rs, xvrs, yvrs = utils.SolveFQuad(a,b,c,shared.FloatPrec) # Calcula
                                                                 # x1, x2, Xv e Yv.
		drs = utils.SolveDelta(a,b,c) # Calcula delta
		print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
		dr = input("Delta = ")
		if dr == 'exit': return 0
		else: QuadFVerify(dr,drs)
		x1r = input("x1 = ")
		if x1r == 'exit': return 0
		else: QuadFVerify(x1r,(x1rs,x2rs))
		x2r = input("x2 = ")
		if x2r == 'exit': return 0
		else: QuadFVerify(x2r,(x1rs,x2rs))
		xvr = input("Xv = ")
		if xvr == 'exit': return 0
		else: QuadFVerify(xvr,xvrs)
		yvr = input("Yv = ")
		if yvr == 'exit': return 0
		else: QuadFVerify(yvr,yvrs)
		iyr = input("Interseção com y = ")
		if iyr == 'exit': return 0
		else: QuadFVerify(iyr,c)

def QuadFVerify(x,r):
    if utils.CheckForFloat(x) == False:
        return 0
    if isinstance(r,tuple) == True: # Caso r for tupla
        r1,r2 = r
        if float(x) == r1 or float(x) == r2: print("Certo")
        else: print("O correto seria "+str(r1)+" ou "+str(r2)+".")
    else:
        if float(x) == r: print("Certo")
        else: print("O correto seria "+str(r)+".")        

