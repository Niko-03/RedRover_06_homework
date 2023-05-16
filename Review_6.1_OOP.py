# создадим класс Car, и атрибуты класса name, make, age  ==============================================

# class Car:                               # название класса всегда с большой буквы
#     name = '07'                          # атрибуты класса: имя
#     make = 'audi'                        # марка
#     age = 2020                           # год выпуска


# методы класса  ========================================================================================

# ОТЛИЧИЯ метода от функции:
# МЕТОД привязан к конкретному объекту класса
# Например, нельзя просто так вызвать функцию start() потому, что она находится внутри зоны видимости класса Car
# ФУНКЦИЯ не привязана к объекту, её можно вызвать в любом месте кода


    # @staticmethod                        # если метод пишем без (self), то через @staticmethod (дополнительно почитать!!!)

    # def start(self):                        # создали метод start
    #     print('Заводим двигатель')
    #
    # def stop(self):                         # создали метод stop
    #     print('Отключаем двигатель')


# экземпляр класса:  =================================================================================

# car1 = Car()                              # создали экземпляр класса Car - машину car1, у которой есть все атрибуты класса Car
# car2 = Car()
# print(type(car1))                         # получим тип экземпляра класса

# print(car1.age)                             # можно обратиться как к атрибуту экземпляра
# print(car1.make)
# print(car1.name)
# car1.start()                                # так и к методу класса


# доступ к атрибутам класса:  ==========================================================================

# print(Car.name)                                      # через обращение к атрибуту класса
# print(Car.x)                                       # обращение к несуществующему атрибуту вернёт ошибку
#
# print(Car.__dict__)                                  # посмотреть все атрибуты класса - метод __dict__ вернёт атрибуты в виде словаря

# print(getattr(Car, 'name'))                            # обращение к атрибуту через встроенную функцию getattr()
# print(getattr(Car, 'x'))                               # обращение к несуществующему атрибуту вернёт ошибку
# print(getattr(Car, 'age', 'Нет такого атрибута'))        # такая запись вернёт артибут, если он существует,
# print(getattr(Car, 'x', 'Нет такого атрибута'))          # или вернёт фразу (третий параметр функции getattr), если атрибута нет - помогает избежать ошибки


# изменение значения атрибута:  ====================================================================================

# Car.make = 'mercedes'
# print(Car.make)
#
# Car.x = 100                     # при обращении к несуществующему атрибуту ошибки не будет, но появится новый атрибут с присвоенным значением
# print(Car.x)
#
# setattr(Car, 'y', 1000)         # создание нового атрибута через встроенную функцию setattr
# print(Car.y)

# print(Car.__dict__)             # проверили наличие новых атрибутов - видим новое значение name, и новые атрибуты x и y


# удаление атрибута:  ==============================================================================================

# del Car.x
# print(getattr(Car, 'x', 'Нет такого атрибута'))
#
# delattr(Car, 'y')                                   # удаление атрибута через встроенную функцию delattr()
# print(getattr(Car, 'y', 'Нет такого атрибута'))


# ===============================================

# class Car1:                                # у класса Car1 видим три атрибута и два метода
#     age = 2020
#     name = 'Priora'
#     make = 'Lada'
#
#     def start(self, name, make='Audio'):             # внутри метода start передали два параметра, причём name - обязательный, make сделали по умолчанию
#         self.name = name
#         self.make = make
#         print(f'У машины {self.make} {self.name} заведём двигатель')
#
#     def get_age(self):                                                         # создали метод get_age
#         print(f'Машина {self.make} {self.name} {self.age} года выпуска')
#
#
# car3 = Car1()                             # экземпляр класса Car1
# print(car3.make)                          # ??? почему Lada...
# print(car3.start('Q7'))                   # вызвали метод start с указанием аргумента name
# print(car3.get_age())                     # вызвали метод get_age


# Конструктор - это специальный метод, который вызывается по умолчанию, когда мы создаём объект класса. ===================

''' Справочно:

Конструктор класса Python — это первая часть кода, которая выполняется при создании нового объекта.
Прежде всего, конструктор можно использовать для помещения значений в переменные-члены.
Также в конструкторе можно выводить сообщения, которые подтвердят, что объект был создан.
Роль конструктора вы сможете оценить по достоинству, когда изучите наследование Python.

Для чего нужен конструктор в Python?
- Конструктор — уникальный метод класса, который называется __init__.
- Первый параметр конструктора во всех случаях self (ключевое слово, которое ссылается на сам класс).
- Конструктор нужен для создания объекта.
- Конструктор передает значения аргументов свойствам создаваемого объекта.
- В одном классе всегда только один конструктор.
- Если класс определяется не конструктором, Python предположит, что он наследует конструктор родительского класса.

'''

