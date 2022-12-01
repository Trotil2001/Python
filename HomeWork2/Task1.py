'''
Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.

Пример:

0,56 -> 11 
'''


def sum_num(n):
    sum_dig = 0
    for i in range(len(n)):
        if (n[i] != ".") and (n[i] != ","):
            sum_dig += int(n[i])
        else:
            continue
    return sum_dig


def sum_num1(n):
    if "," in n:
        print(f"Сумма его цифр: ",sum(map(int, n.replace(",",""))))
    else:
        print(f"Сумма его цифр: ",sum(map(int, n.replace(".",""))))


n = input("Ввведите число N: ")
print(f"Сумма его цифр: ", sum_num(n))
print()
sum_num1(n)
