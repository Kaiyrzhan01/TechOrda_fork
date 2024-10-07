def get_season(day, month):
    if (month == 12 and day >= 1) or (month == 1) or (month == 2):
        return "Зима"
    elif (month == 3) or (month == 4) or (month == 5):
        return "Весна"
    elif (month == 6) or (month == 7) or (month == 8):
        return "Лето"
    elif (month == 9) or (month == 10) or (month == 11):
        return "Осень"
    else:
        return None

try:
    date_input = input("Введите дату в формате 'день.месяц' (например, 21.03): ")
    day, month = map(int, date_input.split('.'))

    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Пожалуйста, введите корректную дату.")
    else:
        season = get_season(day, month)
        if season:
            print(f"Дата {date_input} попадает в сезон: {season}.")
        else:
            print("Дата некорректна.")
except ValueError:
    print("Пожалуйста, введите дату в правильном формате.")
