# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = list(map(float, input("Введите числа через пробел:\n").split()))

numbers1 = []
for i in range(len(numbers)):
    if numbers[i] % 1 != 0:
        numbers1.append(numbers[i])
numbers2 = [round(numbers1[i] % 1, 2) for i in range(len(numbers1))]
print(f"{numbers2} => {round(max(numbers2) - min(numbers2),2)}")