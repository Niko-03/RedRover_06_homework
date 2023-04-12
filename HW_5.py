'''
5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
    нужно использовать методы get и set

5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий


'''


class Person:                                                                      # class - ключевое слово (создание шаблона)
    department = 'IT'                                                              # статический атрибут класса Person, относится ко всем объектам класса

    def __init__(self, first_name, last_name, specialist, salary):            # метод __init__ создаёт динамические атрибуты (в скобках)
        self.first_name = first_name                                              # self (свойство) - ссылка на только что созданный объект
        self.last_name = last_name
        self.specialist = specialist
        self.__salary = salary

    def study(self):                                                               # создали метод study
        return 'I study at RedRover school!'

    def get_first_name(self):                                                     # метод (get) - возвращает имя
        return f'Hello! My name is {self.first_name}.'                            # так получим имя с фразой

    def set_last_name(self, new_last_name):                                       # метод (set) изменяет значение атрибута
        self.last_name = new_last_name

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def set_change(self, new_spec, new_salary):                                  # метод для изменения значений сразу у двух атрибутов
        self.specialist = new_spec
        self.__salary = new_salary


Person1 = Person('Eva', 'Petrova', 'Developer', 2000)                         # создали объект класса Dog с указанием его атрибутов (аргументов)
print(Person1.first_name)                                                   # имя объекта
print(Person1.last_name)                                                    # фамилия объекта
print(Person1.get_first_name())                                             # метод get_first_name выдаст имя с фразой
print(Person1.first_name, Person1.last_name)                                # имя и фамилия

print(Person1.study())                                                        # вызов метода study

Person1.set_last_name('Ivanova')                                            #  через set изменили значение атрибута last_name
print(Person1.last_name)                                                    # вызвали last_name после изменений
#
# print(Person1._Person__salary)                                               # доступ к значению атрибута Private
# Person1.set_salary(2300)                                                     # изменили значение атрибута __salary
# print(Person1._Person__salary)                                               # вызвали __salary после изменений
#
# Person1.set_change('QA Engineer', 2400)                                               # изменили значения двух атрибутов
# print(Person1.__dict__)                                                      # всё про Person1
#
#
# class Junior(Person):                                                          # класс-наследник, в скобках класс-родитель
#     def __init__(self, first_name, last_name, specialist, salary, age):        # конструктор с атрибутами
#         super().__init__(first_name, last_name, specialist, salary)             # метод super() - ссылка на атрибуты родительского класса
#         self.__age = age                                                        # новый атрибут только для класса Junior
#
#
# Person2 = Junior('Николай', 'Семенов', 'QA engineer', 1000, 20)
# print(Person2.__dict__)
#
#
# class Junior_plus(Junior):                                                                 # класс-наследник, в скобках класс-родитель
#     def __init__(self, first_name, last_name, specialist, salary, age, experience):        # конструктор с атрибутами
#         super().__init__(first_name, last_name, specialist, salary, age)                   # метод super() - ссылка на атрибуты родительского класса
#         self.experience = experience
#
#
# Person3 = Junior_plus('Наталья', 'Ветрова', 'developer', 1500, 25, 1)
# print(Person3.__dict__)
#
#
# class Middle(Person):
#     def __init__(self, first_name, last_name, specialist, salary, age, experience):
#         super().__init__(first_name, last_name, specialist, salary)
#         self.__age = age
#         self.experience = experience
#
#
# Person4 = Middle('Сергей', 'Петров', 'developer', 2300, 28, 3.5)
# print(Person4.__dict__)
#
# Person5 = Middle('Ирина', 'Крылова', 'QA engineer', 2200, 27, 3)
# print(Person5.__dict__)
#
#
# class Senior(Person):
#     def __init__(self, first_name, last_name, specialist, salary, age, experience):
#         super().__init__(first_name, last_name, specialist, salary)
#         self.__age = age
#         self.experience = experience
#
#
# Person6 = Senior('Егор', 'Васильев', 'developer', 4000, 35, 8)
# print(Person6.__dict__)
#
# Person7 = Senior('Макс', 'Иванов', 'analyst', 4000, 32, 6.5)
# print(Person7.__dict__)
#









