import math
import shared
import utils
import prop

def AritMenu(GameMenu):
    utils.LogoType()
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("x - Voltar")
    prop.AritOpt = utils.getch()
    if prop.AritOpt == 'x':
        return GameMenu()
    utils.clear()
    print("<'exit' para sair>")
    if prop.AritOpt == '4':
        print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)")
    while 1:
        Arit(GameMenu)

def Arit(GameMenu):
    x = utils.randint(shared.IntMin,shared.IntMax)
    y = utils.randint(shared.IntMin,shared.IntMax)
    if prop.AritOpt == '1':
        z = str(input(str(x)+" + "+str(y)+" = "))
        if utils.CheckForFloat(z) == False:
            if z == 'exit':
                return AritMenu(GameMenu)
            else:
                return Arit(GameMenu)
        else:
            if float(z) == float(x+y):
                print("Correto")
            else:
                print("O certo seria "+str(x+y))
    elif prop.AritOpt == '2':
        z = str(input(str(x)+" - "+str(y)+" = "))
        if utils.CheckForFloat(z) == False:
            if z == 'exit':
                return AritMenu(GameMenu)
            else:
                return Arit(GameMenu)
        else:
            if float(z) == float(x-y):
                print("Correto")
            else:
                print("O certo seria "+str(x-y))
    elif prop.AritOpt == '3':
        z = str(input(str(x)+" x "+str(y)+" = "))
        if utils.CheckForFloat(z) == False:
            if z == 'exit':
                return AritMenu(GameMenu)
            else:
                return Arit(GameMenu)
        else:
            if float(z) == float(x*y):
                print("Correto")
            else:
                print("O certo seria "+str(x*y))
                
    elif prop.AritOpt == '4':
        try:
            float(x/y)
        except ZeroDivisionError:
            return Arit(GameMenu)
        z = str(input(str(x)+" / "+str(y)+" = "))
        if utils.CheckForFloat(z) == False:
            if z == 'exit':
                return AritMenu(GameMenu)
            else:
                return Arit(GameMenu)
        else:
            
            if float(z) == float(round((x/y),shared.FloatPrec)):
                print("Correto")
            else:
                print("O certo seria "+str(round((x/y),shared.FloatPrec)))
    else:
        return AritMenu(GameMenu)
