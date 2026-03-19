print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b or a == c or a == d or b == c or b == d or c == d:
    print("Algum valor está repetido")
else:
    #menor valor
    menor = a
    if b < menor: menor = b
    if c < menor: menor = c
    if d < menor: menor = d
    #maior valor
    maior = a
    if b > maior: maior = b
    if c > maior: maior = c
    if d > maior: maior = d
    #soma do segundo menor com o segundo maior
    soma = a + b + c + d - menor - maior
    print("Menor valor", menor)
    print("Maior valor", maior)
    print("Soma dos outros valores", soma)