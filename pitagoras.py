# library for Mandrake | by vp1147
# DEPRECATED

import utils # utils.py lib
import math
import shared
import JsonFunctions
import prop

def PitagorasMenu(GameMenu): # def pitagorasMenu with GameMenu function added
    utils.LogoType()
    print("<---- Modos ---->")
    print("1 - Simples")
    print("2 - Padrão")
    print("x - Voltar p/ Inicio")
    prop.PitagorasModeOpt = utils.getch()
    if prop.PitagorasModeOpt == 'x':
        return GameMenu()
    utils.LogoType()
    print("1 - Variável -> hip (padrão)")
    print("2 - Variável -> c1")
    print("3 - Variável -> c2")
    print("x - Voltar p/ Inicio")
    prop.VarArrangeOpt = utils.getch()
    if prop.VarArrangeOpt == 'x':
        return PitagorasMenu(GameMenu)
    utils.clear()
    PitagorasModeLogo()
    print("<'exit' para sair>")
    print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)>")
    while 1:
        pitagoras(GameMenu)

def pitagoras(GameMenu):
    x = utils.randint(shared.IntMin,shared.IntMax)
    y = utils.randint(shared.IntMin,shared.IntMax)
    if prop.PitagorasModeOpt == '1':
        if prop.VarArrangeOpt == '1':
            if int(pow(x,2)+pow(y,2)) >= 0:
                z = str(input("Sendo c1 = "+str(x)+" e c2 = "+str(y)+", hip = à raiz quadrada de : "))
                if utils.CheckForFloat(z) == False: # If 'z' isn't a int
                    if z == 'exit':
                        return PitagorasMenu(GameMenu)
                    else:
                        return pitagoras(GameMenu)
                else: # If 'z' is a int
                    if float(z) == (pow(x,2)+pow(y,2)): # If correct
                        print("Correto")
                    else:
                        print("O certo seria "+str(pow(x,2)+pow(y,2)))
        elif prop.VarArrangeOpt == '2':
            if int(pow(y,2))+(int(pow(x,2))*int(-1)) >= 0:
                z = str(input("Sendo c2 = "+str(x)+" e hip = "+str(y)+", c1 = à raiz quadrada de : "))
                if utils.CheckForFloat(z) == False:
                    if z == 'exit':
                        return PitagorasMenu(GameMenu)
                    else:
                        return pitagoras(GameMenu)
                else:
                    if float(z) == (pow(y,2))+(int(pow(x,2))*int(-1)):
                        print("Correto")
                    else:
                        print("O certo seria "+str(int(pow(y,2))+(int(pow(x,2))*int(-1))))
        elif prop.VarArrangeOpt == '3':
            if int(pow(x,2))+(int(pow(y,2))*int(-1)) >= 0:
                z = str(input("Sendo c1 = "+str(y)+" e hip = "+str(x)+", c2 = à raiz quadrada de : "))
                if utils.CheckForFloat(z) == False:
                    if z == 'exit':
                        return PitagorasMenu(GameMenu)
                    else:
                        return pitagoras(GameMenu)
                else:
                    if float(z) == (pow(x,2))+(int(pow(y,2))*int(-1)):
                        print("Correto")
                    else:
                        print("O certo seria "+str(int(pow(x,2))+(int(pow(y,2))*int(-1))))
    elif prop.PitagorasModeOpt == '2':
        if prop.VarArrangeOpt == '1':
            if (pow(x,2)+pow(x,2)) >= 0:
                z = str(input("Sendo c1 = "+str(x)+" e c2 = "+str(y)+", hip = "))
                if utils.CheckForFloat(z) == False:
                    if z == 'exit':
                        return PitagorasMenu(GameMenu)
                    else:
                        return pitagoras(GameMenu)
                else:
                    if float(z) == round((math.sqrt(pow(x,2)+pow(y,2))),shared.FloatPrec):
                        print("Correto")
                    else:
                        print("O certo seria "+str(round(math.sqrt(pow(x,2)+pow(y,2)),shared.FloatPrec)))
        elif prop.VarArrangeOpt == '2':
                if (int(pow(y,2))+(int(pow(x,2))*int(-1))) >= 0:
                    z = str(input("Sendo c2 = "+str(x)+" e hip = "+str(y)+", c1 = "))
                    if utils.CheckForFloat(z) == False:
                        if z == 'exit':
                            return PitagorasMenu(GameMenu)
                        else:
                            return pitagoras(GameMenu)
                    else:
                        if float(z) == round(math.sqrt(int(pow(y,2))+(int(pow(x,2))*int(-1))),shared.FloatPrec):
                            print("Correto")
                        else:
                            print("O certo seria "+str(round(math.sqrt(int(pow(y,2))+(int(pow(x,2))*int(-1))),shared.FloatPrec)))
        elif prop.VarArrangeOpt == '3':
            if (int(pow(x,2))+(int(pow(y,2))*int(-1))) >= 0:
                z = str(input("Sendo c1 = "+str(y)+" e hip = "+str(x)+", c2 = "))
                if utils.CheckForFloat(z) == False:
                    if z == 'exit':
                        return PitagorasMenu(GameMenu)
                    else:
                        return pitagoras(GameMenu)
                else:
                    if float(z) == round(math.sqrt(int(pow(x,2))+(int(pow(y,2))*int(-1))),shared.FloatPrec):
                        print("Correto")
                    else:
                        print("O certo seria "+str(round(math.sqrt(int(pow(x,2))+(int(pow(y,2))*int(-1))),shared.FloatPrec)))

def PitagorasModeLogo(): # mode-based logo
    with open('./design/ModeLogo/logotype'+str(prop.PitagorasModeOpt)+'.txt') as txt:
        print(txt.read())
