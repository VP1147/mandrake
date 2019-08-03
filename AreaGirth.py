# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import shared
import prop
import Circle

def AGMenu(GameMenu):
	utils.LogoType()
	print("<---Modo--->")
	print("1 - Círculo")
	print("x - Voltar")
	prop.AGModeOpt = utils.getch()
	if prop.AGModeOpt == 'x':
		return GameMenu()
	elif prop.AGModeOpt == '1':
		Circle.CircleMenu(GameMenu,AGMenu)
	else: return AGMenu(GameMenu)

	
