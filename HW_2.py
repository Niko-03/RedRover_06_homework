''' ----- ДОМАШНЕЕ ЗАДАНИЕ ------------------------------------------------------------------------

Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре. 
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

'''

# health = int(input('Hi! How is your health? '))
# if health <= 0:                                                # <= по условию!
#     print('False')
# else:
#     print('True')



# health = int(input('Введите уровень здоровья вашего персонажа: '))  # вариант от препода
# if health > 0:
#     print('True')
# else:
#     print('False')



'''Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. 
Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

'''
# num = int(input('Please enter a number: '))
# if num % 2:                                  # num % 2 = 1  -- это True - и значит число нечётное!!
#     print('Нечётное')
# else:
#     print('Чётное')



# number = int(input('Введите любое число: '))   # вариант от препода
# if number%2:
#     print('Нечетное')
# else:
#     print('Четное')

'''Задание 2.3
Напишите программу, которая проверяет является ли год високосным. 
Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). 
Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

'''
# year = int(input('Please enter the year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Leap year')
# else:
#     print('Non-leap year')

# ------------------ от препода ------------------------------

# С вложенными условиями
# year = int(input())

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Високосный')
#         else:
#             print('Невисокосный')
#     else:
#         print('Високосный')
# else:
#     print('Невисокосный')



# C логическими операторами

# if not year % 4 and year % 100 or not year % 400:
#     print('Високосный')
# else:
#     print('Невисокосный')



'''Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. 
Текст и количество повторений нужно ввести с помощью input()

'''
# С циклом while

# text = input("Enter your text: ")

# num = int(input('Enter the number of repetitions: '))
# i = 1
# while i <= num:
#     print(i, text)
#     i += 1



# С циклом for

# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)




'''Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), 
производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

'''
# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#     try:                                               # блок try/except
#         result = num1 / num2
#         print(f'Result: {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#
# elif operator == '/':                                  # деление
#     result = num1 / num2
#     print(f'{num1} {operator} {num2} = {result}')
# #
# elif operator == '*':                                # умножение
#     result = num1 * num2
#     print(f'{num1} {operator} {num2} = {result}')
#
# elif operator == '+':                                 # сложение
#     result = num1 + num2
#     print(f'{num1} {operator} {num2} = {result}')
#
# else:
#     result = num1 - num2                              # вычитание
#     print(f'{num1} {operator} {num2} = {result}')


# от препода ===========================================================

# C указанием каждого оператора в отдельном условии
# try:
#     num1 = int(input('Пожалуйста, введите первое число: '))
#     num2 = int(input('Пожалуйста, введите второе число: '))
# except ValueError as e:
#     print(f'Введенное значение не является числом: {e}')
#     sys.exit()
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# if operator not in '+-*/%':
#     print("Вы ввели не правильный оператор!")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         sys.exit()
# elif operator == '+':
#     result = num1 + num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')



## C применением функции eval()
#
# try:
#     num1 = int(input('Пожалуйста, введите первое число: '))
#     num2 = int(input('Пожалуйста, введите второе число: '))
# except ValueError as e:
#     print(f'Введенное значение не является числом: {e}')
#     sys.exit()
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# if operator not in '+-*/%':
#     print("Вы ввели не правильный оператор!")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!")
# else:
#     result = eval(f'{num1} {operator} {num2}')
#     print(f'{num1} {operator} {num2} = {result}')
#


# на созвоне команды

# print("Привет! Угадаешь число, которе я загадала?")
# number = int(input("Введи любое число от 0 до 10 - "))
# while True:
#     if number == 0:
#         print("Холодно")
#         number = int(input("Попробуй другое число - "))
#     if number == 1:
#         print("Прохладно")
#         number = int(input("Попробуй другое число - "))
#     if number ==2:
#         print("Тепло")
#         number = int(input("Попробуй другое число - "))
#     if number ==3:
#         print("Горячо")
#         number = int(input("Попробуй другое число - "))
#     if number ==5:
#         print("Горячо")
#         number = int(input("Попробуй другое число - "))
#     if number ==6:
#         print("Тепло")
#         number = int(input("Попробуй другое число - "))
#     if number ==7:
#         print("Холодно")
#         number = int(input("Попробуй другое число - "))
#     if number == 8:
#         print("Ледяная глыба")
#         number = int(input("Попробуй другое число - "))
#     if number == 9:
#         print("Ледяная глыба")
#         number = int(input("Попробуй другое число"))


