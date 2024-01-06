"""
: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""
def sum_recursive(a, b):
    if b == 0:
        return a
    return sum_recursive(a + 1,b - 1)

a = int(input("enter first number: "))
b = int(input("enter the second one: "))

result = sum_recursive(a, b)
print(f"Summ of {a} and {b} is equal  {result} :)")