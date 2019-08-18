# # -*- encoding: utf-8 -*-
import math
import shared
import utils
import prop

def AritMenu():
	utils.LogoType()
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
		x = utils.randint(shared.IntMin,shared.IntMax)
		y = utils.randint(shared.IntMin,shared.IntMax)
		if prop.AritOpt == '1':
			r = input(str(x)+" + "+str(y)+" = ")
			if r == 'exit': return 0
			rs = x+y
		elif prop.AritOpt == '2':
			r = input(str(x)+" - "+str(y)+" = ")
			if r == 'exit': return 0
			rs = x-y
		elif prop.AritOpt == '3':
			r = input(str(x)+" x "+str(y)+" = ")
			if r == 'exit': return 0
			rs = x*y   
		elif prop.AritOpt == '4':
			try: x/y
			except ZeroDivisionError: pass
			r = input(str(x)+" / "+str(y)+" = ")
			if r == 'exit': return 0
			rs = round((x/y),shared.FloatPrec)
		if utils.CheckForFloat(r) == False: # Caso não-float
			return 0
		else: # Caso Float
			if float(r) == rs: print("Certo")
			else: print("O certo seria "+str(rs))


def Arit():
	x = utils.randint(shared.IntMin,shared.IntMax)
	y = utils.randint(shared.IntMin,shared.IntMax)
	if prop.AritOpt == '1':
		r = input(str(x)+" + "+str(y)+" = ")
		if r == 'exit': return 0
		rs = x+y
	elif prop.AritOpt == '2':
		r = input(str(x)+" - "+str(y)+" = ")
		if r == 'exit': return 0
		rs = x-y
	elif prop.AritOpt == '3':
		r = input(str(x)+" x "+str(y)+" = ")
		if r == 'exit': return 0
		rs = x*y   
	elif prop.AritOpt == '4':
		try: x/y
		except ZeroDivisionError: pass
		r = input(str(x)+" / "+str(y)+" = ")
		if r == 'exit': return 0
		rs = round((x/y),shared.FloatPrec)
	if utils.CheckForFloat(r) == False: # Caso não-float
		return 0
	else: # Caso Float
		if float(r) == rs: print("Certo")
		else: print("O certo seria "+str(rs))

