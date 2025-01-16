# Recursão: função que chama a si mesma
# python recursao.py


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    

print(fatorial(5)) # 120

# fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8)) # 5