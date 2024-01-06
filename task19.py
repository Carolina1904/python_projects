"""
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""
"""
list_1 = [1, 2, 3, 4, 5]
k = 3
list_2 = []
for i in range(len(list_1)):
    if (i+k)>len(list_1)-1:
        temp = i + k - len(list_1)
        list_2.append(list_1[temp])
    else:
        list_2.append(list_1[i+k])
print(list_2)
"""

lst = [1, 2, 3, 4, 5, 6]
lst_shifted = []
shift = 3
for i in range (len(lst)):
    lst_shifted.append(lst[(i+shift)%len(lst)])
print(lst_shifted)