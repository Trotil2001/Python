"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""

import random


def num_list(n):
    for i in range(n):
        list.append(random.randint(0, 10))
    return list


def sum_pairs():
    m = len(list)//2
    for i in range(m if (len(list) % 2 == 0) else m+1):
        list_sum.append((list[i]*list[-i-1]))
    return list_sum


list = []
list_sum = []
n = int(input('Введите размер списка: '))
print(f'{num_list(n)} => {sum_pairs()}')

