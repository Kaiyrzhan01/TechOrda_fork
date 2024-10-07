def min(arr):
    if len(arr) == 0:
        return 0
   
    min_value = arr[0]

    for item in arr:
        if item < min_value:
            min_value = item
    
    return min_value

length = int(input("Введите длину массива: "))

array = []
for i in range(length):
    element = input(f"Введите элемент {i + 1}: ")
    # Если это число, то конвертируем в int
    try:
        element = int(element)
    except ValueError:
        pass
    array.append(element)

result = min(array)
print("Минимальный элемент в массиве:", result)