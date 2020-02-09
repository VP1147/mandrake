# # -*- encoding: utf-8 -*-
# Library for Mandrake | By vp1147

import utils as u
import shared as s

def PtgsMenu():
	u.LogoType(s.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	Opt = u.getch()
	if Opt == 'x' or int(Opt) > 2: return 0
	u.clear()
	if u.MinSize() == True: u.ReadTxt((s.GameLogoPath+'pit.txt')) # Mode logo
	else: print("< Pitágoras >")
	print("<'exit' para sair>")
	print("<Precisão de "+str(s.FloatPrec)+" decimal(is)>")
	while 1:
		if s.RCount == 0:
			Signal = Ptgs(Opt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,Ptgs(Opt))
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+List[i])
			u.getch()
			return 0

def Ptgs(Opt):
	c1,c2 = u.randint(1,s.IntMax),u.randint(1,s.IntMax)
	hip = round(u.sqrt((c1**2)+(c2**2)),s.FloatPrec)
	if Opt == '1': # Simples: calc raiz de hip
		print("c1 = ",c1,", c2 = ",c2,", hip = √")
		rs = (c1**2+c2**2)
	elif Opt == '2': # Normal: calcula hip
		print("c1 = ",c1,", c2 = ",c2,", hip = ")
		rs = hip
	r = input()
	if u.CheckForFloat(r) == False:
		if r == 'exit': return 'exit'
		else: return 'Nula'
	else:
		if float(r) == rs:
			print("Certo")
			return 'Certo'
		else:
			print("O certo seria ",rs,".")
			return 'Errado'

def BskrMenu():
	u.LogoType(s.LogoPath)
	print("<---Modo--->")
	print("1 - Simples")
	print("2 - Padrão")
	print("x - Voltar")
	Opt = u.getch()
	if Opt == 'x' or int(Opt) > 2: return 0
	u.clear()
	if u.MinSize() == True: u.ReadTxt((s.GameLogoPath+'bhaskara.txt')) # Mode logo
	else: print("< Bhaskara >")
	print("<'exit' para sair>")
	print("<Precisão de ",s.FloatPrec," decimal(is)>")
	while 1:
		if s.RCount == 0:
			Signal = Bhaskara(Opt)
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,Bhaskara(Opt))
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			u.getch()
			return 0

def Bhaskara(Opt):
	Delta, x1, x2, xv, yv, a, b, c = u.GenBhaskara(s.IntMin, s.IntMax, s.FloatPrec)
	l = []
	if Opt == '1':
		print(u.Sig(a),"x\N{SUPERSCRIPT TWO} ",u.Sig(b),"x ",u.Sig(c))
		r = input("Delta = ")
		if r == 'exit' and s.RCount == 0: return 'exit'
		if u.CheckForFloat(r) == False: l.append('Nula')
		elif float(r) == Delta: # P/ evitar diferença entre tipos de dados
			print("Certo")
			l.append('Certo')
		else:
			print("O correto seria ",Delta,".")
			l.append('Errado')
	elif Opt == '2':
		q = ("Delta","x1 (+)","x2 (-)")
		rs = (Delta,x1,x2)
		print(u.Sig(a),"x\N{SUPERSCRIPT TWO} ",u.Sig(b),"x ",u.Sig(c))
		for i in range(len(rs)):
			r = input(q[i]+" = ")
			if r == 'exit' and s.RCount == 0: return 'exit'
			if u.CheckForFloat(r) == False: l.append('Nula')
			elif float(r) == rs[i]:
				print("Certo")
				l.append('Certo')
			else:
				print("O correto seria ",rs[i],".")
				l.append('Errado')
	return l
