a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

max_number = a

if b > max_number:
    max_number = b

if c > max_number:
    max_number = c

print("Максимальное число:", max_number)