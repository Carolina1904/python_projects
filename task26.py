"""
: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
"""
def power_recursive(a, b):
    if b ==0:
        return 1
    return a * power_recursive(a, b - 1)

a = float(input("enter number A: "))
b = int(input("enter number B: "))

result = power_recursive(a, b)
print(result)