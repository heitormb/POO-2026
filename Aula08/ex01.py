# dicionário é uma coleção de itens
# os itens são separados por ,
# cada item chave : valor

x = { "RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife" }
y = [1, 2, 3, 4]
z = (1, 2, 3, 4)

x["AM"] = "Manaus"     # insere
x["PB"] = "J. Pessoa"  # altera
x.pop("PB")            # remove

print(len(x))
for item in x.items(): print(item)


print(x)
print(*x)
print(x["RN"])
#print(x["SP"])

print(y[2])

print(type(x))
print(type(y))
print(type(z))