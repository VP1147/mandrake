# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared, utils

def UtilToolsMenu():
	utils.LogoType(shared.LogoPath)
	print("1 - Verificador de divisibilidade")
	print("2 - Cálculo de π")
	print("3 - Média aritmética")
	print("x - Voltar")
	Opt = utils.getch()
	if Opt == 'x': return 0
	elif Opt == '1': DivTool()
	elif Opt == '2': PiTool()
	elif Opt == '3': AritMeanTool()

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

def AritMeanTool():
	utils.LogoType(shared.LogoPath)
	print("<Valores separados por vírgula>")
	num = input("Valores: ")
	print(utils.AritMean(num.split(',')))
	utils.getch()
	return 0
