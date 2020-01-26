# # -*- encoding: utf-8 -*-
import shared as s
import utils as u

def AritMenu():
	u.LogoType(s.LogoPath)
	print("1 - Adição")
	print("2 - Subtração")
	print("3 - Multiplicação")
	print("4 - Divisão")
	print("x - Voltar")
	Opt = u.getch()
	if Opt == 'x': return 0
	u.clear()
	print("<'exit' para sair>")
	if Opt == '4': print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)")
	while 1:
		if s.RCount ==  0:
			Signal = Arit(Opt) # Para capturar retorno da função 'Arit'
			if Signal == 'exit': 
				return 0 # Se valor for 'exit', sair
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,Arit(Opt))
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+List[i])
			u.getch()
			return 0

def Arit(Opt):
	x = u.randint(s.IntMin,s.IntMax)
	y = u.randint(s.IntMin,s.IntMax)
	if Opt == '1': r = input(str(x)+" + "+str(y)+" = ") ; rs = x+y
	elif Opt == '2': r = input(str(x)+" - "+str(y)+" = ") ; rs = x-y
	elif Opt == '3': r = input(str(x)+" x "+str(y)+" = ") ; rs = x*y   
	elif Opt == '4':
		try: x/y
		except ZeroDivisionError: pass
		r = input(str(x)+" / "+str(y)+" = ")
		rs = round((x/y),s.FloatPrec)
	return u.CheckAnswer(rs,r)
