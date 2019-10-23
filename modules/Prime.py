# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import utils, shared, prop

def PrimeMenu():
	utils.clear()
	print("<'exit' para sair>")
	print("<'S' - É primo / 'n'- Ñ é primo>")
	while 1:
		if shared.RCount == 0:
			Signal = Prime()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(shared.RCount):
				List.insert(Count,Prime())
			print("-- Concluido --")
			for i in range(shared.RCount):
				print(str((i+1))+" - "+List[i])
			utils.getch()
			return 0

def Prime():
	RList = []
	a = utils.randint(shared.IntMin,shared.IntMax)
	return PrimeVerify(input(str(a)+" é primo? "),a)
	
def PrimeVerify(r,x):
	if r == 's' and utils.CheckForPrime(x) == True or r == 'n' and utils.CheckForPrime(x) == False:
		print("Certo")
		return 'Certo'
	elif r == 's' and utils.CheckForPrime(x) == False or r == 'n' and utils.CheckForPrime(x) == True:
		print("Errado")
		return 'Errado'
	else:
		print(r+", "+str(utils.CheckForPrime(x)))
		return 'Nula'
