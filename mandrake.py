# # -*- encoding: utf-8 -*-
# Mandrake by vp1147 -- 05/03/19 -->

# External libs
from random import randint
import sys

# Own libs
sys.path.append('./modules')
import utils, Gen, shared, JsonFunctions, Area, Arit, Prime, UtilTools, Functions, Equations

def GameMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		print("1 - Aritmética")
		print("2 - Equações")
		print("3 - Funções")
		print("4 - Geometria")
		print("5 - Números primos")
		print("x - Voltar")
		Opt = utils.getch()
		if Opt == '1': Arit.AritMenu()
		elif Opt == '2': EqMenu()
		elif Opt == '3': FunctionsMenu()
		elif Opt == '4': Area.AreaMenu()
		elif Opt == '5': Prime.PrimeMenu()
		elif Opt == 'x': return 0 # Finaliza a função
    	# Código reinicia

def SettingsMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		print("1 - Parâmetros de geração de números (Definido: "+str(shared.IntMin)+" - "+str(shared.IntMax)+")")
		print("2 - Precisão de decimais (Definido: "+str(shared.FloatPrec)+")")
		print("3 - Contagem de resoluções (Definido: "+str(shared.RCount)+")")
		print("x - Voltar")
		Opt = utils.getch()
		if Opt == '1':
			utils.LogoType(shared.LogoPath)
			shared.IntMin = int(input("Definir tamanho mínimo: "))
			shared.IntMax = int(input("Definir tamanho máximo: "))
		elif Opt == '2':
			utils.LogoType(shared.LogoPath)
			shared.FloatPrec = int(input("Casas decimais de precisão (Default:1): "))
			JsonFunctions.SaveAllFromCfg(SettingsMenu)
			return 0
		elif Opt == '3':
			utils.LogoType(shared.LogoPath)
			shared.RCount = int(input("Limite de resoluções (0 - Desabilitar limite): "))
		elif Opt == 'x':
			return 0

def FunctionsMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		# print("1 - Função linear [f(x) = ax]") # SID
		print("1 - Função Quadrática [f(x) = ax\N{SUPERSCRIPT TWO} + bx + c]")
		print("x - Voltar")
		Opt = utils.getch()
		# if Opt == '1':
		if Opt == '1': Functions.QuadFMenu()
		elif Opt == 'x': return 0

def EqMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		# print("1 - Equação de 1° Grau") # SID
		print("1 - Equação de 2° Grau [ax\N{SUPERSCRIPT TWO} + bx + c = 0]")
		print("2 - Teorema de Pitágoras")
		print("x - Voltar")
		Opt = utils.getch()
		# if Opt == '1': 
		if Opt == '1': Equations.BskrMenu()
		elif Opt == '2': Equations.PtgsMenu()
		elif Opt == 'x': return 0
	
utils.LogoGen()
while 1:
	utils.LogoType(shared.LogoPath)
	print("1 - Jogar")
	print("2 - Gerador")
	print("3 - Ferramentas")
	print("4 - Config")
	print("5 - Sobre")
	print("x - Sair")
	Opt = utils.getch()
	if Opt == '1': GameMenu()
	elif Opt == '2': Gen.GenMenu()
	elif Opt == '3' : UtilTools.UtilToolsMenu()
	elif Opt == '4': SettingsMenu()
	elif Opt == '5':
		utils.LogoType(shared.LogoPath)
		utils.ReadTxt('./data/info.txt')
		utils.getch()
	elif Opt == 'x':
		JsonFunctions.SaveAllFromCfg(SettingsMenu) # Salva as alterações 
		utils.clear()
		utils.exit()
    # Código reinicia

