"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""

number = int(input('Введите целое положительное число произвольной длины: '))
reversion_of_number = 0
n = number


while n > 0:
    digit = n % 10
    reversion_of_number = reversion_of_number * 10 + digit
    n = n // 10

if number == reversion_of_number:
    print('Введенное число является палиндромом')
else:
    print('Введенное число не является палиндромом')
