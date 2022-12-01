"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных индексах. Индексы вводятся 
одной строкой, через пробел.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
--> 0 2 3
-3 * -1 * 0 = 0
Вывод: 0
"""


def list_n(n):
    for i in range(-n,n+1):
        list.append(i)
    return list

def product_i(s):
    m = list[int(s[0])]
    for i in range(1,len(s)):
        m =m * list[int(s[i])]
    return m
    
list = []
# n = int(input("Введите число N: "))
print(list_n(int(input("Введите число N: "))))
# s = input("Введите индексы через пробел: ").replace(" ","")
print(f'Произведение равно: {product_i(input("Введите индексы через пробел: ").replace(" ",""))}')
