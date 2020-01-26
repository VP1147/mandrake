# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils as u
import shared as s

def AreaMenu():
	u.LogoType(s.LogoPath)
	print("<---Modo--->")
	print("1 - Círculo")
	print("2 - Quadrado")
	print("3 - Triângulo")
	print("x - Voltar")
	Opt = u.getch()
	if Opt == 'x':
		return 0
	u.clear()
	print("<'exit' para sair>")
	print("<Precisão de "+str(s.FloatPrec)+" decimal(is)>")
	while 1:
		if s.RCount == 0:
			Signal = Area(Opt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,Area(Opt))
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+List[i])
			u.getch()
			return 0

def Area(Opt):
	if Opt == '1':
		while 1:
			Rad,Pi,Area = u.GenCircle(1,s.IntMax,s.FloatPrec)
			r = input("Raio = "+str(Rad)+" | Área = ")
			return u.CheckAnswer(Area,r)
	elif Opt == '2':
		while 1:
			Side,Area = u.GenQuad(1,s.IntMax,s.FloatPrec)
			r = input("Lado = "+str(Side)+" | Área = ")
			return u.CheckAnswer(Area,r)
	elif Opt == '3':
		while 1:
			Base,Height,Area = u.GenTriangle(1,s.IntMax,s.FloatPrec)
			r = input("Base = "+str(Base)+" | Altura = "+str(Height)+" | Área = ")
			return u.CheckAnswer(Area,r)


