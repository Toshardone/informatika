import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение CSV файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file) #использует первую строку как заголовки столбцов
        data = list(reader) # Преобразуем в список словарей


    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file: # Запись в JSON файл с отступами 4

        json.dump(data, json_file, indent=4)     # форматирование с отступами


if __name__ == '__main__':
    task()

# Вывод содержимого output.json (для проверки)
with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
    for line in output_f:
        print(line, end="")