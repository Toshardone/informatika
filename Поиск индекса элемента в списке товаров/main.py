# TODO Напишите функцию для поиска индекса товара
def Find_ind(list, tov): # Перебираем все элементы списка
    for ind in range(len(list)):
        if list[ind] == tov:   # Сравниваем текущий элемент
            return ind             # Возвращаем индекс первого
    return None                       # Если ничего нет возвращаем None
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = Find_ind(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
