"""
Задайте список из нескольких чисел. Напишите программу, которая 
найдёт сумму элементов списка, стоящих на нечётной идексах.

Пример:

[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

"""

import random


def num_sum(n):
    sum_num = 0
    for i in range(n):
        list.append(random.randint(0, 10))
        if i % 2 != 0:
            sum_num += list[i]
            not_even.append(list[i])
    return sum_num


list = []
not_even = []
n = int(input('Введите размер списка: '))
print('{1}\n{2} Сумма: {0}'.format(num_sum(n),list, not_even))
