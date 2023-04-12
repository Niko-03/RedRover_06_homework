''' ----- ДОМАШНЕЕ ЗАДАНИЕ ---------------------------------------------------------------------

3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

'''
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])                    # как список
# print(*my_list[2])                    # как отдельные элементы


# -------------- варианты на разборе домашки ---------------------

#Option 1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])

# Option 2. Using deconstruction
# my_list = ['a', 'b', [1, 2, 3], 'd']
# list1 = my_list[2]
# print(*list1, sep='\n')



'''
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
'''
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

# ----------- сумма всех чисел ------------------
# list_num = [item for item in list_1 if isinstance(item, int)]             # один способ
# list_num = [item for item in list_1 if type(item) is int]               # другой способ
# list_num = list(filter(lambda i: isinstance(i, int), list_1))                     # и ещё способ, через lambda

# print(list_num)
# print(sum(list_num))

# ---------- строки с буквой а -----------------
# list_str = [item for item in list_1 if isinstance(item, str)]    # отсортировали строки из list_1
# print(list_str)

# list_str1 = [i for i in list_str if 'a' in i]                  # первый способ
# print(list_str1)

# ------- или так ----------
# for i in list_str:                                               # второй способ записи
#     if 'a' in i:
#         print(i)


# -------------- варианты на разборе домашки ---------------------

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #a) Using filter get sum of all integers
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# #b) Using list comprehension print string which contain 'a'
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])




'''
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

'''
# my_lst = ['cat', 'dog', 'horse', 'cow']
# my_tup = tuple(my_lst)
#
# print(my_lst)
# print(type(my_lst))
#
# print(my_tup)
# print(type(my_tup))


# -------------- вариант на разборе домашки ---------------------

# print(tuple(['cat', 'dog', 'horse', 'cow']))



'''
3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal') - 'Равный'
     
'''

# fam_1 = tuple(input('Перечислите членов семьи_1 через запятую: ').split(','))
# fam_2 = tuple(input('Перечислите членов семьи_2 через запятую: ').split(','))
#
# if len(fam_1) == len(fam_2):
#     print('Equal')
# elif len(fam_1) > len(fam_2):
#     print('family_1')
# else:
#     print('family_2')



'''
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

# '''
# film = {
#     'title': 'The Matrix',
#     'director': 'братья Вачовски',
#     'years': 1999,
#     'budget': 63000000,
#     'main_actor': 'Киану Ривз',
#     'slogan': 'Добро пожаловать в реальный мир',
# }
# print(film)
# print(film.keys())       # ключи
# print(film.values())     # значения
# print(film.items())      # пара ключ-значение




'''
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
'''
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(my_dictionary.values())
# print(sum(my_dictionary.values()))


# -------------- варианты на разборе домашки ---------------------

# Option 1
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# result = 0
# for x in my_dictionary:
#     result += my_dictionary[x]
# print(result)


# Option 2
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))



'''
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 
'''
# my_lst = [1, 2, 3, 4, 5, 3, 2, 1]
# print(my_lst)
#
# my_set = set(my_lst)                   # множество удаляет повторяющиеся элементы
# print(my_set)
#
# my_lst2 = list(my_set)
# print(my_lst2)                         # множество превратили в список



# -------------- варианты на разборе домашки ---------------------

# new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(new_list)



'''
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
'''

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(set1)
# print(set2)

# print(set1.intersection(set2))             # пересечение множеств - возвращает общие, одинаковые, элементы

# print(set1.difference(set2))               # разность множеств - возвращает множество с элементами, которых нет в других переданных множествах
# print(set2.difference(set1))
#
# print(set1.symmetric_difference(set2))     # симметричная разность - возвращает множество с элементами, которые есть либо в самом множестве,
#                                            #  либо во втором переданном множестве
# print(set2.symmetric_difference(set1))

# print(set1.issubset(set2))                 # является ли множество set1 подмножеством множества set2
# print(set2.issubset(set1))                 # является ли множество set2 подмножеством множества set1




# -------------- варианты на разборе домашки ---------------------

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))

