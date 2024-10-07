string = input("Введите строку: ")

cleaned_string = string.replace(" ", "").lower()

if cleaned_string == cleaned_string[::-1]:
    print(f'"{string}" является палиндромом.')
else:
    print(f'"{string}" не является палиндромом.')
