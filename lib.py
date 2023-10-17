def count_common_elements(*lists):
    # Объединяем все списки в один
    combined_list = []
    for lst in lists:
        combined_list += lst

    # Создаем словарь для подсчета элементов
    element_counts = {}
    for element in combined_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Считаем количество одинаковых элементов
    common_elements = 0
    for count in element_counts.values():
        if count == len(lists):
            common_elements += 1

    return common_elements


