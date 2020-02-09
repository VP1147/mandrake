# -*- encoding: utf-8 -*-
# library for Mandrake | by vp1147

import shared as s
import utils as u

def QuadFMenu():
	u.clear()
	if u.MinSize() == True: u.ReadTxt((s.GameLogoPath+'function.txt')) # Mode logo
	else: print("< f(x) >")
	print("<'exit' para sair>")
	print("<Precisão de "+str(s.FloatPrec)+" decimal(is)>")
	while 1:
		if s.RCount == 0:
			Signal = QuadF()
			if Signal == 'exit': return 0
		else:
			List = []
			for Count in range(s.RCount):
				List.insert(Count,QuadF())
			print("-- Concluido --")
			for i in range(s.RCount):
				print(str((i+1))+" - "+', '.join(List[i]))
			u.getch()
			return 0

def QuadF():
	Delta, x1, x2, Xv, Yv, a, b, c = u.GenBhaskara(s.IntMin,s.IntMax,s.FloatPrec)
	rs = (Delta,x1,x2,Xv,Yv)
	l = []
	q = ("Delta","x1 (+)","x2 (-)","Xv","Yx")
	print(u.Sig(a),"x\N{SUPERSCRIPT TWO} ",u.Sig(b),"x ",u.Sig(c))
	for i in range(len(rs)):
		r = input(q[i]+" = ")
		if s.RCount == 0 and r == 'exit': return 'exit'
		if u.CheckForFloat(r) == False: l.append('Nula')
		elif float(r) == rs[i]:
			print("Certo")
			l.append('Certo')
		else:
			print("O correto seria "+str(rs[i])+".")
			l.append('Errado')
	return l
