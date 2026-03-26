a = int(input())
b = int(input())

def maior(a, b):
    if a == b:
        print("Números iguais")
    elif a != b:
        c = max(a, b)
        print(f'Maior = {c}')

maior(a, b)