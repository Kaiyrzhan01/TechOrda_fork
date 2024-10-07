def sum_array(array):
    if len(array) == 0:
        return 0

    total = 0

    for num in array:
        total += num
    
    return total

length = int(input("Введите длину массива: "))

if length <= 0:
    print("Длина массива должна быть больше 0.")
else:
    array = []

    print(f"Введите {length} чисел (через пробел): ")
    input_elements = input().split()

    if len(input_elements) != length:
        print(f"Ошибка: ожидается {length} чисел.")
    else:
        for element in input_elements:
            try:
                num = int(element)
                array.append(num)
            except ValueError:
                print(f"Ошибка: '{element}' не является числом. Ввод будет проигнорирован.")
        
        sum_number = sum_array(array)

        print(f"Сумма элементов массива: {sum_number}")
