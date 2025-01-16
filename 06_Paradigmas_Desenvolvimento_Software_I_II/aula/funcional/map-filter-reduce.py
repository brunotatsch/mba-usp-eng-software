# python map-filter-reduce.py
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map, filter, reduce

# filter - filtrar os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Pares: {pares}')

numeros_pares_dobrados = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))

print(f'Números pares dobrados: {numeros_pares_dobrados}')

# reduce - soma todos os números
soma = reduce(lambda x, y: x + y, numeros_pares_dobrados)
print(f'Soma: {soma}')