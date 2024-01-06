"""
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""
number_a = int(input("Enter a number: "))

fib_number, fib_number1 = 0, 1
counter = 2

while fib_number + fib_number1 < number_a:
    fib_number, fib_number1 = fib_number1, fib_number + fib_number1
    counter += 1

if number_a == 0:
    print(1)
elif number_a == 1:
    print("It can be either 2 or 3")
elif fib_number + fib_number1 == number_a:
    print(counter + 1)
else:
    print(-1)
