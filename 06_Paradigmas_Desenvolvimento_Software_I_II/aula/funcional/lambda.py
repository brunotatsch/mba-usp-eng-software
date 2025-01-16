# Criação: 21/02/2021
dobro = lambda x: x * 2

print(dobro(4))

# Calcular o dobros de uma lista
numeros = [1, 2, 3, 4, 5]
dobros = list(map(lambda x: x * 2, numeros))
print(f'Dobros: {dobros}')