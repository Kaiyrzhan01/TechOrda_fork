def range_n(n):
    if n <= 0:
        return []

    result = []
    for i in range(1, n + 1):
        result.append(i)
    
    return result

n = int(input("Введите n: "))
arr = range_n(n)

print("Массив:", arr)

for i in range(len(arr)):
    print(arr[i], end=" ")