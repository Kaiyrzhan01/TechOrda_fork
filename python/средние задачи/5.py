def is_perfect_number(n):
    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n

try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    perfect_numbers = []
    for number in range(start, end + 1):
        if is_perfect_number(number):
            perfect_numbers.append(number)

    print(f"Совершенные числа в диапазоне от {start} до {end}: {perfect_numbers}")
except ValueError:
    print("Пожалуйста, введите корректные целые числа для диапазона.")
