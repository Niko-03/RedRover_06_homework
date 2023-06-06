# смотри файлы:
# проект Lesson_7_pro_selenium --> test_lesson_7_openweather.py
# проект QA_auto_Python_HW --> Lesson_7_Selenium.py
# проект QA_auto_Python_HW --> Lesson_pro_tests.py

''' Для каждого проекта устанавливаем - через Terminal (!!! В начале названия файла и функции должно стоять слово test):

- pip install selenium
- pip install pytest
- pip install webdriver-manager    (для работы драйверов нашего браузера, и всегда поддтягивает последнюю версию браузера)


========== импорты (прописываем в файле) ====================

from selenium import webdriver                                # импортируем вебдрайвер
import pytest
from webdriver_manager.chrome import ChromeDriverManager      # ChromeDriverManager - это класс
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By                    # класс By


======== и ещё импорты ==================
import time
from selenium.webdriver.support.wait import WebDriverWait           # явное ожидание
from selenium.webdriver.support import expected_conditions as EC    # модуль expected_conditions уже содержит набор предопределенных условий для работы с WebDriverWait



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  --> создали экземпляр браузера (или драйвера)
                                                                                 и обозначили, что наш браузер --> Chrome
                                                                                 все свойства и методы наш экземпляр будет брать
                                                                                 из класса ChromeDriverManager


browser.   -->  увидим все методы для браузера, например:
browser.get('url') -->  откроет веб-страницу


============== примерное взаимодействие с элементами веб-страницы ===========================

browser.get('http://suninjuly.github.io/cats.html')       --> открыли страницу сайта
browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")    --> find_element() - выбрали элемент на веб-странице
browser.find_element(By.CSS_SELECTOR, 'здесь селектор')    --> или так выбрали элемент

bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")     --> переменной присвоили наш элемент
print(bullet_cat)        -->  распечатаем наш элемент - в консоли увидим наш объект

print(bullet_cat.text)        --> через свойство text увидим текст этого элемента



view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")    --> browser.find_elements - выбрали все элементы на странице с текстом View
print(view_buttons)     --> получим лист с элементами
assert len(view_buttons) == 6, 'wron length'     -->  проверка на то, что наших элементов на странице 6 штук
                                                      'wron length' - неверная длина - получим в случае ошибки



================= создадим функцию ====================================

def open_page():
    browser.get('http://suninjuly.github.io/cats.html')

    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    print(bullet_cat.text)

    view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_buttons)
    assert len(view_buttons) == 6, 'wron length'


================= создадим тестовый метод ====================================

def test_open_page():
    open_page()            --> вызвали нашу функцию


===================== или так ========================================

def test_open_page():
    browser.get('http://suninjuly.github.io/cats.html')

    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    print(bullet_cat.text)

    view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_buttons)
    assert len(view_buttons) == 6, 'wron length'


'''

'''
---------------------- PAGE OBJECT MODEL (POM) -----------------------------------------------------------------------


-- на лекции -----------------

- main_page - страница сайта представлена как класс
                 - у этой страницы (класса) есть метод - искать погоду в определённом городе
                 - любое действие, произведённое на странице (клик по кнопке меню, заполнение строки поиска и т.д.) - это метод класса
                 - любой элемент на странице, виджет, карта... - это свойство

- base_page - базовая страница - здесь прописываются одинаковые элементы для каждой страницы (header, footer например)

'''

