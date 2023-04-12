''' ----- ДОМАШНЕЕ ЗАДАНИЕ ---------------------------------------------------------------------
4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.

----------- Справочно ------------
# print("%.1f" % number)
# number - это твоё число которое ты хочешь округлить, 1 знак после запятой будет

# Формула диагонали квадрата через длину стороны: D = корень.кв из (x * x * 2)

'''

from math import sqrt
# import math
#
#
# def square(x):
#     perimetr = x * 4                                           # периметр
#     area = x * x                                               # площадь
#     diagonal = (float('%.2f' % math.sqrt(x * x * 2)))          # диагональ ("%.1f" % number -- эта запись позволяет округлить число)
#     # diagonal = math.ceil(math.sqrt(x * x * 2))               # ещё про диагональ, math.ceil округлит цифру до целого числа
#     return (perimetr, area, diagonal)
#
#
# result = square(5)
#
# print(result)
# print(type(result))

# ---------------- вариант_2 - после ревью ----------------------------------

# from math import sqrt
#
# def square(side):
#   return (side**2, side*4, round(sqrt(side**2*2), 2))       # цифра 2 в конце скобок - это округление диагонали до 2-х знаков
#
# print(tuple(square(5)))





'''
4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
в формате аргумент:значение. Например:
name: John
last_name: Smith
age: 35
position: web developer
'''

# def person(**kwargs):                          # запись **kwards - означает: прими произвольное количество именованных аргументов
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# person(f_name='John', l_name='Smith', age=27, position='web developer')





'''
4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
положительные числа.
'''
# my_list = [20, -3, 15, 2, -1, -21]
# filtered = list(filter(lambda x: x >= 0, my_list))
#
# print(filtered)
# print(id(my_list))
# print(id(filtered))


# ---------------- вариант_2 - после ревью ----------------------------------
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))



'''
4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке.

--- Справочно ---
- Модуль functools - сборник функций высокого уровня: взаимодействующих с другими функциями или возвращающие другие функции.

- Функция reduce принимает 2 аргумента: функцию и последовательность. 
reduce() последовательно применяет функцию-аргумент к элементам списка, возвращает единичное значение. 
(в Python 2.x функция reduce доступна как встроенная, в то время, как в Python 3 она была перемещена в модуль functools)

'''

# from functools import reduce
#
# my_list = [20, -3, 15, 2, -1, -21]
# result = reduce(lambda x, y: x * y, my_list)           # или x+y, или x-y, и т.д.
# print(result)


# ---------------- вариант_2 - после ревью ----------------------------------

# from functools import reduce
# print(reduce(lambda x, y: x*y, my_list))


# Чтобы получить результат перемножения только положительных значений

# print(reduce(lambda x, y: x * y, [x for x in my_list if x > 0]))


# ---------------- вариант_3 - без lambda ----------------------------------
'''
Модуль Math в Python содержит ряд математических операций, которые можно легко выполнить с помощью модуля. 
math.prod()метод в Python используется для вычисления произведения всех элементов, присутствующих в данном итерируемом объекте . 
Большинство встроенных контейнеров в Python, таких как list, tuple, являются итерируемыми. 
Итерируемый объект должен содержать числовое значение, иначе нечисловые типы могут быть отклонены.
Этот метод является новым в Python версии 3.8.

Синтаксис: math.prod(iterable, *, start = 1)

Параметры:
iterable : итерируемый объект, содержащий числовые значения
start : целое число, представляющее начальное значение. start — это именованный (только ключевое слово) параметр, значение по умолчанию — 1.

Возвращает: вычисленное произведение всех элементов, присутствующих в данной итерации.

'''

# import math
# my_list = [20, -3, 15, 2, -1, -21]
# mult = math.prod(my_list, start=1)      #  без lambda
#
# print(mult)




'''
4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра.


подсказка на лекции print(time.perf_counter()) - определить начало работы функции,
и вызвать это ещё раз, чтобы отметить конец работы функции

time.sleep(5)  - задержка начала работы функции в секундах

'''
# import time
#
#
# def decor_time(func):                             # ничего не понимаю, разобраться..........
#     def wrapper(*arg, **kwargs):
#         start_time = time.time()
#         result = func(*arg, **kwargs)
#         end_time = time.time()
#         print(f'Функция {func.__name__} работает {end_time - start_time:.8f} секунд')
#         return result
#     return wrapper


# @decor_time
# def func_a():
#     print(time.sleep(3))
#
# func_a()



# @decor_time
# def say_hello(name):
#     time.sleep(2)                              # задержка выполнения функции для наглядности
#     print(f'Hello, {name}!')
#
#
# say_hello('Tom')                               # вызов функции с переданным аргументом





'''
4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
Примените эти функции в качестве методов в другом файле. 

'''

# from my_calc import *
# #
# print(addition(8, 15))
# print(subtraction(48, 26.4))
# print(multiplication(13, 4))
# print(division(35, 12))
# print(division(4, 0))
# print(remain(15, 2))


# --------------------------------------------------------------------------------------------------

# from my_calc import addition as add
#
# print(add(3, 12))
#
# ------------------------------------------------------------------------------------------------

# from my_calc import subtraction as sub
#
# print(sub(38, 115))

# -----------------------------------------------------------------------------------------------

from my_calc import addition as add, subtraction as sb, multiplication as ml, division as dv, remain as rm
#
# print(ad(8, 15))
# print(sb(48, 26.4))
# print(ml(13, 4))
# print(dv(35, 12))
# print(dv(35, 0))
# print(rm(15, 2))

# ----------- или записать так: --------------------------------

# add_res = add(100, 20)
# print(add_res)
#
# sb_res = sb(45, 9)
# print(sb_res)
#
# ml_res = ml(5, 37)
# print(ml_res)
#
# dv_res = dv(585, 15)
# print(dv_res)
#
# dv_res1 = dv(49, 0)
# print(dv_res1)
#
# rm_res = rm(541, 6)
# print(rm_res)


# ================================================================================================================



#4.5.
# import time
#
# def count_execution_time(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         end = time.perf_counter()
#         exec_time = end - start
#         print(f'{func.__name__} execution time is: {exec_time}')
#         return result
#     return wrapper
#
# @count_execution_time
# def greeting(name):
#     return f'Hello {name}!'




