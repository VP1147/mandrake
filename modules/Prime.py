# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils as u
import shared as s

def PrimeMenu():
	u.clear()
	print("< Números Primos >")
	print("<'exit' para sair>")
	print("<'s' - É primo / 'n'- Ñ é primo>")
	while 1:
		if s.RCount == 0:
			Signal = Prime()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,Prime())
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+List[i])
			u.getch()
			return 0

def Prime():
	RList = []
	a = u.randint(1,s.IntMax)
	return PrimeVerify(input(str(a)+" é primo? "),a)

def PrimeVerify(r,x):
	if r == 's' and u.CheckForPrime(x) == True or r == 'n' and u.CheckForPrime(x) == False:
		print("Certo")
		return 'Certo'
	elif r == 's' and u.CheckForPrime(x) == False or r == 'n' and u.CheckForPrime(x) == True:
		print("Errado")
		return 'Errado'
	elif s.RCount == 0 and r == 'exit': return 'exit'
	else: return 'Nula'