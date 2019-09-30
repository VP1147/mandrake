# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import utils, shared, prop

def PtgsMenu():
	utils.LogoType(shared.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	prop.PtgsModeOpt = utils.getch()
	if prop.PtgsModeOpt == 'x':
		return 0
	utils.clear()
	utils.ReadTxt((shared.GameLogoPath+'pit.txt')) # Mode logo
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = Ptgs(prop.PtgsModeOpt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Ptgs(prop.PtgsModeOpt))
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+List[i])
			utils.getch()
			return 0

def Ptgs(Opt):
	x = utils.randint(shared.IntMin,shared.IntMax)
	y = utils.randint(shared.IntMin,shared.IntMax)
	z = utils.randint(shared.IntMin,shared.IntMax)
	if Opt == '1': # P/ otimizar ...
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

