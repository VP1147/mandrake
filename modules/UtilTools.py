# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared as s
import utils as u

def UtilToolsMenu():
	u.LogoType(s.LogoPath)
	print("1 - Verificador de divisibilidade")
	print("2 - Cálculo de π")
	print("3 - Média aritmética")
	print("x - Voltar")
	Opt = u.getch()
	if Opt == 'x': return 0
	elif Opt == '1': DivTool()
	elif Opt == '2': PiTool()
	elif Opt == '3': AritMeanTool()

def DivTool():
	u.LogoType(s.LogoPath)
	num = int(input("Número: "))
	if num > 9999999: 
		print("<Aviso: Número grande, operação pode demorar>")
	List = u.DivCheck(num)
	print(str(num)+" é divisível por: "+str(List))
	u.getch()
	return 0

def PiTool():
	u.LogoType(s.LogoPath)
	prec = int(input("Precisão: "))
	if prec > 9999:
		print("<Aviso: Número grande, operação pode demorar>")
	print("π ~= "+str(u.Chudnovsky(prec, prec)))
	u.getch()
	return 0

def AritMeanTool():
	u.LogoType(s.LogoPath)
	print("<Valores separados por vírgula>")
	num = input("Valores: ")
	print(u.AritMean(num.split(',')))
	u.getch()
	return 0
