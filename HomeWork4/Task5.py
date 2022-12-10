""" 
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов 
(складываются числа, у которых "х" в одинаковых степенях). 
Пример того, что будет в итогвом файле: 
8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

"""

""" 

не получается получить спикок всех коэффициентов многочлена

 """


import re
import numpy as np
lis = []
list_s = []
count_d = ''
count = 0
str_dec = ''
koef = ''



f1_in_path = 'task5_in1.txt'
f2_in_path = 'task5_in2.txt'
f_out_path = 'task5_out.txt'


def read_f(path_f):
    with open(path_f, 'r', encoding='utf-8') as data_in:
        return data_in.read()


def write_f(path_f, str_f):
    with open(path_f, 'w', encoding='utf-8') as data_encod_out:
        data_encod_out.writelines(str_f)


def convert_pol(pol):
    num = ''
    pol = pol.replace('=0', '')
    pol = pol.replace('^','')
    print(pol)
    
    # for item in pol:
    for i in pol:
            if i.isdigit():
              num += i
              # print(num)
            elif i == pol.find(i)-1:
              print(i)
              lis.append(num)
              print(num)
            elif i == 'x':
              lis.append(num)
              num = ''
            else:
                if num == '':num = '1'
                list_s.append(num)
                # print(num)
                num = ''
    return pol


# str1 = '53x^2+7x+4=0'
str1 = read_f(f1_in_path)
# str2 = read_f(f2_in_path)
# k = str1.split('+')

print(str1)
# print(str2)
pol_1 = convert_pol(str1)
# pol_2 = convert_pol(str2)
print(lis)
print(list_s)
# sum_pol=np.polyadd(pol_1, pol_2)
# print(sum_pol)
