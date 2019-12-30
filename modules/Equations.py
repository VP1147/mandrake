# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import utils, shared, prop

def PtgsMenu():
	utils.LogoType(shared.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	Opt = utils.getch()
	if Opt == 'x' or int(Opt) > 2: return 0
	utils.clear()
	if utils.MinSize() == True: utils.ReadTxt((shared.GameLogoPath+'pit.txt')) # Mode logo
	else: print("< Pitágoras >")
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = Ptgs(Opt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Ptgs(Opt))
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+List[i])
			utils.getch()
			return 0

def Ptgs(Opt): # TODO: Optimize
	x = utils.randint(shared.IntMin,shared.IntMax)
	y = utils.randint(shared.IntMin,shared.IntMax)
	z = utils.randint(shared.IntMin,shared.IntMax)
	if Opt == '1':
		if x >= y and x >= z: # Caso x maior
			r = input("c1 = "+str(y)+", c2 = "+str(z)+", hip = raiz quadrada de ")
			rs = (y**2)+(z**2)
		elif y >= x and y >= z: # Caso y maior
			r = input("c1 = "+str(x)+", c2 = "+str(z)+", hip = raiz quadrada de ")
			rs = (x**2)+(z**2)
		elif z >= x and z >= y: # Caso z maior
			r = input("c1 = "+str(x)+", c2 = "+str(y)+", hip = raiz quadrada de ")
			rs = (x**2)+(y**2)
	elif Opt == '2':
		if x >= y and x >= z: # Caso x maior
			r = input("c1 = "+str(y)+", c2 = "+str(z)+", hip = ")
			rs = round(utils.sqrt((y**2)+(z**2)),shared.FloatPrec)
		elif y >= x and y >= z: # Caso y maior
			r = input("c1 = "+str(x)+", c2 = "+str(z)+", hip = ")
			rs = round(utils.sqrt((x**2)+(z**2)),shared.FloatPrec)
		elif z >= x and z >= y: # Caso z maior
			r = input("c1 = "+str(x)+", c2 = "+str(y)+", hip = ")
			rs = round(utils.sqrt((x**2)+(y**2)),shared.FloatPrec)

	if utils.CheckForFloat(r) == False:
		if r == 'exit': return 'exit'
		else: return 'Nula'
	else:
		if float(r) == rs: 
			print("Certo")
			return 'Certo'
		else: 
			print("O certo seria "+str(rs))
			return 'Errado'

def BskrMenu():
	utils.LogoType(shared.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	Opt = utils.getch()
	if Opt == 'x' or int(Opt) > 2: return 0
	utils.clear()
	if utils.MinSize() == True: utils.ReadTxt((shared.GameLogoPath+'bhaskara.txt')) # Mode logo
	else: print("< Bhaskara >")
	print("<'exit' para sair>")
	print("<Precisão de ",shared.FloatPrec," decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = Bhaskara(Opt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Bhaskara(Opt))
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			utils.getch()
			return 0

def Bhaskara(Opt):
	Delta, x1, x2, xv, yv, a, b, c = utils.GenBhaskara(shared.IntMin, shared.IntMax, shared.FloatPrec)
	l = []
	if Opt == '1':
		print(utils.Sig(a),"x\N{SUPERSCRIPT TWO} ",utils.Sig(b),"x ",utils.Sig(c))
		r = input("Delta = ")
		if r == 'exit' and shared.RCount == 0: return 'exit'
		if utils.CheckForFloat(r) == False: l.append('Nula')
		if r == Delta: 
			print("Certo")
			l.append('Certo')
		else: 
			print("O correto seria ",Delta,".")
			l.append('Errado')
	elif Opt == '2':
		q = ("Delta","x1 (+)","x2 (-)")
		rs = (Delta,x1,x2)
		print(utils.Sig(a),"x\N{SUPERSCRIPT TWO} ",utils.Sig(b),"x ",utils.Sig(c))
		for i in range(len(rs)):
			r = input(q[i]+" = ")
			if r == 'exit' and shared.RCount == 0: return 'exit'
			elif utils.CheckForFloat(r) == False: l.append('Nula')
			if r == rs[i]: 
				print("Certo")
				l.append('Certo')
			else: 
				print("O correto seria ",rs[i],".")
				l.append('Errado')
	return l

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
