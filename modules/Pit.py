# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import utils, shared, prop

def PtgsMenu():
	utils.LogoType()
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	prop.PtgsModeOpt = utils.getch()
	if prop.PtgsModeOpt == 'x':
		return GameMenu()
	utils.clear()
	utils.ReadTxt(('./design/ModeLogo/logotype'+str(prop.PtgsModeOpt)+'.txt')) # Mode logo
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		x = utils.randint(shared.IntMin,shared.IntMax)
		y = utils.randint(shared.IntMin,shared.IntMax)
		z = utils.randint(shared.IntMin,shared.IntMax)
		if prop.PtgsModeOpt == '1':
			if x >= y and x >= z: # Caso x maior
				r = input("c1 = "+str(y)+", c2 = "+str(z)+", hip = raiz quadrada de ")
				rs = (y**2)+(z**2)
			elif y >= x and y >= z: # Caso y maior
				r = input("c1 = "+str(x)+", c2 = "+str(z)+", hip = raiz quadrada de ")
				rs = (x**2)+(z**2)
			elif z >= x and z >= y: # Caso z maior
				r = input("c1 = "+str(x)+", c2 = "+str(y)+", hip = raiz quadrada de ")
				rs = (x**2)+(y**2)
		elif prop.PtgsModeOpt == '2':
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
			if r == 'exit': return 0
			else: pass
		else:
			if float(r) == rs: print("Certo")
			else: print("O certo seria "+str(rs))
			

