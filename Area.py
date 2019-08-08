# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import shared
import prop

def AreaMenu(GameMenu):
	utils.LogoType()
	print("<---Modo--->")
	print("1 - Círculo")
	print("2 - Quadrado")
	#print("3 - Triângulo")
	print("x - Voltar")
	prop.AreaModeOpt = utils.getch()
	if prop.AreaModeOpt == 'x':
		return GameMenu()
	elif prop.AreaModeOpt == '1':
		CircleArea(GameMenu,AreaMenu)
	elif prop.AreaModeOpt == '2':
		QuadArea(GameMenu,AreaMenu)
	else: return AreaMenu(GameMenu)

def CircleArea(GameMenu,AreaMenu):
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		Rad,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec)
		r = input("Raio = "+str(Rad)+" | Área = ")
		rs = Area
		if utils.CheckForFloat(r) == False: # Caso não-float
			if r == 'exit': return AreaMenu(GameMenu)
			# Loop continua caso r != exit
		else: # Caso Float
			if float(r) == rs: print("Certo")
			else: print("O certo seria "+str(rs))

def QuadArea(GameMenu,AreaMenu):
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		Side, Area = utils.GenQuad(shared.IntMin,shared.IntMax,shared.FloatPrec)
		r = input("Lado = "+str(Side)+" | Área = ")
		rs = Area
		if utils.CheckForFloat(r) == False: # Caso não-float
			if r == 'exit': return AreaMenu(GameMenu)
			# Loop continua caso r != exit
		else: # Caso Float
			if float(r) == rs: print("Certo")
			else: print("O certo seria "+str(rs))

