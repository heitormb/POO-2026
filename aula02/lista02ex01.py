print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
sp = 0
si = 0
if a % 2 == 0: sp += a 
else: si += a
if b % 2 == 0: sp += a 
else: si += b
if c % 2 == 0: sp += a 
else: si += c
if d % 2 == 0: sp += a 
else: si += d
print("Soma dos pares:", sp)
print("Soma dos ímpares:", si)