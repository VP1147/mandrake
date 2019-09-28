# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import shared, utils, prop

def BskrGen():
	utils.LogoType(shared.LogoPath)
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
			rs = utils.SolveDelta(a,b,c) # Calcula delta
			print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
			print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
			print("Delta = "+str(rs))
		elif prop.GenBskrModeOpt == '2':
			rs1,rs2 = utils.SolveBhaskara(a,b,c,shared.FloatPrec) # Calcula x1 e x2
			print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
			print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
			print("x1 = "+str(rs1)+" | x2 = "+str(rs2))
	utils.getch()
	return 0

def PtgsGen():
    utils.LogoType(shared.LogoPath)
    print("<---Gerar Teorema de Pítágoras--->")
    print("Valor mínimo das variáveis: ",shared.IntMin)
    print("Valor máximo das variáveis: ",shared.IntMax)
    print("Precisão de decimais: ",shared.FloatPrec)
    prop.GenPtgsModeOpt = str(input("Modo (1-2)(Ver manual): "))
    GenQuant = int(input("Quantidade para gerar: "))
    for i in range(0,GenQuant):
        x = utils.randint(shared.IntMin,shared.IntMax)
        y = utils.randint(shared.IntMin,shared.IntMax)
        z = utils.randint(shared.IntMin,shared.IntMax)
        if prop.GenPtgsModeOpt == '1':
        	if x >= y and x >= z: # Caso x maior
        		rs = (y**2)+(z**2)
        		print("c1 = "+str(y)+", c2 = "+str(z)+", hip = raiz quadrada de "+str(rs))
        	elif y >= x and y >= z: # Caso y maior
        		rs = (x**2)+(z**2)
        		print("c1 = "+str(x)+", c2 = "+str(z)+", hip = raiz quadrada de "+str(rs))
        	elif z >= x and z >= y: # Caso z maior
        		rs = (x**2)+(y**2)
        		print("c1 = "+str(x)+", c2 = "+str(y)+", hip = raiz quadrada de "+str(rs))
        elif prop.GenPtgsModeOpt == '2':
        	if x >= y and x >= z: # Caso x maior
        		rs = round(utils.sqrt((y**2)+(z**2)),shared.FloatPrec)
        		print("c1 = "+str(y)+", c2 = "+str(z)+", hip = "+str(rs))
        	elif y >= x and y >= z: # Caso y maior
        		rs = round(utils.sqrt((x**2)+(z**2)),shared.FloatPrec)
        		print("c1 = "+str(x)+", c2 = "+str(z)+", hip = "+str(rs))
        	elif z >= x and z >= y: # Caso z maior
        		rs = round(utils.sqrt((x**2)+(y**2)),shared.FloatPrec)
        		print("c1 = "+str(x)+", c2 = "+str(y)+", hip = "+str(rs))
    utils.getch()

def FQuadGen():
    utils.LogoType(shared.LogoPath)
    print("<---Gerar função quadrática--->")
    print("Valor mínimo das variáveis: ",shared.IntMin)
    print("Valor máximo das variáveis: ",shared.IntMax)
    print("Precisão de decimais: ",shared.FloatPrec)
    GenQuant = int(input("Quantidade para gerar: "))
    for i in range(0,GenQuant):
        a = utils.randint(shared.IntMin,shared.IntMax)
        b = utils.randint(shared.IntMin,shared.IntMax)
        c = (utils.randint(shared.IntMin,shared.IntMax))*-1
        x1,x2,xv,yv = utils.SolveFQuad(a,b,c,shared.FloatPrec) # Define x1, x2, Xv e Yv.
        print(str(a)+"*x^2 + "+str(b)+"*x + ("+str(c)+")")
        print("a = "+str(a)+" | b = "+str(b)+" | c = "+str(c)) # Mostra a, b e c
        print("x1 = "+str(x1)+"\nx2 = "+str(x2)+"\nXv = "+str(xv)+"\nyv = "+str(yv))
        print("Interceção com eixo Y: "+str(c)) 
    utils.getch()

def GenMenu():
	while 1:
		utils.LogoType(shared.LogoPath)
		print("1 - Teorema de Pitágoras")
		print("2 - Equação quadrática")
		print("3 - Função quadrática")
		print("x - Voltar")
		GenMenuOpt = utils.getch()
		if GenMenuOpt == '1':
			PtgsGen()
		elif GenMenuOpt == '2':
			BskrGen()
		elif GenMenuOpt == '3':
			FQuadGen()
		elif GenMenuOpt == 'x':
			return 0

