a = int(input("Введите число a: "))
b = int(input("Введите степень b: "))

result = 1

for _ in range(b):
    result *= a

print(result)