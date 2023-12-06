from decimal import Decimal, getcontext

def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count  # Встановлюємо точність для Decimal

    sum_decimal = Decimal(0)  # Ініціалізуємо суму змінних типу Decimal
    count = len(number_list)  # Кількість чисел у списку

    for num in number_list:
        sum_decimal += Decimal(str(num))  # Додаємо число до суми

    if count > 0:
        average_decimal = sum_decimal / count  # Обчислюємо середнє арифметичне
        return average_decimal

    return Decimal(0)  # Повертаємо 0, якщо список чисел порожній


# Приклади використання
result1 = decimal_average([3, 5, 77, 23, 0.57], 4)
print(result1)  # Вивід: 21.714

result2 = decimal_average([31, 55, 177, 2300, 1.57], 5)
print(result2)  # Вивід: 512.91400
