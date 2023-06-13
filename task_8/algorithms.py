#  Линейные алгоритмы
#1
# def gramms_to_kilogramms():
#     gramms = float(input("Введите значение в граммах: "))
#     kilogramms = gramms / 1000
#     print("Результат в килограммах:", kilogramms)
#

#2
# x = 10
# y = 55
# print("Значения переменных до замены:")
# print("x =", x)
# print("y =", y)
#
# temp = x
# x = y
# y = temp
#
# print("Значения переменных после замены:")
# print("x =", x)
# print("y =", y)

#3
# L = float(input("Введите расстояние в метрах: "))
# kilometers = L // 1000
# print("Количество полных километров:", kilometers)


#4
# num = int(input("Введите целое число: "))
# reversed_num = int(str(num)[::-1])
# print("Обратное число:", reversed_num)

#5
# from datetime import date
#
# today = date.today()
# formatted_date = today.strftime("%d.%m.%Y")
#
# print("Текущая дата в формате 'год-месяц-день':", today)
# print("Текущая дата в формате 'день.месяц.год':", formatted_date)


# Логические выражения

#1
# x = 75
# y = 90
# z = 70
#
# if x > 80 or y > 80 or z > 80:
#     print("Условие истинно: хотя бы одно из чисел больше 80")
# else:
#     print("Условие ложно: все числа меньше или равны 80")

#2
# a = 10
# b = -5
#
# if (a > 0 and b > 0) or (a < 0 and b < 0):
#     print("Условие истинно: оба числа одновременно положительны или отрицательны")
# else:
#     print("Условие ложно: числа имеют разные знаки или одно из чисел равно нулю")

#3
# a = 130
# b = 25
# c = 70
#
# min_value = min(a, b, c)
#
# print("Наименьшее число:", min_value)

#4
# a = 130
# b = 25
# c = 70
#
# min_value = a  # Предполагаем, что 'a' - наименьшее число
#
# if b < min_value:
#     min_value = b
#
# if c < min_value:
#     min_value = c
#
# print("Наименьшее число:", min_value)
#

#Циклы
#1
# string = 'Python - это Питон!'
# count = 0
#
# for char in string:
#     count += 1
#
# print("Количество символов (с помощью цикла for):", count)
#
# string = 'Python - это Питон!'
# count = 0
# index = 0
#
# while index < len(string):
#     count += 1
#     index += 1
#
# print("Количество символов (с помощью цикла while):", count)

#2
# my_list = [1, '2', 3, 4, '5']
# total_sum = 0
#
# for item in my_list:
#     if isinstance(item, str):
#         item = int(item)
#     total_sum += item
#
# print("Сумма всех элементов списка:", total_sum)

#3
# a = 'abcde123'
# b = 'bad_cat_23'
# for i in a:
#     if i in b:
#         print(f'Символ {i} есть в "bad_cat_23".')
#     else:
#         print(f'Символа {i} нет в "bad_cat_23".')

# str1 = 'abcde123'
# str2 = 'bad_cat_23'
#
# for char in str1:
#     if char in str2:
#         print('Символ "{}" есть в "{}".'.format(char, str2))
#     else:
#         print('Символа "{}" нет в "{}".'.format(char, str2))

# 4
# for i in range(2, 20):
#     if i % 2 == 0:
#         for j in range(2, 10):
#             print('/ \_', end='')
#     else:
#         for j in range(2, 10):
#             print('\_/ ', end='')
#     print('')

#5


# Функции
import random


def generate_password(length):
    password = ""
    for _ in range(length):
        char_type = random.randint(0, 2)
        if char_type == 0:
            # Генерация случайной цифры (диапазон 48-57)
            password += chr(random.randint(48, 57))
        elif char_type == 1:
            # Генерация случайной буквы в верхнем регистре (диапазон 65-90)
            password += chr(random.randint(65, 90))
        else:
            # Генерация случайной буквы в нижнем регистре (диапазон 97-122)
            password += chr(random.randint(97, 122))

    return password


# Генерация и вывод трех паролей
for _ in range(3):
    password = generate_password(random.randint(8, 15))
    print(password)


