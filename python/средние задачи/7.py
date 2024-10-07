def is_perfect_number(n):
    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n

try:
    number = int(input("Введите число для проверки: "))

    if is_perfect_number(number):
        print(f"{number} является совершенным числом.")
    else:
        print(f"{number} не является совершенным числом.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")
