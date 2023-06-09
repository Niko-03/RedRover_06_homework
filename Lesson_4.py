''' --------- ФУНКЦИЯ (FUNCTION) -----------------------------------------------------------
- def - это именованный фрагмент кода, отделённый от других;
- может принимать любое количество любых входных параметров,
  и возвращать любое количество любых результатов;
- функция - это объект, поэтому её можно
                                    присваивать переменной,
                                    передавать в качестве аргумента,
                                    возвращать из других функций.

Синтаксис:

def calc(a, b):
    print(a)
    print(d)
    return a + b


- Параметр функции - это имя в списке параметров в первой строке определения функции (получает своё значение при вызове функции)
- Аргумент - это реальное значение (или ссылка на него), переданное функции при вызове.

DEF SUM(X, Y):     -- X, Y - это параметры функции SUM
    RETUTN X + y

SUM(1, 2)          -- 1, 2 - это аргументы функции


- Позиционные аргументы (positional argument) - значения копируются в соответствующие параметры по порядку.
- Именованные аргументы (keyword argument) -передаются как пара "имя=значение", и их можно передавать в любом порядке.
- Позиционные аргументы указываются до именованных аргументов, но порядок можно не соблюдать,
  если указать позиционный аргумент по имени.

def add_it(a, b, c = 3):          или так:        def add_it(a, b, c = 3):
    return a + b + c                                  return a + b + c

add_it(8, 10, c = 5)                               add_it(b = 8, a = 10, c = 5)


------ Встроенные функции --------------
# print(sum())
# print(min())
# print(max())


-------- АНОНИМНЫЕ ФУНКЦИИ: LAMBDA-ВЫРАЖЕНИЯ -------------------------------

- могут содержать только одно выражение (выполняются быстрее);
- обычно применяются в функциях высшего порядка (это функция (высокоуровневая), которая взаимодействует с другими функциями или возвращает другие функции);
- создаются с помощью инструкции lambda, их не обязательно присваивать переменной (в отличие от обычной функции);
- lambda-функции не требуется инструкция return.


------- Синтаксис ------------

lambda argument: manipulat(argument)
lambda n: n*n

func = lambda x, y: x * y         # пример
print(func(2, 5))


--------------- ФУНКЦИЯ ВЫСОКОГО УРОВНЯ (высшего порядка, высокоуровневая)------------------------------

- взаимодействует с другими функциями или возвращает другие функции
  (принимает в качестве аргумента другие функции, например lambda).

- map  -  применит указанное действие к каждому элементу последовательности
- filter  -  отфильтрует элементы последовательности по заданным параметрам (условиям)
- reduce  -  приведёт к одному результату элементы последовательности (всё перемножит, или сложит, или разделит...)


----------------------- ДЕКОРАТОРЫ -----------------------------
- это функция, которая в качестве параметра получает функцию, и в качестве результата также возвращает функцию;
- декораторы позволяют модифицировать выполняемую функцию, значения её параметров и её результат без изменения исходного кода этой функции
  (то есть, декоратор позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода).

DEF DECORATOR_FUNCTION(FUNC):
    DEF WRAPPER():
        PRINT('Функция-обёртка!)
        PRINT(F'Оборачиваемая функция: {FUNC}')
        PRINT('Выполняем обёрнутую функцию...')
        FUNC()
        PRINT('Выходим из обёртки')
    RETURN WRAPPER

----------------------- МОДУЛИ ----------------------------------------------------------------------
- это отдельный файл с кодом, который можно повторно использовать в других программах;
- каждая программа может импортировать модуль и получить доступ к его классам, функциям и объектам;
- модули позволяют разбивать огромные программы на небольшие кусочки кода, которыми легко управлять и организовывать.


---------------------------ПРОСТРАНСТВО ИМЕН в Python (NAMESPACE)--------------------------------------------
- место, где хранится переменная
- реализованы в виде словарей, где ключи - это имена объектов,
                                   значения - это сами объекты


- ВСТРОЕННОЕ ПРОСТРАНСТВО (BUILT-IN) имён содержит имена всех встроенных объектов Python

- ГЛОБАЛЬНЫЕ (GLOBAL) ПРОСТРАНСТВА имён содержат имена на уровне основной программы,
  поэтому переменные, находящиеся в нём, являются ГЛОБАЛЬНЫМИ

- ЗАМКНУТОЕ (ENCLOSED) ПРОСТРАНСТВО имён включает имена, определённые внутри внешней функции

- ЛОКАЛЬНОЕ (LOCAL) ПРОСТРАНСТВО имён включает в себя локальные имена внутри функции.
  Переменные, которые находятся внутри функций, называются ЛОКАЛЬНЫМИ


- ПРИОРИТЕТНОСТЬ:             Built-In
                            ^
                              Global
                            ^
                              Enclosed
                            ^
                              Local
                                ^
                                ^
                          Variable Lookup

- поиск переменной всегда изнутри наружу


------------ ОБЛАСТЬ ВИДИМОСТИ (SCOPE) -----------------------------------
- если пространство имен (namespace)- это словарь для хранения всех переменных,
  то область видимости (scope) - это правило, по которому выполняется поиск привязок (значение с назначенным именем).


'''


