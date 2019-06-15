# Library for Mandrake (Gen functions) | By vp1147
import shared
import utils
import prop
from math import sqrt

def BskrGen():
    utils.LogoType()
    print("<---Gerar equação quadrática--->")
    print("Valor mínimo das variáveis: ",shared.IntMin)
    print("Valor máximo das variáveis: ",shared.IntMax)
    print("Precisão de decimais: ",shared.FloatPrec)
    prop.GenBskrModeOpt = str(input("Modo (1-2)(Ver manual): "))
    GenQuant = int(input("Quantidade para gerar: "))
    for i in range(0,GenQuant):
        a = utils.randint(shared.IntMin,shared.IntMax)
        b = utils.randint(shared.IntMin,shared.IntMax)
        c = (utils.randint(shared.IntMin,shared.IntMax))*-1
        if prop.GenBskrModeOpt == '1':
            GenBskrMode1(a,b,c)
        elif prop.GenBskrModeOpt == '2':
            GenBskrMode2(a,b,c)
    utils.getch()
            
def GenBskrMode1(a,b,c):
    rs = (b**2)-4*a*c # Calcula delta
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
    print("Delta = "+str(rs))

def GenBskrMode2(a,b,c):
    rs1 = round(float(((b*-1)+sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec) # Calcula x1
    rs2 = round(float(((b*-1)-sqrt((b**2)-4*a*c))/(2*a)),shared.FloatPrec) # Calcula x2
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
    print("x1 = "+str(rs1)+" | x2 = "+str(rs2))
