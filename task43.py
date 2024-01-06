"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
"""
import random
lst = [random.randint(0,10)for _ in range(int(input("Enter the size: ")))]
print(lst)
print(set(lst))

count = 0
for item in set(lst):
    count += lst.count(item)//2
print(count)

