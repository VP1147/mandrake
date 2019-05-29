import utils
import math
import os
import shared

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
    print("Valor mínimo das variáveis: "+str(shared.IntMin))
    print("Valor máximo das variáveis: "+str(shared.IntMax))
    VarArrange = int(input("Modo de arranjo das variáveis (ler manual): "))
    # Rand Var arrange bool #
    if VarArrange == 4:
        RandVarArrange = True
    else:
        RandVarArrange = False
    GenQuant = int(input("Contas p/ gerar: "))
    GenPrec = int(input("Casas de precisão: "))
    GenMode = int(input("Modo -> 1-Simples / 2-Normal / 3-Aleatório : "))
    if GenMode == 3:
        RandMode = True
    else:
        RandMode = False
    for looper in range(0,GenQuant):
        if RandMode == True:
            GenMode = utils.randint(1,2)
        if RandVarArrange == True:
            VarArrangeOpt = utils.randint(1,3)
        x = utils.randint(shared.IntMin,shared.IntMax)
        y = utils.randint(shared.IntMin,shared.IntMax)
        if GenMode == 1:
            if VarArrange == 1:
                print("Sendo c1 = "+str(x)+" e c2 = "+str(y)+", hip = à raiz quadrada de : ")
                print("r = "+str(int(pow(x,2)+pow(y,2))))
            elif VarArrange == 2:
                print("Sendo c2 = "+str(x)+" e hip = "+str(y)+", c1 = à raiz quadrada de : ")
                print("r = "+str(int(pow(y,2))+(int(pow(x,2))*int(-1))))
            elif VarArrange == 3:
                print("Sendo c1 = "+str(y)+" e hip = "+str(x)+", c2 = à raiz quadrada de : ")
                print("r = "+str(int(pow(x,2))+(int(pow(y,2))*int(-1))))
        elif GenMode == 2:
            if VarArrange == 1:
                print("Sendo c1 = "+str(x)+" e c2 = "+str(y)+", hip = ")
                try:
                    print("r = "+str(round((math.sqrt(pow(x,2)+pow(x,2))),GenPrec)))
                except ValueError:
                    print("r =/R")
                except:
                    print("r = "+str(round((math.sqrt(pow(x,2)+pow(x,2))),GenPrec)))
            elif VarArrange == 2:
                print("Sendo c2 = "+str(x)+" e hip = "+str(y)+", c1 = ")
                try:
                    print("r = "+str(round(math.sqrt(int(pow(y,2))+(int(pow(x,2))*int(-1))),GenPrec)))
                except ValueError:
                    print("r =/R")
                except:
                    print("r = "+str(round(math.sqrt(int(pow(y,2))+(int(pow(x,2))*int(-1))),GenPrec)))
            elif VarArrange == 3:
                print("Sendo c1 = "+str(y)+" e hip = "+str(x)+", c2 = ")
                try:
                    print(str(round(math.sqrt(int(pow(x,2))+(int(pow(y,2))*int(-1))),GenPrec)))
                except ValueError:
                    print("r =/R")
                except:
                    print(str(round(math.sqrt(int(pow(x,2))+(int(pow(y,2))*int(-1))),GenPrec)))

    utils.getch()
