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
	utils.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		if shared.RCount == 0:
			Signal = Area(prop.AreaModeOpt)
			if Signal == 'exit': return 0
			else: pass
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Area(prop.AreaModeOpt))
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+List[i])
			utils.getch()
			return 0

def Area(Opt):
	if Opt == '1':
		while 1:
			Rad,Pi,Area = utils.GenCircle(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Raio = "+str(Rad)+" | Área = ")
			if r == 'exit': return 'exit'
			else: return CheckAnswer(Area,r)
	elif Opt == '2':
		while 1:
			Side,Area = utils.GenQuad(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Lado = "+str(Side)+" | Área = ")
			if r == 'exit': return 'exit'
			else: return CheckAnswer(Area,r)
	elif Opt == '3':
		while 1:
			Base,Height,Area = utils.GenTriangle(shared.IntMin,shared.IntMax,shared.FloatPrec)
			r = input("Base = "+str(Base)+" | Altura = "+str(Height)+" | Área = ")
			if r == 'exit': return 'exit'
			else: return CheckAnswer(Area,r)

def CheckAnswer(rs,r):
	if utils.CheckForFloat(r) == False: # Caso não-float
		return 'Nula'
	else: # Caso Float
		if float(r) == rs: 
			print("Certo")
			return 'Certo'
		else: 
			print("O certo seria "+str(rs))
			return 'Errado'

