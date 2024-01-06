"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
"""
def find_indices_in_range(lst, min_num, max_num):
    indices = []
    for i, num in enumerate(lst):
        if min_num <= num <= max_num:
            indices.append(i)
    return indices

# Пример использования
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

result_indices = find_indices_in_range(list_1, min_number, max_number)
#print("Индексы элементов в заданном диапазоне:", result_indices)
for index in result_indices:
    print(index)




#from autotest
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            print(i)