""" 
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

"""

# s = 'Я люблю абвЖвау иабв Питон'
f_in_path = 'Task1_in.txt'
f_out_path = 'Task1_out.txt'
repl='абв'

def open_r():
    with open(f_in_path, 'r',encoding='utf-8') as data_in:
        str1=data_in.read()
    return str1
str1=open_r()
print(str1)


res = ' '.join([i for i in str1.split() if repl not in i])

def open_w(res):
    with open(f_out_path, 'w',encoding='utf-8') as data_out:
        data_out.writelines(res)
open_w(res)
print(res)

