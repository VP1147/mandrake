# # -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147
import shared
import utils

def FQuadGen():
    utils.LogoType()
    print("<---Gerar função quadrática--->")
    print("Valor mínimo das variáveis: ",shared.IntMin)
    print("Valor máximo das variáveis: ",shared.IntMax)
    print("Precisão de decimais: ",shared.FloatPrec)
    GenQuant = int(input("Quantidade para gerar: "))
    for i in range(0,GenQuant):
        a = utils.randint(shared.IntMin,shared.IntMax)
        b = utils.randint(shared.IntMin,shared.IntMax)
        c = (utils.randint(shared.IntMin,shared.IntMax))*-1
        GenFQuad(a,b,c)
    utils.getch()

def GenFQuad(a,b,c):
    x1, x2, xv, yv = utils.SolveFQuad(a,b,c,shared.FloatPrec) # Calcula
                                                              # x1, x2, Xv e Yv.
    print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
    print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
    print("x1 = "+str(x1)+"\nx2 = "+str(x2)+"\nXv = "+str(xv)+"\nyv = "+str(yv))
    print("Interceção com eixo Y: "+str(c))
