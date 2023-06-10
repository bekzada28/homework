# end_1 = int(input(''))
# start_1 = int(input(''))

# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     sum_1 = 0
#     for i in range(start, end+1):
#         sum_1 += i
#     return sum_1
#
# print(sum_range(4, 1))
#
# #2
# def date(day, month, year: int):
#     if day <= 0 or month <= 0 or year < 0:
#        return False
#     else:
#         months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:  months[1] = 29
#     if day <= months[month - 1]:
#         if month <= 12:
#             return True
#     return False
#
# print(date(4,5,2022))
#

#3

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# num = int(input("Введите число от 0 до 1000: "))
# print(is_prime(num))

4

# def square(side):
#     perimeter = 4 * side
#     area = side ** 2
#     diagonal = (2 * side ** 2) ** 0.5
#     return (perimeter, area, diagonal)
# print(square(3))

#5

# def is_year_leap(year):
#     year = int(input('Ведите год: '))

#     if (year % 4 and not year % 100) or year % 400:
#         print('Високосный')
#     else:
#         print('Невисокосный')

# def is_year_leap(year):
#     """
#     Принимает аргумент: порядковый номер года
#     Возвращает значение: если високосный год - True, иначе - False
#     """
#     if year % 4 != 0:
#         return False
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         return True

# def date(day, month, year):
#     """
#     Принимает аргументы: день, месяц, год
#     Возвращает значение: если дата правильная - True, иначе - False
#     """
#     # Задаем количество дней в месяцах невисокосного года
#     set_months = {1: 31,
#                   2: 28,
#                   3: 31,
#                   4: 30,
#                   5: 31,
#                   6: 30,
#                   7: 31,
#                   8: 31,
#                   9: 30,
#                   10: 31,
#                   11: 30,
#                   12: 31}
#     # Проверяем заданы ли верно год и месяц
#     if year > 0 and (month >= 1 and month <= 12):
#         # Изменяем количество дней для февраля в високосных годах
#         if month == 2 and is_year_leap(year) == True:
#             set_months[2] = 29
#         # Проверяем задан ли верно день
#         if day in range(1, set_months[month]+1):
#             return True
#         else:
#             return False
#     else:
#         return False
# # Тест кейсы
# print(date(31, 12, 2020)) # Правильная дата
# print(date(1, 0, 2000)) # Месяц вне диапазона
# print(date(1, 1, 0)) # Год вне диапазона
# print(date(29, 2, 2000)) # 29 февраля високосный год
# print(date(29, 2, 1900)) # 29 февраля невисокосный год

# users_day = int(input('Введите день :'))
# users_month = int(input('Введите месяц :'))
# users_year = int(input('Введите год :'))
# user_date = {users_day:users_month}

# # print (date(users_day,users_month,users_year))

# def date (day,month,year):
# #создаем месяца с количеством дней {m,d}
#     month_day = { 1:31 , 2:28 , 3:31 , 4:30 , 5:31 ,
#     6:30 , 7:31 , 8:31 , 9:30 , 10:31,
#     11:30 , 12:31
#     }
#     real_year = (range(2020))
# #меняем значения февраля, если он високосный
#     if year % 4 == 0:
#         month_day = 29
#     if year % 4 == 0 and year % 100 == 0:
#         month_day = 28
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         month_day = 29
#     if user_date in month_day:
#         print('Верная дата')
#     else:
#         print('не верная дата')

# print (date(users_day,users_month,users_year))



#6

# def arithmetic(number_1, number_2, operation):
#
#     if operation == '+':
#         return number_1 + number_2
#     elif operation == '-':
#         return number_1 - number_2
#     elif operation == '*':
#         return number_1 * number_2
#     elif operation == '/':
#         return number_1 / number_2
#     else:
#         return "Неизвестная операция"


# 7

def bank(a, years):
    percent = 0.1
    balance = a
    for _ in range(years):
        balance += balance * percent
    return balance


