""" 

Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной 
последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
Вывод: [2, 3]
"""

numbers = [1, 1, 2, 3, 4, 4, 4]


def unique(numbers):
    res = []
    for item in numbers:
        if numbers.count(item) == 1:
            res.append(item)
    return res


print(f'Исходный список {numbers}')
print(f'Список неповторяющихся элементов {unique(numbers)}')
