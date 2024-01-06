"""
: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
import random
n = int(input("Enter the number of elements of the first set: "))
m = int(input("Enter the number of elements of the second set: "))

set_1 = set(random.randint(1, 100) for _ in range(n))
print(set_1)
set_2 = set(random.randint(1, 100) for _ in range(m))
print(set_2)
common_elements = sorted(set_1.intersection(set_2))

if common_elements:
    print(f"Common elements in both sets: ", common_elements )
else:
    print("There are no common elements in both sets.")
