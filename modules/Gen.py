# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import shared as s 
import utils as u

def PtgsGen(q): # TODO : Optimization
    Opt = str(input("Modo (1-2)(Ver manual): "))
    for i in range(0,q):
        x = u.randint(s.IntMin,s.IntMax)
        y = u.randint(s.IntMin,s.IntMax)
        z = u.randint(s.IntMin,s.IntMax)
        if Opt == '1':
        	if x >= y and x >= z: # Caso x maior
        		rs = (y**2)+(z**2)
        		print("c1 = "+str(y)+", c2 = "+str(z)+", hip = raiz quadrada de "+str(rs))
        	elif y >= x and y >= z: # Caso y maior
        		rs = (x**2)+(z**2)
        		print("c1 = "+str(x)+", c2 = "+str(z)+", hip = raiz quadrada de "+str(rs))
        	elif z >= x and z >= y: # Caso z maior
        		rs = (x**2)+(y**2)
        		print("c1 = "+str(x)+", c2 = "+str(y)+", hip = raiz quadrada de "+str(rs))
        elif Opt == '2':
        	if x >= y and x >= z: # Caso x maior
        		rs = round(u.sqrt((y**2)+(z**2)),s.FloatPrec)
        		print("c1 = "+str(y)+", c2 = "+str(z)+", hip = "+str(rs))
        	elif y >= x and y >= z: # Caso y maior
        		rs = round(u.sqrt((x**2)+(z**2)),s.FloatPrec)
        		print("c1 = "+str(x)+", c2 = "+str(z)+", hip = "+str(rs))
        	elif z >= x and z >= y: # Caso z maior
        		rs = round(u.sqrt((x**2)+(y**2)),s.FloatPrec)
        		print("c1 = "+str(x)+", c2 = "+str(y)+", hip = "+str(rs))
    utils.getch()

def BskrGen(q):
    for i in range(0,q):
        a = u.randint(s.IntMin,s.IntMax)
        b = u.randint(s.IntMin,s.IntMax)
        c = u.randint(s.IntMin,s.IntMax)
        Delta, x1, x2, Xv, Yv, a, b, c = u.GenBhaskara(s.IntMin,s.IntMax,s.FloatPrec)
        print(u.Sig(a),"*x\N{SUPERSCRIPT TWO} ",u.Sig(b),"*x ",u.Sig(c))
        print("Delta = ",Delta,"\nx1 = ",x1,"\nx2 = ",x2,"\nXv = ",Xv,"\nyv = ",Yv)
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
        print("Min: ",s.IntMin)
        print("Max: ",s.IntMax)
        print("Prec: ",s.FloatPrec)
        q = int(input("Quantidade para gerar: "))
        if Opt == '1': PtgsGen(q)
        elif Opt == '2': BskrGen(q)
