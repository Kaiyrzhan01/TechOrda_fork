def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

try:
    number = int(input("Введите число для проверки, является ли оно числом Фибоначчи: "))

    if is_fibonacci(number):
        print(f"{number} является числом Фибоначчи.")
    else:
        print(f"{number} не является числом Фибоначчи.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
