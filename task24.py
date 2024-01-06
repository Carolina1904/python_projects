"""
: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

"""
"""
def max_berry_harvest(n , berries):
    max_harvest = 0
    for i in range(n):
        current_harvest = berries[i] + berries[(i + 1)%n]+berries[(i+2)%n]
        max_harvest= max(max_harvest, current_harvest)
    return max_harvest

n = int(input())
berries = list(map(int,input().split()))
result = max_berry_harvest(n, berries)
print(result)
"""

n = int(input("enter: "))  # Количество кустов
berries = list(map(int, input().split()))  # Урожайность каждого куста
max_harvest = 0

for i in range(n):
    current_harvest = berries[i] + berries[(i + 1) % n] + berries[(i + 2) % n]
    max_harvest = max(max_harvest, current_harvest)

print(max_harvest)


import random

bushes = [random.randint(1,15) for _ in range(10)]

print(bushes)

max_berries = 0
for i in range(len(bushes)):
total = bushes[i-2] + bushes[i-1] + bushes[i]
if total > max_berries:
max_berries = total

print(max_berries)