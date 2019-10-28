# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared, utils

def UtilToolsMenu():
	utils.LogoType(shared.LogoPath)
	print("1 - Verificador de divisibilidade")
	print("2 - Cálculo de π")
	print("x - Voltar")
	UtilsToolOpt = utils.getch()
	if UtilsToolOpt == 'x': return 0
	elif UtilsToolOpt == '1': DivTool()
	elif UtilsToolOpt == '2': PiTool()

def DivTool():
	utils.LogoType(shared.LogoPath)
	num = int(input("Número: "))
	if num > 9999999: 
		print("<Aviso: Número grande, operação pode demorar>")
	List = utils.DivCheck(num)
	print(str(num)+" é divisível por: "+str(List))
	utils.getch()
	return 0

def PiTool():
	utils.LogoType(shared.LogoPath)
	prec = int(input("Precisão: "))
	if prec > 9999:
		print("<Aviso: Número grande, operação pode demorar>")
	print("π ~= "+str(utils.Chudnovsky(prec, prec)))
	utils.getch()
	return 0
