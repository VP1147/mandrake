# # -*- encoding: utf-8 -*-
# Mandrake by vp1147 -- 05/03/19 -->

from random import randint
import utils # utils.py file
import pitagoras # pitagoras.py file
import gen
import os
import shared
import JsonFunctions

def InitMenu():
    utils.LogoType()
    print("1 - Jogar")
    print("2 - Gerador")
    print("3 - Config")
    print("4 - Manual")
    print("5 - Sobre")
    print("x - Sair")
    initMenuOpt = utils.getch() # call getch from utils.py
    if initMenuOpt == '1':
        GameMenu()

    elif initMenuOpt == '2': # call generator
        gen.GenMenu(InitMenu)

    elif initMenuOpt == '3': # call settings menu
        SettingsMenu()

    elif initMenuOpt == '4': # call man page
        utils.LogoType()
        os.system("cat man.txt")
        utils.getch()
        return InitMenu()

    elif initMenuOpt == '5':
        utils.LogoType()
        os.system("cat info.txt")
        utils.getch()
        return InitMenu()
    elif initMenuOpt == 'x': # exit program
        utils.clear()
        exit()

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
    print("2 - Equação")
    print("3 - Teorema de Pitágoras")
    print("x - Voltar")
    GameMenuOpt = utils.getch()
    if GameMenuOpt == '1':
        import Arit
        Arit.AritMenu(GameMenu)
    if GameMenuOpt == '3':
        import pitagoras # pitagoras.py file
        pitagoras.PitagorasMenu(GameMenu)
    elif GameMenuOpt == '2':
        Eq.EqMenu(GameMenu)
    elif GameMenuOpt == 'x':
        return InitMenu()
    else:
        return GameMenu()

utils.LogoGen()
InitMenu()
