# # -*- encoding: utf-8 -*-
# Mandrake by vp1147 -- 05/03/19 -->

from random import randint
import utils # utils.py file
import Pit
import Gen
import os
import shared
import JsonFunctions
import Bhaskara
import FQuad
import AreaGirth
 
def InitMenu():
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
    elif InitMenuOpt == '2': Gen.GenMenu(InitMenu)
    elif InitMenuOpt == '3': SettingsMenu()
    elif InitMenuOpt == '4': # call man page
        utils.LogoType()
        utils.ReadTxt('man.txt')
        utils.getch()
        return InitMenu()
    elif InitMenuOpt == '5':
        utils.LogoType()
        utils.ReadTxt('info.txt')
        utils.getch()
        return InitMenu()
    elif InitMenuOpt == '6':
        utils.LogoType()
        utils.ReadTxt('LICENSE')
        utils.getch()
        return InitMenu()
    elif InitMenuOpt == 'x': # exit program
        utils.clear()
        utils.exit()
    else:
        return InitMenu()

def SettingsMenu():
    utils.LogoType()
    print("1 - Parâmetros de geração de números")
    print("2 - Precisão de decimais")
    print("x - Voltar")
    SettingsMenuOpt = utils.getch()
    if SettingsMenuOpt == '1':
        utils.LogoType()
        shared.IntMin = int(input("Definir tamanho mínimo: "))
        shared.IntMax = int(input("Definir tamanho máximo: "))
        if shared.IntMin > shared.IntMax:
            return SettingsMenu()
        JsonFunctions.SaveAllFromCfg(SettingsMenu)
    elif SettingsMenuOpt == '2':
        utils.LogoType()
        try:
            shared.FloatPrec = int(input("Casas decimais de precisão [Default:1]: "))
        except ValueError:
            return SettingsMenu()
        JsonFunctions.SaveAllFromCfg(SettingsMenu)
        return SettingsMenu()
    elif SettingsMenuOpt == 'x':
        return InitMenu()
    else:
        return SettingsMenu()

def GameMenu():
    utils.LogoType()
    print("1 - Aritmética")
    print("2 - Equação quadrática")
    print("3 - Teorema de Pitágoras")
    print("4 - Função Quadrática")
    print("5 - Área e perímetro")
    print("x - Voltar")
    GameMenuOpt = utils.getch()
    if GameMenuOpt == '1':
        import Arit
        Arit.AritMenu(GameMenu)
    if GameMenuOpt == '3':
        Pit.PtgsMenu(GameMenu)
    elif GameMenuOpt == '2':
        Bhaskara.BskrMenu(GameMenu)
    elif GameMenuOpt == '4':
        FQuad.QuadFMenu(GameMenu)
    elif GameMenuOpt == '5':
    	AreaGirth.AGMenu(GameMenu)
    elif GameMenuOpt == 'x':
        return InitMenu()
    else:
        return GameMenu()

# --- Game Start --- #

utils.LogoGen()
InitMenu()
