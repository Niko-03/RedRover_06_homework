# ------- Условные операторы IF (если) и ELSE (иначе)--------
# проверяют, является ли значение выражения True
# x = 5
# print(x > 3 and not x < 8)         # False
# print(x > 3 and not x > 8)         # True

# if x == 5:
#     print('Five')
# else:
#     print('Not five')

# -------Оператор ELIF (означает ELSE IF - иначе если)
# для первого варианта - IF
# для промежуточных - ELIF
# для последнего условия - ELSE

# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than five')   # более пяти
# else:
#     print('Less than five')   # меньше пяти

# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print('Wecome!')
# else:
#     print('Go home, baby!')

# ------ про деление на ноль ------

# num1 = int(input('Number 1: '))    # 5
# num2 = int(input('Number 2: '))    # 0
# # operator = input('Operator: ')
# result = num1 / num2
# print(f'Result: {result}')

# ----- Домашнее задание (дописать калькулятор) ------
import sys

# num1 = int(input('Number 1: '))  # 5
# num2 = int(input('Number 2: '))    # 0
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#     try:                               # блок try/except
#         result = num1 / num2
#         print(f'Result: {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         # sys.exit()                      # выход из программы
#
# elif operator == '/':                   # деление
#     result = num1 / num2
#     print(f'Result: {result}')
#
# elif operator == '*':                    # умножение
#     result = num1 * num2
#     print(f'Result: {result}')
#
# elif operator == '+':                     # сложение
#     result = num1 + num2
#     print(f'Result: {result}')
#
# else:
#     result = num1 - num2                  # вычитание
#     print(f'Result: {result}')


'''---------ЦИКЛ WHILE (пока)------------

Три части цикла:
- оператор while
- условие - при каких условиях цикл работает (пока условие истино - цикл выполняется)
- тело - код цикла, который работает при указанном условии

- итерация - повторение цикла
- оператор break - выход из цикла
- оператор continue - переход к следующей итерации цикла

'''

# num = 0                    # переменная
# while num < 5:              # пока моё число < 5, выполняется цикл
#     print(num)
#     num += 1

# message = 'Hello!'
# i = 1                      # переменная, которая считает количество повторений нашего цикла (итерации)
# while i < 6:
#     print(i, message)
#     i += 1

# Это уже другой цикл (для примера, работает немного по другому)

# message = 'Hello!'
# i = 1
# while i < 6:
#     i += 1
#     print(i, message)

# message = 'Hello!'
# i = 1
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break                # выход из цикла
#     i += 1

# message = 'Hello!'
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:                  # если i=3 - пропускаем эту итерацию
#         continue                # переход к следующей итерации
#     print(i, message)


# i = 0
# x = 0
# while i < 4:
#     x += i
#     i += 1
#     print(f'x = {x}, i = {i}')   # как наглядно увидеть работу цикла
#     print(x)


'''---------ЦИКЛ FOR ------------

- for выполняет ту же функцию, что и while - повторяет указанные строки кода
- для работы for не требуется никаких условий
- используется для перебора последовательности (например, списка или строки)
- функция RANGE - для повторения цикла N раз

- FOR IN RANGE(N):   -- по умолчанию перебор с индекса 0 до индекса N (N исключается)
      PRINT(I)

- FOR IN RANGE(START, STOP, STEP):
      PRINT(I)     

'''

# for i in range(6):
#     print(i)

# for i in range(1, 9, 3):
#     print(i)

# for item in 'Hello':     # оператор in применяется для итерации внутри заданной последовательности (в этом случае - строка)
#     print(item)

# start = 5
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)


# def num():
#     return 2 * 2
#
#
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):             # start, stop, step - могут быть и функцией
#     print(i)

''' ----------- Про True и False --------
Как выражение становится булевым без явного указания

'''
# message = 'Hello'
# if message:               # переменная message - не пустая строка, поэтому её значение приравнивается к True
#     print(message)
# else:
#     print('The string is empty')    # если message - пустая строка, то её значение приравнивается к False (в кавычках - строка пустая)

# num = 21
# if num % 2:               # или (num != 0)
#     print('Нечетное')     # если (num % 2 = 1) - True, если (num % 2 = 0) - False
# else:
#     print('Четное')


''' --------- ФУНКЦИИ -----------
Функция DEF - в Python это объект, который принимает аргументы и возвращает значение.

DEF SUM(X, Y):
    RETURN X + Y

PRINT(SUM(5, 8))   >>> 13

Если функция задана, её можно вызвать в любом месте кода, и передать в неё какие-то аргументы
'''
#
# def num(num1, num2):
#     return num1 - num2
#
#
# print(num(10, 7))
# print(num(35, 12))

