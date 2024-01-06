"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

Пример:
n = 385916 -> yes
n = 123456 -> no
"""
n = int(input("Enter the number of your ticket: "))
ticket_str = str(n)
if len(ticket_str) == 6:
    first_part_sum = sum(int(digit) for digit in ticket_str[:3])
    second_part_sum = sum(int(digit) for digit in ticket_str[3:])
    if first_part_sum == second_part_sum:
        print("YES")
    else:
        print("NO")

elif len(ticket_str) != 6:
    print("Not enough digits")
