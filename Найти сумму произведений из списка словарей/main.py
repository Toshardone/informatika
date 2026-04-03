# TODO решите задачу
import json


def task() -> float: #Объявляем функцию
    with open('input.json', 'r', encoding='utf-8') as f: #Открываем data.json в режиме чтения
        data = json.load(f) #Преобразует JSON-строку в Python-объекты

    total = 0.0
    for item in data: #Запускаем цикл по каждому элементу списка
        total += item['score'] * item['weight']

    return round(total, 3)


print(task())
