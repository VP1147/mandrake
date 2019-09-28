# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import shared
import prop

def AreaMenu():
	utils.LogoType(shared.LogoPath)
	print("<---Modo--->")
	print("1 - Círculo")
	print("2 - Quadrado")
	print("3 - Triângulo")
	print("x - Voltar")
	prop.AreaModeOpt = utils.getch()
	if prop.AreaModeOpt == 'x':
		return 0
	elif prop.AreaModeOpt == '1':
		utils.clear()
		print("<'exit' para sair>")
		print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
		while 1:
			Rad,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Raio = "+str(Rad)+" | Área = ")
			if r == 'exit': return 0
			rs = Area
			CheckAnswer(rs,r)
	elif prop.AreaModeOpt == '2':
		utils.clear()
		print("<'exit' para sair>")
		print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
		while 1:
			Side,Area = utils.GenQuad(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Lado = "+str(Side)+" | Área = ")
			if r == 'exit': return 0
			rs = Area
			CheckAnswer(rs,r)
	elif prop.AreaModeOpt == '3':
		utils.clear()
		print("<'exit' para sair>")
		print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
		while 1:
			Base,Height,Area = utils.GenTriangle(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Base = "+str(Base)+" | Altura = "+str(Height)+" | Área = ")
			if r == 'exit': return 0
			rs = Area
			CheckAnswer(rs,r)

def CheckAnswer(rs,r):
	if utils.CheckForFloat(r) == False: # Caso não-float
		return 0
	else: # Caso Float
		if float(r) == rs: print("Certo")
		else: print("O certo seria "+str(rs))

