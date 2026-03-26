entrada = input("Digite uma sequência de números separados por vírgula: ")

numeros = entrada.split(',')

soma = 0
for num in numeros:
    soma += int(num)

print(f"Soma = {soma}")