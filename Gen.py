# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147
import shared
import utils
import prop
import GenPtgs
import GenBskr

def GenMenu(InitMenu):
    utils.LogoType()
    print("1 - Teorema de Pitágoras")
    print("2 - Equação quadrática")
    print("x - Voltar")
    GenMenuOpt = utils.getch()
    if GenMenuOpt == '1':
        GenPtgs.PtgsGen()
        return GenMenu(InitMenu)
    elif GenMenuOpt == '2':
        GenBskr.BskrGen()
        return GenMenu(InitMenu)
    elif GenMenuOpt == 'x':
        return InitMenu()
    else:
        return GenMenu(InitMenu)
