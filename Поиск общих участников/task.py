# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter= ','): #Находим общих участников в двух группах.
    # Разбиваем строки на списки участников
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    # Преобразуем списки во множества
    set1 = set(list1)
    set2 = set(list2)
    # Находим пересечение общих участников
    common_set = set1.intersection(set2)
    # Преобразуем множество в список и сортируем его
    common_list = sorted(common_set)
    return common_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)  # ['Петров', 'Сидоров']