# def calc(a, b):          # def - ключевое слово, calc - имя функции, a и b -параметры функции
#     # print(a)           # тело...
#     # print(b)           # тело функции
#     return a + b         # возвращаемое значение
#
#
# print(calc(7, 12))       # вызов функции, здесь в скобках - аргументы функции

# ------------------------------------------------------------------------------------------------------------------
# def person(age, f_name, l_name):                                          # позиционные аргументы
#     return f'Hello! My name is {f_name} {l_name}. I am {age} years old.'
#
#
# print(person(25, 'Tom', 'Smit'))                            # при вызове функции указываются в том же порядке, что и при определении функции
# print(person(l_name='Smit', f_name='Tom', age=25))          # при таком синтаксисе порядок не имеет значения


# ------ Встроенные функции --------------
# print(sum([5, 6, 7, 2, 15]))
# print(min(5, 6, 7, 2, 15))
# print(max(5, 6, 7, 2, 15))

# ------------------------------------------------------------------
# def pattern(length, char1, char2):
#     return (char1 + char2) * length + char1
#
#
# print(pattern(8, '*', '-'))

# --------------------------------------------------------------------------
# def pattern(length, char2, char1='*'):
#     return (char1 + char2) * length + char1
#
#
# print(pattern(8, '/'))
# print(pattern(8, '-', char1='*'))
# print(pattern(8, '/', char1='+'))
# print(pattern(8, char1='*', char2='--'))          # и так далее...


# -------- LAMBDA ФУНКЦИИ ----------------------------------------

# mult = lambda x, y: x * y          # умножение (здесь функцию lambda присвоили переменной mult, т.к. здесь не используется функция высшего порядка)
# print(mult(10, 2))
#
# div = lambda x, y: x / y            # деление
# print(div(10, 2))
#
# add = lambda x, y: x + y           # сложение
# print(add(10, 2))
#
# subt = lambda x, y: x - y            # вычитание
# print(subt(10, 2))


# -------------- применение lambda-функций --------------------------------------------------------

# lst = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lst))      # отфильтруем из нашего списка только чётные значения, или нечётные, или str...
# filtered = list(filter(lambda x: isinstance(x, int) or isinstance(x, float), lst))      # отфильтруем из нашего списка все цифры
# filtered = list(filter(lambda x: not isinstance(x, str), lst))                          # или так отфильтровать только цифры
# filtered = list(filter(lambda x: isinstance(x, str), lst))                              # отфильтровать строки (без list() получим filter object!!)
# print(filtered)                                                                         # получили отфильтрованный объект
# print(*filtered)                                                                        # * - оператор распаковки

# lst1 = [20, 15, 8, 7, 6]
# power = list(map(lambda x: x ** 2, lst1))      # map применит указанное действие к каждому элементу последовательности
# print(power)
#
# power1 = list(map(lambda x: x ** 2 if isinstance(x, int) else x, lst))
# print(power1)


