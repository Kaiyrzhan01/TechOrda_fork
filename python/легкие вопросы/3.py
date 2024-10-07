m = int(input("Введите начальное число m: "))
n = int(input("Введите конечное число n: "))

sum_of_squares = 0

for i in range(m, n + 1):
    sum_of_squares += i * i  # Добавляем квадрат числа i к сумме

print("Сумма квадратов чисел от", m, "до", n, "равна:", sum_of_squares)