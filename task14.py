"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
"""


def powers_of_two_up_to_n(n):
    power_of_two = 1
    while power_of_two <= n:
        print(power_of_two)
        power_of_two *= 2

n = int(input("Enter the number N: "))
powers_of_two_up_to_n(n)