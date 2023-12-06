import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    if isinstance(cats[0], dict):  # Перевіряємо, чи cats - список словників
        converted_list = []
        for cat_dict in cats:
            cat_namedtuple = Cat(**cat_dict)  # Створюємо іменований кортеж зі словника
            converted_list.append(cat_namedtuple)
        return converted_list
    else:
        converted_list = []
        for cat_namedtuple in cats:
            cat_dict = cat_namedtuple._asdict()  # Перетворюємо іменований кортеж у словник
            converted_list.append(cat_dict)
        return converted_list


# Приклад використання
cats_list = [
    Cat("Mick", 5, "Sara"),
    Cat("Barsik", 7, "Olga"),
    Cat("Simon", 3, "Yura")
]

converted_dict_list = convert_list(cats_list)
print(converted_dict_list)
