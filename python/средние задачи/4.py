from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

date_input = input("Введите дату в формате 'DD.MM.YYYY': ")

if is_valid_date(date_input):
    print(f"{date_input} является корректной датой.")
else:
    print(f"{date_input} не является корректной датой.")
