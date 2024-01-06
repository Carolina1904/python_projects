"""
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2
"""

import math

n = int(input("Enter number of km in a day: "))
m = int(input("Enter total km: "))
result = (n+m-1)//n
print(f"We'll need {result} days!")
print(math.ceil(m/n))
print(f"We'll need {m//n + bool(m%n!=0)} days")