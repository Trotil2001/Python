# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек
# в этой четверти (x и y).

n = int(input("Введте номер четверти: "))
if n == 1:
    print("диапазон возможных координат точек 'x' и 'y' от 0 до +∞")
elif n == 2:
    print("диапазон возможных координат точек 'x' от 0 до -∞, 'y' от 0 до +∞")
elif n == 3:
    print("диапазон возможных координат точек 'x' от 0 до -∞, 'y' от 0 до -∞")
elif n == 4:
    print("диапазон возможных координат точек 'x' от 0 до +∞, 'y' от 0 до -∞")
