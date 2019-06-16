# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147
import utils
import shared
import prop
from math import sqrt

def BskrMenu(GameMenu):
    utils.LogoType()
    print("<---Modo--->")
    print("1 - Simples")
    print("2 - Padrão")
    print("x - Voltar")
    prop.BskrModeOpt = utils.getch()
    if prop.BskrModeOpt == 'x':
        return GameMenu()
    BskrModeLogo()
    print("<'exit' para sair>")
    print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
    while 1:
        a = utils.randint(shared.IntMin,shared.IntMax)
        b = utils.randint(shared.IntMin,shared.IntMax)
        c = (utils.randint(shared.IntMin,shared.IntMax))*-1 # Para evitar delta (-)
        if prop.BskrModeOpt == '1':
            BskrMode1(GameMenu,BskrMenu,a,b,c)
        elif prop.BskrModeOpt == '2':
            BskrMode2(GameMenu,BskrMenu,a,b,c)

def BskrMode1(GameMenu,BskrMenu,a,b,c): # Modo simples
    rs = (b**2)-4*a*c # Calcula delta
    r = input(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+"). Delta = ")
    if utils.CheckForFloat(r) == False: # Verificação para float
        if r == 'exit':
            return BskrMenu(GameMenu)
        else:
            return BskrMode1(BskrMenu,GameMenu,a,b,c)
    else:
        if float(r) == rs:
            print("Certo")
        else:
            print("O certo seria "+str(rs))

def BskrMode2(GameMenu,BskrMenu,a,b,c): # Modo padrão
    rs1 = round(float(((b*-1)+sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec) # Calcula x1
    rs2 = round(float(((b*-1)-sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec) # Calcula x2
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    r1 = input("x1 = ")
    r2 = input("x2 = ")
    if utils.CheckForFloat(r1) == False or utils.CheckForFloat(r2) == False:
        if r1 == 'exit' or r2 == 'exit':
            return BskrMenu(GameMenu)
        else:
            return BskrMode2(GameMenu,BskrMenu,a,b,c)
    else:
        if (float(r1) == rs1 and float(r2) == rs2) or (float(r1) == rs2 and float(r2) == rs2):
            print("Certo")
        else:
            print("O certo seria "+str(rs1)+" e "+str(rs2))
            
def BskrModeLogo(): # Mode-based logo
    utils.clear()
    with open('./design/ModeLogo/logotype'+str(prop.BskrModeOpt)+'.txt') as txt:
        print(txt.read())
