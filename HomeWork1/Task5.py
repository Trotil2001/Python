# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21+
ax = int(input("Введите координаты 'X' точки A: "))
ay = int(input("Введите координаты 'Y' точки A: "))
bx = int(input("Введите координаты 'X' точки B: "))
by = int(input("Введите координаты 'Y' точки B: "))
print("Растояние между точками =", round((((ax-bx)**2 + (ay-by)**2)**0.5),2))