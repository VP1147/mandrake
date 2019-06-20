# # -*- encoding: utf-8 -*-
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
    if prop.AritOpt == 'x': return GameMenu()
    utils.clear()
    print("<'exit' para sair>")
    if prop.AritOpt == '4': print("<Precisão de "+str(shared.FloatPrec)+" decimal(is)")
    while 1: Arit(GameMenu)

def Arit(GameMenu):
    x = utils.randint(shared.IntMin,shared.IntMax)
    y = utils.randint(shared.IntMin,shared.IntMax)
    if prop.AritOpt == '1':
        r = input(str(x)+" + "+str(y)+" = ")
        rs = x+y
        if utils.CheckForFloat(r) == False:
            if r == 'exit': return AritMenu(GameMenu)
            else: return Arit(GameMenu)
        else:
            if float(r) == rs: print("Correto")
            else: print("O certo seria "+str(rs))
    elif prop.AritOpt == '2':
        r = input(str(x)+" - "+str(y)+" = ")
        rs = x-y
        if utils.CheckForFloat(r) == False:
            if r == 'exit': return AritMenu(GameMenu)
            else: return Arit(GameMenu)
        else:
            if float(r) == rs: print("Correto")
            else: print("O certo seria "+str(rs))
    elif prop.AritOpt == '3':
        r = input(str(x)+" x "+str(y)+" = ")
        rs = x*y
        if utils.CheckForFloat(r) == False:
            if r == 'exit': return AritMenu(GameMenu)
            else: return Arit(GameMenu)
        else:
            if float(r) == rs: print("Correto")
            else: print("O certo seria "+str(rs))
                
    elif prop.AritOpt == '4':
        try: x/y
        except ZeroDivisionError: return Arit(GameMenu)
        r = input(str(x)+" / "+str(y)+" = ")
        rs = round((x/y),shared.FloatPrec)
        if utils.CheckForFloat(r) == False:
            if r == 'exit': return AritMenu(GameMenu)
            else: return Arit(GameMenu)
        else:
            if float(r) == rs: print("Correto")
            else: print("O certo seria "+str(rs))
    else:
        return AritMenu(GameMenu)
