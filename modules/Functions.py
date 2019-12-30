# -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared, prop, utils

def QuadFMenu():
	utils.clear()
	if utils.MinSize() == True: utils.ReadTxt((shared.GameLogoPath+'function.txt')) # Mode logo
	else: print("< f(x) >")
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
	Delta, x1, x2, Xv, Yv, a, b, c = utils.GenBhaskara(shared.IntMin,shared.IntMax,shared.FloatPrec)
	rs = (Delta,x1,x2,Xv,Yv)
	l = []
	q = ("Delta","x1 (+)","x2 (-)","Xv","Yx")
	print(utils.Sig(a),"x\N{SUPERSCRIPT TWO} ",utils.Sig(b),"x ",utils.Sig(c))
	for i in range(len(rs)):
		r = input(q[i]+" = ")
		if shared.RCount == 0 and r == 'exit': return 'exit'
		if utils.CheckForFloat(r) == False: l.append('Nula')
		elif r == rs[i]: # Caso certo
			print("Certo")
			l.append('Certo')
		else: # Caso diferente
			print("O correto seria "+str(rs[i])+".")
			l.append('Errado')
	return l

def SimpleFMenu():
	utils.clear()
	if utils.MinSize() == True: utils.ReadTxt((shared.GameLogoPath+'function.txt')) # Mode logo
	else: print("< f(x) >")
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = SimpleF()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,SimpleF())
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			utils.getch()
			return 0

# TODO
#def SimpleF():
