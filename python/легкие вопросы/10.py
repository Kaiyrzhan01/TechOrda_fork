def sort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

if __name__ == "__main__":
    length = int(input("Введите длину массива: "))

    array = []

    for i in range(length):
        element = int(input(f"Введите элемент {i + 1}: "))
        array.append(element)

    print("Массив до сортировки:", array)

    sort(array)

    print("Массив после сортировки:", array)
