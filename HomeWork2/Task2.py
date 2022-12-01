'''
Напишите программу, которая принимает на вход число N и
выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''


def number_product(n):
    num = 1
    for i in range(1, n+1):
        num *=i
        list.append(num)
    return list

list = []
n = int(input("Введите число N: "))
print(number_product(n))
