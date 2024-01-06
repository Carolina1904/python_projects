"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание:
Простое число - это число, которое имеет 2 делителя: 1 и n(само число) Input: 5 Output: yes
"""
def prime_number(number):
    if number in (1, 2):
        return True
    if not number % 2:
        return False
    for i in range(2, int(number ** 0.5), 2):
        if not number % i:
            return False
    return True
print(prime_number(int(input("enter a number: "))))