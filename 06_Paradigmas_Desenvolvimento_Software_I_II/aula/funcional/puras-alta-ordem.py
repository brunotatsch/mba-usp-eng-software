# python puras-alta-ordem.py
def soma(x, y):
    return x + y
 
print(soma(3, 4))
print(soma(3, 4))

def aplicar_duas_vezes(funcao, x):
    return funcao(funcao(x))

print(aplicar_duas_vezes(lambda x: x * 3,4))

def incrementar(x):
    return x + 1

print(aplicar_duas_vezes(incrementar, 4))

numeros = [1, 2, 3, 4, 5, 6]

def eleva_ao_quadrado(x):
    return x ** 2


def aplicar_transformacao(funcao, lista):
    return [funcao(x) for x in lista]

print(aplicar_transformacao(lambda x: x * 2, numeros))

print(aplicar_transformacao(eleva_ao_quadrado, numeros))
