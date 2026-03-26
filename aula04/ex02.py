entrada = input("Digite dois valores inteiros separados por um operador (+, -, * ou /): ")

if '+' in entrada:
    operador = '+'
elif '-' in entrada:
    operador = '-'
elif '*' in entrada:
    operador = '*'
elif '/' in entrada:
    operador = '/'
else:
    print("Operador inválido!")
    exit()

valores = entrada.split(operador)

num1 = int(valores[0])
num2 = int(valores[1])

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2

print(f"O resultado da operação é {resultado}")