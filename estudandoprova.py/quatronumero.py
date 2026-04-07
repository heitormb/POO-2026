pares = 0
impares= 0

for i in range(1, 5):
    a = int(input())
    if a%2 == 0:
        pares = pares + a
    elif a%2 != 0:
        impares = impares + a


print(f'soma dos pares:{pares}')
print(f'soma dos impares:{impares}')