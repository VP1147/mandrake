# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import shared as s 
import utils as u

def PtgsGen(q): # TODO : Optimization
    for i in range(0,q):
        c1,c2 = u.randint(1,s.IntMax),u.randint(1,s.IntMax)
        hip = round(u.sqrt((c1**2)+(c2**2)),s.FloatPrec)
        print("c1 =",c1,", c2 =",c2,", hip = √",(c1**2+c2**2),"=",hip)
    u.getch()

def BskrGen(q):
    for i in range(0,q):
        a, b, c = u.randint(s.IntMin,s.IntMax),u.randint(s.IntMin,s.IntMax),u.randint(1,s.IntMax)
        Delta, x1, x2, Xv, Yv, a, b, c = u.GenBhaskara(s.IntMin,s.IntMax,s.FloatPrec)
        print(u.Sig(a),"x\N{SUPERSCRIPT TWO}",u.Sig(b),"x",u.Sig(c))
        print("Delta =",Delta,"\nx1 =",x1,"\nx2 =",x2,"\nXv =",Xv,"\nyv =",Yv)
    u.getch()

def GenMenu():
    while 1:
        u.LogoType(s.LogoPath)
        print("1 - Teorema de Pitágoras")
        print("2 - Equação quadrática")
        print("x - Voltar")
        Opt = u.getch()
        if Opt == 'x': return 0
        u.clear()
        print("Min: ",1)
        print("Max: ",s.IntMax)
        print("Prec: ",s.FloatPrec)
        q = int(input("Quantidade para gerar: "))
        if Opt == '1': PtgsGen(q)
        elif Opt == '2': BskrGen(q)
