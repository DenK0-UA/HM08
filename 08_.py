from datetime import date

def get_days_in_month(month, year):
    if month == 2 and date(year, 2, 29):
        #if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29  # Високосний рік, лютого 29 днів
    # elif month != 2:
    #     return 28 # Звичайний рік, лютого 28 днів

    elif month in [4, 6, 9, 11]:
        return 30  # Квітень, червень, вересень, листопад - 30 днів
    else:
        return 31  # Січень, березень, травень, липень, серпень, жовтень, грудень - 31 день


a = get_days_in_month(2,2021)
print(a)

