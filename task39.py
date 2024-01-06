"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
"""
import random

len1 = int(input("enter the length of the first list: "))
len2 = int(input("enter the length of the second list: "))

lst1 = [random.randint(0, 5) for _ in range(len1)]
lst2 = [random.randint(0, 5) for _ in range(len2)]

print(lst1)
print(lst2)

for elem in lst1:
    if elem not in lst2:
        print(elem, end=" ")