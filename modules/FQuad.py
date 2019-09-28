# -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared, prop, utils

def QuadFMenu():
	utils.clear()
	utils.ReadTxt((shared.GameLogoPath+'function.txt')) # Mode logo
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = QuadF()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,QuadF())
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			utils.getch()
			return 0

def QuadF():
	a = utils.randint(shared.IntMin,shared.IntMax)
	b = utils.randint(shared.IntMin,shared.IntMax)
	c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
	x1rs, x2rs, xvrs, yvrs = utils.SolveFQuad(a,b,c,shared.FloatPrec) # Calcula
                                                                # x1, x2, Xv e Yv.
	RList = []
	drs = utils.SolveDelta(a,b,c) # Calcula delta
	print(str(a)+"*x\N{SUPERSCRIPT TWO} + "+str(b)+"x + ("+str(c)+")")
	dr = input("Delta = ")
	if shared.RCount == 0 and dr == 'exit': return 'exit' # Otimizar essa sessão...
	else: RList.append(QuadFVerify(dr,drs))
	x1r = input("x1 = ")
	if shared.RCount == 0 and x1r == 'exit': return 'exit'
	else: RList.append(QuadFVerify(x1r,(x1rs,x2rs)))
	x2r = input("x2 = ")
	if shared.RCount == 0 and x2r == 'exit': return 'exit'
	else: RList.append(QuadFVerify(x2r,(x1rs,x2rs)))
	xvr = input("Xv = ")
	if shared.RCount == 0 and xvr == 'exit': return 'exit'
	else: RList.append(QuadFVerify(xvr,xvrs))
	yvr = input("Yv = ")
	if shared.RCount == 0 and yvr == 'exit': return 'exit'
	else: RList.append(QuadFVerify(yvr,yvrs))
	iyr = input("Interseção com y = ")
	if iyr == 'exit': return 'exit'
	else: RList.append(QuadFVerify(iyr,c))
	return RList

def QuadFVerify(x,r):
    if utils.CheckForFloat(x) == False: # Caso x não for float
        return 'Nula'
    if isinstance(r,tuple) == True: # Caso r for tupla
        r1,r2 = r
        if float(x) == r1 or float(x) == r2: # Caso certo
        	print("Certo")
        	return 'Certo'
        else: # Caso diferente
        	print("O correto seria "+str(r1)+" ou "+str(r2)+".")
        	return 'Errado'
    else:
        if float(x) == r: # Caso certo
        	print("Certo")
        	return 'Certo'
        else: # Caso diferente
        	print("O correto seria "+str(r)+".")
        	return 'Errado'     

