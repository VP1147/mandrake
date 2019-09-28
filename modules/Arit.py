# # -*- encoding: utf-8 -*-
import math
import shared
import utils
import prop

def AritMenu():
	utils.LogoType(shared.LogoPath)
	print("1 - Adição")
	print("2 - Subtração")
	print("3 - Multiplicação")
	print("4 - Divisão")
	print("x - Voltar")
	prop.AritOpt = utils.getch()
	if prop.AritOpt == 'x': return 0
	utils.clear()
	print("<'exit' para sair>")
	if prop.AritOpt == '4': print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)")
	while 1:
		if shared.RCount ==  0:
			Signal = Arit() # Para capturar retorno da função 'Arit'
			if Signal == 'exit': 
				return 0 # Se valor for 'exit', sair
		else:
			List = []
			for Count in range(shared.RCount):
				#List[Count] = Arit()
				List.insert(Count,Arit())
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+List[i])
			utils.getch()
			return 0

def Arit():
	x = utils.randint(shared.IntMin,shared.IntMax)
	y = utils.randint(shared.IntMin,shared.IntMax)
	if prop.AritOpt == '1':
		r = input(str(x)+" + "+str(y)+" = ")
		rs = x+y
	elif prop.AritOpt == '2':
		r = input(str(x)+" - "+str(y)+" = ")
		rs = x-y
	elif prop.AritOpt == '3':
		r = input(str(x)+" x "+str(y)+" = ")
		rs = x*y   
	elif prop.AritOpt == '4':
		try: x/y
		except ZeroDivisionError: pass
		r = input(str(x)+" / "+str(y)+" = ")
		rs = round((x/y),shared.FloatPrec)
	if r == 'exit': return 'exit'
	if utils.CheckForFloat(r) == False: # Caso não-float
		return 0
	else: # Caso Float
		if float(r) == rs: 
			print("Certo")
			return 'Certo'
		else: 
			print("O certo seria "+str(rs))
			return 'Errado'

