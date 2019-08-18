# # -*- encoding: utf-8 -*-
# Mandrake by vp1147 -- 05/03/19 -->

# External libs
from random import randint
import os

# Own libs
import utils, Pit, Gen, shared, JsonFunctions, Bhaskara, FQuad, Area, Arit

def GameMenu():
	while 1:
		utils.LogoType()
		print("1 - Aritmética")
		print("2 - Equação quadrática")
		print("3 - Teorema de Pitágoras")
		print("4 - Função Quadrática")
		print("5 - Área")
		print("x - Voltar")
		GameMenuOpt = utils.getch()
		if GameMenuOpt == '1': Arit.AritMenu()
		elif GameMenuOpt == '2': Bhaskara.BskrMenu()
		elif GameMenuOpt == '3': Pit.PtgsMenu()
		elif GameMenuOpt == '4': FQuad.QuadFMenu()
		elif GameMenuOpt == '5': Area.AreaMenu()
		elif GameMenuOpt == 'x': return 0 # Finaliza a função
    	# Código reinicia

def SettingsMenu():
	while 1:
		utils.LogoType()
		print("1 - Parâmetros de geração de números")
		print("2 - Precisão de decimais")
		print("x - Voltar")
		SettingsMenuOpt = utils.getch()
		if SettingsMenuOpt == '1':
			utils.LogoType()
			shared.IntMin = int(input("Definir tamanho mínimo: "))
			shared.IntMax = int(input("Definir tamanho máximo: "))
			if shared.IntMin <= shared.IntMax:
				JsonFunctions.SaveAllFromCfg(SettingsMenu)
				return 0
		elif SettingsMenuOpt == '2':
			utils.LogoType()
			shared.FloatPrec = int(input("Casas decimais de precisão [Default:1]: "))
			JsonFunctions.SaveAllFromCfg(SettingsMenu)
			return 0
		elif SettingsMenuOpt == 'x':
			return 0

utils.LogoGen()
while 1:
    utils.LogoType()
    print("1 - Jogar")
    print("2 - Gerador")
    print("3 - Config")
    print("4 - Manual")
    print("5 - Sobre")
    print("6 - Licença")
    print("x - Sair")
    InitMenuOpt = utils.getch()
    if InitMenuOpt == '1': GameMenu()
    elif InitMenuOpt == '2': Gen.GenMenu()
    elif InitMenuOpt == '3': SettingsMenu()
    elif InitMenuOpt == '4': # call man page
        utils.LogoType()
        utils.ReadTxt('man.txt')
        utils.getch()
    elif InitMenuOpt == '5':
        utils.LogoType()
        utils.ReadTxt('info.txt')
        utils.getch()
    elif InitMenuOpt == '6':
        utils.LogoType()
        utils.ReadTxt('LICENSE')
        utils.getch()
    elif InitMenuOpt == 'x':
        utils.clear()
        utils.exit()
    # Código reinicia