# from functools import reduce                     # приведет к одному результату элементы последовательности (всё перемножит, или сложит, или разделит...)
# result = reduce(lambda x, y: x - y, lst1)        # или x*y, или x+y, или x/y...
# print(result)


## ------------ ДЕКОРАТОРЫ ----------------
## ------- пример функции без аргумента ----------------
# def my_decorator(func):                # функция-декоратор - в качестве аргумента передаём нашу функцию
#     def wrapper():                     # функция-обёртка
#         print('Я - обёртка!')          # то, что внутри обёртки
#         func()                         # вызов нашей функции
#         print('Завернули')             # окончание заворачивания
#     return wrapper()
#
#
# @my_decorator                          # эта запись о том, что наша функция обёрнута декоратором
# def say_hello():                       # простая функция, без аргумента
#     print(f'Hello!')

# say_hello = my_decorator(say_hello)            # и эта запись тоже о том, что наша функция обёрнута декоратором (синтаксический сахар)

## -------- пример функции с аргументом ----------------

# def my_decorator(func):                # функция-декоратор - в качестве аргумента передаём нашу функцию (любую функцию)
#     def wrapper(arg):                  # функция обёртки
#         print('Я - обёртка!')          # то, что внутри обёртки - этот print для наглядности
#         func(arg)                      # вызов нашей функции (с аргументом, может принимать произвольное кол-во элементов **arg), которую оборачиваем
#         print('Завернули')             # окончание заворачивания - строка не обязательная, просто для наглядности
#     return wrapper                     # вернули обёртку
#
#
# @my_decorator                          # эта запись о том, что наша функция обёрнута декоратором
# def say_hello(name):                   # наша функция с аргументом
#     print(f'Hello, {name}!')           # то, что должна сделать наша функция (вывести фразу)
#
#
# say_hello('Tom')                       # вызов функции с переданным аргументом

## ещё пример, приготовим кофе -------------

# def milk(func):                    # первый декоратор (с молоком)
#     def wrapper():
#         print('milk')
#         func()
#     return wrapper
#
#
# def not_milk(func):                    # второй декоратор (без молока)
#     def wrapper():
#         print('not milk')
#         func()
#     return wrapper
#
#
# def sugar(func):                    # третий декоратор (с сахаром)
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
#
#
# def not_sugar(func):                    # четвёртый декоратор (без сахара)
#     def wrapper():
#         print('not sugar')
#         func()
#     return wrapper
#
#
# @sugar                           # это кофе с сахаром и молоком
# @milk
# def coffee():                    # сама функция
#     print('Coffee')
#
#
# coffee()                         # вызвали нашу функцию
#
#
# @not_sugar                       # чёрный кофе
# @not_milk
# def coffee():
#     print('Coffee')
#
#
# coffee()
#
#
# @not_sugar                      # кофе с молоком
# @milk
# def coffee():
#     print('Coffee')
#
#
# coffee()
#

# -------- -- синтаксис декоратора -----------------
# DEF DECORATOR_FUNCTION(FUNC):
#     DEF WRAPPER():
#         PRINT('Функция-обёртка!)
#         PRINT(F'Оборачиваемая функция: {FUNC}')
#         PRINT('Выполняем обёрнутую функцию...')
#         FUNC()
#         PRINT('Выходим из обёртки')
#     RETURN WRAPPER


## ----------- посчитать время выполнения функции -----------

# import time                       # импортировали модуль (все импорты всегда в начале файла!!)
# print(time.time())                # текущее время


# import datetime                   # более информативная
# print(datetime.date.today())      # дата сегодня


# bdate = 1980                                 # дан год рождения
# current_date = datetime.date.today()         # переменная определяет дату сегодня
# age = current_date.year - bdate              # из сегоднешней даты берём только год и вычитаем год рождения
# current_month = current_date.month           # месяц текущей даты
#
# print(age)                                   # получаем возраст
# print(current_month)                         # текущий месяц


