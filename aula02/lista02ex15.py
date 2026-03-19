print("Digite um número inteiro")
n = int(input())
primo = True
for d in range(2, n):
    if n % d == 0: primo = False
    if primo == False: break
if primo == True: print(n, "é primo")
else: print(n, "não é primo")