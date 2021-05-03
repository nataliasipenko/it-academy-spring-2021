"""
Даны: три стороны треугольника. Требуется: проверить, действительно
ли это стороны треугольника. Если стороны определяют треугольник,
найти его площадь. Если нет, вывести сообщение о неверных данных.
"""
import math

a = float(input('Введите одну сторону треугольника: '))
b = float(input('Введите вторую сторону треугольника: '))
c = float(input('Введите третью сторону треугольника: '))

if a + b > c and b + c > a and c + a > b:
    perimeter = (a + b + c)
    square = math.sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))  # или **0.5
    print('Стороны определяют треугольник с площадью: ', square)
else:
    print('Неверные входные данные')
