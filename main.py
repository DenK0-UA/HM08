from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_day = {today.strftime('%A'): today}
    for i in range(1, 7):
        today += timedelta(days=1)
        current_day[today.strftime('%A')] = today

    result = {}

    for user in users:
        current_users = user["birthday"]

        for weekday in current_day:
            current_today = current_day[weekday]

            if not (current_today.month == current_users.month and current_today.day == current_users.day):
                continue

            if weekday in ('Sunday', 'Saturday'):
                if 'Monday' in result:
                    result['Monday'].append(user["name"])
                else:
                    result['Monday'] = [user["name"]]

            else:
                if weekday in result:
                    result[weekday].append(user["name"])
                else:
                    result[weekday] = [user["name"]]

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan", "birthday": datetime(1976, 11, 24).date()},
        {"name": " Koum", "birthday": datetime(1976, 11, 22).date()},
        {"name": "JK", "birthday": datetime(1976, 11, 25).date()},
        {"name": "Heho", "birthday": datetime(1976, 11, 26).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
