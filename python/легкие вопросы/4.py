a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()