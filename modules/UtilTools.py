# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared, utils

def UtilToolsMenu():
	utils.LogoType(shared.LogoPath)
	print("1 - Verificador de divisibilidade")
	print("x - Voltar")
	if utils.getch == 'x': return 0
	elif utils.getch() == '1':
		DivTool()

def DivTool():
	utils.LogoType(shared.LogoPath)
	num = int(input("Número: "))
	if num > 9999999: 
		print("<Aviso: Número grande, operação pode demorar>")
	List = utils.DivCheck(num)
	print(str(num)+" é divisível por: "+str(List))
	utils.getch()
	return 0
