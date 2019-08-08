# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import shared
import prop
import Circle

def AreaMenu(GameMenu):
	utils.LogoType()
	print("<---Modo--->")
	print("1 - Círculo")
	#print("2 - Quadrado")
	#print("3 - Triângulo")
	print("x - Voltar")
	prop.AreaModeOpt = utils.getch()
	if prop.AreaModeOpt == 'x':
		return GameMenu()
	elif prop.AreaModeOpt == '1':
		Circle.CircleMenu(GameMenu,AreaMenu)
	else: return AreaMenu(GameMenu)

	
