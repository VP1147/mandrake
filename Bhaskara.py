# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147
import utils
import shared
import prop

def BskrMenu():
	utils.LogoType()
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	prop.BskrModeOpt = utils.getch()
	if prop.BskrModeOpt == 'x':
		return 0
	utils.clear()
	utils.ReadTxt(('./design/ModeLogo/logotype'+str(prop.BskrModeOpt)+'.txt')) # Mode logo
	print("<'exit' para sair>")
	print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
	while 1:
		a = utils.randint(shared.IntMin,shared.IntMax)
		b = utils.randint(shared.IntMin,shared.IntMax)
		c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
		if prop.BskrModeOpt == '1':
			drs = utils.SolveDelta(a,b,c) # Calcula delta
			dr = input(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+"). Delta = ")
			if dr == 'exit': return 0
			else: BskrVerify(dr,drs)
		elif prop.BskrModeOpt == '2':
			x1rs,x2rs = utils.SolveBhaskara(a,b,c,shared.FloatPrec) # Calcula x1 e x2
			drs = utils.SolveDelta(a,b,c) # Calcula delta
			print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
			dr = input("Delta = ")
			if dr == 'exit': return 0
			else: BskrVerify(dr,drs)
			x1r = input("x1 = ")
			if x1r == 'exit': return 0 # Se 'x'
			else: BskrVerify(x1r,(x1rs,x2rs)) # Senão, verificação normal
			x2r = input("x2 = ")
			if x2r == 'exit': return 0
			else: BskrVerify(x2r,(x1rs,x2rs))

def BskrVerify(x,r):
	if utils.CheckForFloat(x) == False:
		return 0
	if isinstance(r,tuple) == True: # Caso r for tupla
		r1,r2 = r
		if float(x) == r1 or float(x) == r2: print("Certo")
		else: print("O correto seria "+str(r1)+" ou "+str(r2)+".")
	else:
		if float(x) == r: print("Certo")
		else: print("O correto seria "+str(r)+".")
