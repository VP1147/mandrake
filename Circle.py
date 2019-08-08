# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import prop
import shared

def CircleMenu(GameMenu,AreaMenu):
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		CircleArea(GameMenu,AreaMenu)

def CircleArea(GameMenu,AreaMenu):
	Rad,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec)
	r = input("Raio = "+str(Rad)+" | Área = ")
	rs = Area
	if utils.CheckForFloat(r) == False: # Caso não-float
		if r == 'exit': return AreaMenu(GameMenu)
		else: return CircleArea(GameMenu,AreaMenu)
	else: # Caso Float
		if float(r) == rs: print("Certo")
		else: print("O certo seria "+str(rs))

