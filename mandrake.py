# # -*- encoding: utf-8 -*-
# Mandrake by vp1147 -- 05/03/19 -->

# External libs
from random import randint
import os
import sys

# Own libs
sys.path.append('./modules')
import utils, Pit, Gen, shared, JsonFunctions, Bhaskara, FQuad, Area, Arit, Prime, UtilTools

def GameMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		print("1 - Aritmética")
		print("2 - Equação quadrática")
		print("3 - Teorema de Pitágoras")
		print("4 - Função Quadrática")
		print("5 - Área")
		print("6 - Números primos")
		print("x - Voltar")
		GameMenuOpt = utils.getch()
		if GameMenuOpt == '1': Arit.AritMenu()
		elif GameMenuOpt == '2': Bhaskara.BskrMenu()
		elif GameMenuOpt == '3': Pit.PtgsMenu()
		elif GameMenuOpt == '4': FQuad.QuadFMenu()
		elif GameMenuOpt == '5': Area.AreaMenu()
		elif GameMenuOpt == '6': Prime.PrimeMenu()
		elif GameMenuOpt == 'x': return 0 # Finaliza a função
    	# Código reinicia

def SettingsMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		print("1 - Parâmetros de geração de números (Definido: "+str(shared.IntMin)+" - "+str(shared.IntMax)+")")
		print("2 - Precisão de decimais (Definido: "+str(shared.FloatPrec)+")")
		print("3 - Contagem de resoluções (Definido: "+str(shared.RCount)+")")
		print("x - Voltar")
		SettingsMenuOpt = utils.getch()
		if SettingsMenuOpt == '1':
			utils.LogoType(shared.LogoPath)
			shared.IntMin = int(input("Definir tamanho mínimo: "))
			shared.IntMax = int(input("Definir tamanho máximo: "))
		elif SettingsMenuOpt == '2':
			utils.LogoType(shared.LogoPath)
			shared.FloatPrec = int(input("Casas decimais de precisão (Default:1): "))
			JsonFunctions.SaveAllFromCfg(SettingsMenu)
			return 0
		elif SettingsMenuOpt == '3':
			utils.LogoType(shared.LogoPath)
			shared.RCount = int(input("Limite de resoluções (0 - Desabilitar limite): "))
		elif SettingsMenuOpt == 'x':
			return 0

utils.LogoGen()
while 1:
	utils.LogoType(shared.LogoPath)
	print("1 - Jogar")
	print("2 - Gerador")
	print("3 - Ferramentas")
	print("4 - Config")
	print("5 - Manual")
	print("6 - Sobre")
	print("7 - Licença")
	print("x - Sair")
	InitMenuOpt = utils.getch()
	if InitMenuOpt == '1': GameMenu()
	elif InitMenuOpt == '2': Gen.GenMenu()
	elif InitMenuOpt == '3' : UtilTools.UtilToolsMenu()
	elif InitMenuOpt == '4': SettingsMenu()
	elif InitMenuOpt == '5': # call man page
		utils.LogoType(shared.LogoPath)
		utils.ReadTxt('./data/man.txt')
		utils.getch()
	elif InitMenuOpt == '6':
		utils.LogoType(shared.LogoPath)
		utils.ReadTxt('./data/info.txt')
		utils.getch()
	elif InitMenuOpt == '7':
		utils.LogoType(shared.LogoPath)
		utils.ReadTxt('LICENSE')
		utils.getch()
	elif InitMenuOpt == 'x':
		JsonFunctions.SaveAllFromCfg(SettingsMenu) # Salva as alterações 
		utils.clear()
		utils.exit()
    # Código reinicia

