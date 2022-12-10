""" 
Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл 
многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или
 8*(x**4) + 5*x + 4 = 0 и т.д.

"""

from random import randint

k = int(input('Введите значение натуральной степени K: '))
f_path = 'task4_out.txt'
max_rand = 100


def rand_n(n):
    return randint(n, max_rand)

numbr = [rand_n(0) for i in range(k)]+[rand_n(1)]
polynom = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
                   j in enumerate(numbr) if j][::-1])
polynom = polynom.replace('x^1', 'x')
polynom = polynom.replace('x^0', '')
polynom += ('', '1')[polynom[-1] == '+']
polynom = (polynom, polynom[:-2])[polynom[-2:] == '^1']


with open(f_path, 'w') as data:
    data.write(str(polynom)+'=0') 


