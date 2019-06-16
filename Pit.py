# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147
import utils
import shared
import prop
from math import sqrt

def PtgsMenu(GameMenu):
    utils.LogoType()
    print("<---Modo--->")
    print("1 - Simples")
    print("2 - Padrão")
    print("x - Voltar p/ Inicio")
    prop.PtgsModeOpt = utils.getch()
    if prop.PtgsModeOpt == 'x':
        return GameMenu()
    PitModeLogo() # Call mode-based logotype func
    print("<'exit' para sair>")
    print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
    while 1:
        x = utils.randint(shared.IntMin,shared.IntMax)
        y = utils.randint(shared.IntMin,shared.IntMax)
        z = utils.randint(shared.IntMin,shared.IntMax)
        if prop.PtgsModeOpt == '1':
            PtgsMode1(PtgsMenu,GameMenu,x,y,z)
        elif prop.PtgsModeOpt == '2':
            PtgsMode2(PtgsMenu,GameMenu,x,y,z)

def PtgsMode1(PtgsMenu,GameMenu,x,y,z): # Modo simples
    if x >= y and x >= z: # Caso x maior
        print("c1 = "+str(y)+", c2 = "+str(z)+", hip = raiz quadrada de ")
        rs = (y**2)+(z**2)
        r = input()
    elif y >= x and y >= z: # Caso y maior
        print("c1 = "+str(x)+", c2 = "+str(z)+", hip = raiz quadrada de ")
        rs = (x**2)+(z**2)
        r = input()
    elif z >= x and z >= y: # Caso z maior
        print("c1 = "+str(x)+", c2 = "+str(y)+", hip = raiz quadrada de ")
        rs = (x**2)+(y**2)
        r = input()
    if utils.CheckForFloat(r) == False: # Verificação para float
        if r == 'exit':
            return PtgsMenu(GameMenu)
        else:
            return PtgsMode1(PtgsMenu,GameMenu,x,y,z)
    else:
        if float(r) == rs:
            print("Certo")
        else: 
            print("O certo seria "+str(rs))

def PtgsMode2(PtgsMenu,GameMenu,x,y,z): # Modo padrão
    if x >= y and x >= z: # Caso x maior
        print("c1 = "+str(y)+", c2 = "+str(z)+", hip = ")
        rs = round(sqrt((y**2)+(z**2)),shared.FloatPrec)
        r = input()
    elif y >= x and y >= z: # Caso y maior
        print("c1 = "+str(x)+", c2 = "+str(z)+", hip = ")
        rs = round(sqrt((x**2)+(z**2)),shared.FloatPrec)
        r = input()
    elif z >= x and z >= y: # Caso z maior
        print("c1 = "+str(x)+", c2 = "+str(y)+", hip = ")
        rs = round(sqrt((x**2)+(y**2)),shared.FloatPrec)
        r = input()
    if utils.CheckForFloat(r) == False:
        if r == 'exit':
            return PtgsMenu(GameMenu)
        else:
            return PtgsMode2(PtgsMenu,GameMenu,x,y,z)
    else:
        if float(r) == rs:
            print("Certo")
        else: 
            print("O certo seria "+str(rs))

def PitModeLogo(): # Mode-based logo
    utils.clear()
    with open('./design/ModeLogo/logotype'+str(prop.PtgsModeOpt)+'.txt') as txt:
        print(txt.read())
