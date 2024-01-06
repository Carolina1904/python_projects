"""
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
import random
watermelon = int(input("Enter number of watermelons: "))
max_amount = 0
min_amount = 100
for _ in range(watermelon):
    amount = random.randint(1, 10)
    print(amount, end=', ')
    if amount>max_amount:
        max_amount=amount
    if amount<min_amount:
        min_amount=amount
print()
print(f"Max watermelon is {max_amount} kg and min watermelon is {min_amount} kg")


