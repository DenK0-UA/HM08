from datetime import datetime

def get_str_date(date):
    # Перетворюємо рядок з датою на об'єкт datetime
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')

    # Отримуємо назву дня тижня, числа, назву місяця та рік
    day = dt.strftime('%A')
    day_number = dt.strftime('%d')
    month = dt.strftime('%B')
    year = dt.strftime('%Y')

    # Формуємо рядок з результатом
    result = f"{day} {day_number} {month} {year}"

    return result


#date = '2021-05-27 17:08:34.149Z'
date = datetime.now()
iso_format = date.strftime('%Y-%m-%d %H:%M:%S.%fZ')
print(iso_format)
formatted_date = get_str_date(iso_format)
print(formatted_date)