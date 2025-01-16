numbers = [1, 2, 3, 4, 5]

print("Number list:", numbers)

print("First element:", numbers[0])  # Primeiro elemento
print("Last element:", numbers[-1])  # Último elemento

numbers.append(6)
print("Array after append number 6:", numbers)

numbers.remove(3)
print("Array after remove the number 3:", numbers)

print("Array element's:")
for number in numbers:
    print(number)

if 2 in numbers:
    print("Array contains the number 2.")
else:
    print("Array not contains the number 2.")
