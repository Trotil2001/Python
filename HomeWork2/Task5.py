"""
Реализуйте алгоритм перемешивания списка.
"""

import random

n=int(input('Введите размер списка: '))
list = []
for i in range(0,n):
    list.append(random.randint(0,10))
print(list)


random.shuffle(list)
print(list)


