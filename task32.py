"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
"""

def find_indices_in_range(arr, min_value, max_value):
    indices = [i for i, element in enumerate(arr) if min_value <= element <= max_value]
    return indices

# Ваш введенный список
my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Указанный диапазон (включительно)
min_range = -3
max_range = 3

result_indices = find_indices_in_range(my_list, min_range, max_range)

print(f"Индексы элементов в диапазоне от {min_range} до {max_range}: {result_indices}")


