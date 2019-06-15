# Library for Mandrake | By vp1147
import utils
import shared
import prop
from math import sqrt

def BskrMenu(GameMenu):
    utils.LogoType()
    print("1 - Simples")
    print("2 - Padrão")
    print("x - Voltar")
    prop.BskrModeOpt = utils.getch()
    if prop.BskrModeOpt == 'x':
        return GameMenu()
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
    print(a,"*x^2 + ",b,"*x + (",c,"). Delta = ")
    r = input()
    if utils.CheckForFloat(r) == False: # Verificação para float
        if r == 'exit':
            return BskrMenu(GameMenu)
        else:
            return BskrMode1(BskrMenu,GameMenu,a,b,c)
    else:
        if float(r) == rs:
            print("Certo")
        else:
            print("O certo seria ",rs)

def BskrMode2(GameMenu,BskrMenu,a,b,c): # Modo padrão
    rs1 = round(float(((b*-1)+sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec)
    rs2 = round(float(((b*-1)-sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec)
    print(a,"*x^2 + ",b,"*x + (",c,")")
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
            print("O certo seria",rs1,"e",rs2)
    