# class Cat:
#     name = 'Timmy'
#
#     def __init__(self):              # конструктор вызывается методом __init__ - здесь пока не принимает никаких параметров
#         print('Hello!')              # через метод __init__ сокращается запись кода - параметры класса передаются в __init__
#
#
# print(Cat())                        # вызвали класс Cat - при каждом вызове класса будет вызываться конструктор --> def __init__(self)
# print(Cat())
# print(Cat())


# Задача  ======================================================================================

# class HockeyPlayer:                                                 # создали класс хоккеистов
#     def __init__(self, first_name, last_name, goal=0, assist=0):    # параметры класса (через __init__)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.goal = goal
#         self.assist = assist
#
#     def goals(self, goal=0):                                           # метод принимает количество голов, забитых игроком (по умолчанию равен 0)
#         self.goal = goal                                               # это тот же goal, что и в __init__
#
#     def all_assist(self, assist=0):                                    # метод принимает assist игрока (по умолчанию равен 0)
#         self.assist = assist
#
#     def statistics(self):                                                 # метод описывает статистику
#         print(f'HockeyPlayer: {self.first_name} {self.last_name}')
#         print(f'Goals: {self.goal}')
#         print(f'Assist: {self.assist}')
#
#
# ovechkin = HockeyPlayer('Alexandr', 'Ovechkin')                      # создали экземпляр класса
# ovechkin.goals(700)                                                  # вызвали метод goals
# ovechkin.all_assist(500)                                             # вызвали метод all_assist
# ovechkin.statistics()                                                # вызвали метод statisnics
#
# lekavele = HockeyPlayer('Vinsent', 'Lekavele')                      # создали экземпляр класса
# lekavele.goals(500)                                                  # вызвали метод goals
# lekavele.all_assist(600)                                             # вызвали метод all_assist
# lekavele.statistics()





# изменить имя класса  (???)======================================================




# методы наследования  ========================================================


# class Person:                                # Parent (родительский класс)
#     def can_breathe(self):
#         print('Я дышу')
#
#     def can_walk(self):
#         print('Я хожу')

    # def can_sleep(self):
    #     print('Я сплю')


# class Teacher(Person):                       # Subclass (дочерний класс- Teacher - учитель)
#     def can_teach(self):
#         print('Я учу')
    #
    # def can_breathe(self):
    #     print('Я дышу')
    #
    # def can_walk(self):
    #     print('Я хожу')
    #
    # def can_sleep(self):
    #     print('Я сплю')

# t1 = Teacher()                        # экземпляр дочернего класса
# t1.can_breathe()                      # может брать методы и атрибуты родительского класса
# t1.can_sleep()                        # и свои методы и атрибуты
#
# p1 = Person()                         # экземпляр родительского класса
# p1.can_breathe()                      # экземпляр родительского класса может использовать только свои методы и атрибуты
# p1.sleep()                            # и не может использовать методы (и атрибуты) дочернего класса




# Проверка: является ли класс Teacher подклассом Person  ===============================================================

# print(issubclass(Teacher, Person))                       # Teacher является подклассом Person - вернёт True (или False)
#
# print(issubclass(Person, Teacher))                       # Person не является подклассом Teacher



# НО если не указывается от кого наследуется класс, то по умолчанию он наследуется от object: ==================================
# object - самый главный, корневой, класс

# class Person1(object):                                # Parent
#     def can_breathe(self):
#         print('Я дышу')
#
#
# class Teacher1(Person1):                              # Subclass
#     def can_teach(self):
#         print('Я учу')
#
#
# print(issubclass(Teacher1, Person1))
# print(issubclass(Person1, object))
# print(issubclass(Teacher1, object))





# переопределение - если каких-то методов нет у наследника, он берёт их у родителя   ======================================
# если у родителя и наследника есть одинаковые методы, то наследник перезаписывает (меняет) родительский метод на свой
# то же самое происходит и с атрибутами

# расширение - это когда у наследника есть метод(или атрибут), которого нет у родителя

class Person2:                                # Parent
    def can_breathe(self):
        print('Я дышу')

    def can_walk(self):
        print('Я хожу')

    def can_sleep(self):
        print('Я сплю')


class Teacher2(Person2):                       # Subclass
    def can_teach(self):                       # расширение - это когда у наследника есть метод(или атрибут), которого нет у родителя
        print('Учитель учит')

    def can_breathe(self):
        print('Учитель дышит')

    def can_sleep(self):
        print('Я сплю')


t2 = Teacher2()
t2.can_teach()
t2.can_breathe()
t2.can_walk()
t2.can_sleep()



# Делегирование - это ... =========================================

