''' -------------------- импорт модулей ------------------

 --------- способы импорта модулей ------------------

- это встроенные методы, но можно создать свой метод, и импортировать его

import math                 # импорт модуля математических операций
import math as m            # переименование модуля с длинным названием (в коде используем сокращённое название m)
from math import  *         # взять всё из модуля
from math import sum        # из модуля math берём только функцию сложения (пример)
'''
# import math as m
#
# l = [3, 5, 6, 9, -12]
# print(m.prod(l))              # перемножить все цифры списка (без lambda функции)

# -------------------------------------------------------------------------------------------------

# from math import ceil           # округление до ближайшего большего числа
#
# l1 = [3, 5, 6.12, 9, -12.3, 7, 56.8, -35]
# print(sum(l1))
# print(ceil(sum(l1)))

''' ----------------- Создание своего метода ------------

чтобы импортировать свой модуль в другой файл, пишем так:
import <имя файла с модулем>

'''
# import Lesson_4_module
# print(Lesson_4_module.hello('Sam'))

# import Lesson_4_module as les                              # или так (укоротили название метода)
# print(les.hello('Tom'))

# from Lesson_4_module import hello                          # из всего файла импортировали только метод hello
# print(hello('Piter'))

# from Lesson_4_module import hello as h                      # так же можно сократить запись и для отдельного модуля
# print(h('Piter'))

# from Lesson_4_module import result                             # или только метод sum
# from Lesson_4_module import hello, result                    # или так импортировать только два метода
# from Lesson_4_module import hello as h, result as r          # или так - сократить названия методов
# from Lesson_4_module import *                                # или так импортировать всё, что есть
# print(result(7, 5))



# ---------------- про пространство имен ------------------------------------------------

'''
- ВСТРОЕННОЕ ПРОСТРАНСТВО (BUILT-IN) имён содержит имена всех встроенных объектов Python

- ГЛОБАЛЬНЫЕ (GLOBAL) ПРОСТРАНСТВА имён содержат имена на уровне основной программы,
  поэтому переменные, находящиеся в нём, являются ГЛОБАЛЬНЫМИ

- ЗАМКНУТОЕ (ENCLOSED) ПРОСТРАНСТВО имён включает имена, определённые внутри внешней функции

- ЛОКАЛЬНОЕ (LOCAL) ПРОСТРАНСТВО имён включает в себя локальные имена внутри функции.
  Переменные, которые находятся внутри функций, называются ЛОКАЛЬНЫМИ

'''

# print(dir(__builtins__))     # увидим все объекты на встроенном уровне built-in


# l = [3, 5, 6, 9, -12]      # глобальный уровень (пример)
# print(globals())           # объекты на глобальном уровне global

## --------------------------------------------------------------------------------------------------
# def pattern(length=8, char2='/', char1='*'):
#     pattern_1 = (char1 + char2) * length + char1
#     print(f'Locals: {locals()}')                        #  объекты на локальном уровне local
#
#
# pattern()

# print(pattern_1)                                        # будет ошибка потому, что эта переменная локальная, объявлена внутри функции


## --------------------------------------------------------------------------------------------------
# var = 'global'                                          # здесь переменная объявлена на глобальном уровне
# def func1():                                            # внешняя функция
#     def local():                                        # внутренняя функция
#         print(var)
#     local()
# func1()


## --------------------------------------------------------------------------------------------------
# def func2():                                            # внешняя функция
#     var = 'enclosed'                                    # здесь переменная объявлена внутри внешней функции
#     def local():                                        # внутренняя функция
#         print(var)
#
#     local()
#
#
# func2()


## --------------------------------------------------------------------------------------------------
# def func3():                        # внешняя функция
#     var = 'enclosed'                # здесь переменная объявлена внутри внешней функции
#     def local():                    # внутренняя функция
#         var = 'local'               # здесь переменная объявлена на локальном уровне
#         print(var)
#
#     local()
#
#
# func3()


















