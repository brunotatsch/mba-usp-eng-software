# Somar números até atingir um limite

limite = 100
soma = 0
numero = 1

# Enquanto a soma for menor que o limite, continue somando
while soma < limite:
    soma += numero
    numero += 1 # Incrementa o número
    print(f'Número: {numero}, Soma: {soma}')

print(f'A soma dos números até atingir o limite {limite} é {soma}')

# Encontrar o primeiro numero divisivel por 7 em um intervalo
intervalo = range(8, 100)
for numero in intervalo:
    if numero % 7 == 0:
        print(f'O primeiro número divisível por 7 é {numero}')
        break 
    
# Verifica se todos os itens de uma lista sao positivos
numeros = [1,2,3,8,9,-1]
todos_positivos = True
for numero in numeros:
    if numero < 0:
        todos_positivos = False
        break    
print(f'Todos os números são positivos? {todos_positivos}')