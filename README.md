# Mandrake
Conjunto de ferramentas e jogos simples de matemática em Python3.
Inclui:
- Aritmética;
- Equação quadrática (Bhaskara);
- Função quadrática;
- Teorema de Pitágoras;
- Área de figuras geométricas;
- Cálculo de números primos;
- Cálculo de pi
- Geração de exercícios.
- Funções úteis (utils.py)


## Debian
```
$ sudo apt install git python3
$ git clone https://github.com/vp1147/mandrake
$ cd ~/mandrake
$ python3 mandrake.py

## Windows
Abra o arquivo mandrake.py em um interpretador Python3 (https://www.python.org/downloads/windows/).
```
> python mandrake.py
```

Também é possível utilizar as funções da biblioteca utils.py separadamente. No interpretador Python3:
``` 
>>> import tools as t
```
Função GenCircle()
```
>>> foo = t.GenCircle(1,10,3)
>>> print(foo)
(7, 3.142, 153.958)
```
Função CheckForPrime()
```
>>> t.CheckForPrime(7)
True 
>>> t.CheckForPrime(223)
True
>>> t.CheckForPrime(984)
False
```
Função GenBhaskara()
```
>>> import tools as t
>>> a, b, c = 2, 5, -10 # 2x^2 + 5x - 10
>>> Delta, x1, x2, Xv, Yv = t.SolveBhaskara(a,b,c)
>>> print(Delta,x1,x2,Xv,Yv)
105 1.31 -3.81 -1.25 -13.12
```
