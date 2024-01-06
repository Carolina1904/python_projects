"""
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X

"""

import random

def count_occurrences(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count

# Ввод данных от пользователя
N = int(input("Введите количество элементов в массиве: "))

# Генерация рандомного массива
A = [random.randint(1, 100) for _ in range(N)]
print(f"Сгенерированный массив: {A}")

X = int(input("Введите число X: "))

# Вычисление и вывод результата
result = count_occurrences(A, X)
print(f"Число {X} встречается в массиве {result} раз.")