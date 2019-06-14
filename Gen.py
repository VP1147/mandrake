import os
import shared
import utils
from math import sqrt
import prop

def GenMenu(InitMenu):
    utils.LogoType()
    print("1 - Teorema de Pitágoras")
    print("x - Sair")
    GenMenuOpt = utils.getch()
    if GenMenuOpt == '1':
        PitagorasGen()
        return GenMenu(InitMenu)
    elif GenMenuOpt == 'x':
        return InitMenu()
    else:
        return GenMenu(InitMenu)
        
def PitagorasGen():
    utils.LogoType()
    print("Valor mínimo das variáveis: ",shared.IntMin)
    print("Valor máximo das variáveis: ",shared.IntMax)
    print("Precisão de decimais: ",shared.FloatPrec)
    prop.GenPtgsModeOpt = str(input("Modo (1-2)(Ver manual): "))
    GenQuant = int(input("Quantidade para gerar: "))
    for i in range(0,GenQuant):
        x = utils.randint(shared.IntMin,shared.IntMax)
        y = utils.randint(shared.IntMin,shared.IntMax)
        z = utils.randint(shared.IntMin,shared.IntMax)
        if prop.GenPtgsModeOpt == '1':
            GenPtgsMode1(x,y,z)
        elif prop.GenPtgsModeOpt == '2':
            GenPtgsMode2(x,y,z)
    utils.getch()

def GenPtgsMode1(x,y,z): # Modo simples
    if x >= y and x >= z: # Caso x maior
        rs = (y**2)+(z**2)
        print("c1 = ",y,", c2 = ",z,", hip = raiz quadrada de ",rs)
    elif y >= x and y >= z: # Caso y maior
        rs = (x**2)+(z**2)
        print("c1 = ",x,", c2 = ",z,", hip = raiz quadrada de ",rs)
    elif z >= x and z >= y: # Caso z maior
        rs = (x**2)+(y**2)
        print("c1 = ",x,", c2 = ",y,", hip = raiz quadrada de ",rs)

def GenPtgsMode2(x,y,z): # Modo padrão
    if x >= y and x >= z: # Caso x maior
        rs = round(sqrt((y**2)+(z**2)),shared.FloatPrec)
        print("c1 = ",y,", c2 = ",z,", hip = ",rs)
    elif y >= x and y >= z: # Caso y maior
        rs = round(sqrt((x**2)+(z**2)),shared.FloatPrec)
        print("c1 = ",x,", c2 = ",z,", hip = ",rs)
    elif z >= x and z >= y: # Caso z maior
        rs = round(sqrt((x**2)+(y**2)),shared.FloatPrec)
        print("c1 = ",x,", c2 = ",y,", hip = ",rs)
