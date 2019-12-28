# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import utils, shared, prop

def BskrMenu():
	utils.LogoType(shared.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	prop.BskrModeOpt = utils.getch()
	if prop.BskrModeOpt == 'x':
		return 0
	utils.clear()
	if MinSize() == True: utils.ReadTxt((shared.GameLogoPath+'bhaskara.txt'))
	else: print("<Bhaskara>")
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = Bhaskara()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Bhaskara())
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			utils.getch()
			return 0

def Bhaskara():
	a = utils.randint(shared.IntMin,shared.IntMax)
	b = utils.randint(shared.IntMin,shared.IntMax)
	c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
	RList = []
	if prop.BskrModeOpt == '1':
		drs = utils.SolveDelta(a,b,c) # Calcula delta
		dr = input(str(a)+"x\N{SUPERSCRIPT TWO} + "+str(b)+"x + ("+str(c)+"). Delta = ")
		if dr == 'exit': return 'exit'
		else: RList.append(BskrVerify(dr,drs))
	elif prop.BskrModeOpt == '2':
		x1rs,x2rs = utils.SolveBhaskara(a,b,c,shared.FloatPrec) # Calcula x1 e x2
		drs = utils.SolveDelta(a,b,c) # Calcula delta
		print(str(a)+"x\N{SUPERSCRIPT TWO} + "+str(b)+"x + ("+str(c)+")")
		dr = input("Delta = ")
		if dr == 'exit': return 'exit'
		else: RList.append(BskrVerify(dr,drs))
		x1r = input("x1 = ")
		if x1r == 'exit': return 'exit' # Se 'x'
		else: RList.append(BskrVerify(x1r,(x1rs,x2rs))) # Senão, verificação normal
		x2r = input("x2 = ")
		if x2r == 'exit': return 'exit'
		else: RList.append(BskrVerify(x2r,(x1rs,x2rs)))
	return RList

def BskrVerify(x,r):
	if utils.CheckForFloat(x) == False:
		return 'Nula'
	if isinstance(r,tuple) == True: # Caso r for tupla
		r1,r2 = r
		if float(x) == r1 or float(x) == r2: 
			print("Certo")
			return 'Certo'
		else: 
			print("O correto seria "+str(r1)+" ou "+str(r2)+".")
			return 'Errado'
	else:
		if float(x) == r: 
			print("Certo")
			return 'Certo'
		else: 
			print("O correto seria "+str(r)+".")
			return 'Errado'

