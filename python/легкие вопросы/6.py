def calc_deposit(n, k, b):
    for _ in range(n):
        b += b * (k / 100)
    return b

n = int(input("Введите количество месяцев: "))
k = float(input("Введите процентную ставку: "))
b = float(input("Введите начальный баланс: "))

result = calc_deposit(n, k, b)
print(result)