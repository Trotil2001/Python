""" 
Вычислить число c заданной точностью d

Пример:

- при d = 0.001, π = 3.141   
Ввод: 0.01
    Вывод: 3.14

    Ввод: 0.001
    Вывод: 3.141

"""


from math import pi

n_pi=pi
print(n_pi)
d=len(input('Введите точность d: ').split('.')[1])
str = f'%.{d}f' % n_pi
print(str)




