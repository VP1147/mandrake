# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils
import prop
import shared

def CircleMenu(GameMenu,AGMenu):
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		CircleAG(GameMenu,AGMenu)

def CircleAG(GameMenu,AGMenu):
	if utils.randint(0,1) == 0: # Caso funções de perímetro
		if utils.randint(0,1) == 0: VarMode = 'R'
		else: VarMode = 'C'
		Rad,Circ,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec,VarMode)
		if VarMode == 'C': # Caso raio incognita 
			r = input("Circunferência = "+str(Circ)+" | Raio = ")
			rs = Rad
		elif VarMode == 'R': # Caso perímetro incognita
			r = input("Raio = "+str(Rad)+" | Circunferência = ")
			rs = Circ
	else: # Caso funcões de área
		Rad,Circ,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec,'R')
		r = input("Raio = "+str(Rad)+" | Área = ")
		rs = Area
	if utils.CheckForFloat(r) == False: # Verificação para float
		if r == 'exit': return AGMenu(GameMenu)
		else: return CircleAG(GameMenu, AGMenu)
	else:
		if float(r) == rs: print("Certo")
		else: print("O certo seria "+str(rs))

