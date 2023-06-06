# смотри файлы:
# проект Lesson_7_pro_selenium --> test_lesson_7_openweather.py
# проект QA_auto_Python_HW --> Lesson_7_Selenium.py
# проект QA_auto_Python_HW --> Lesson_pro_tests.py

'''
- webdriver.Chrome - указываем, что из webdriver`а берём Chrome;
- service=Service(ChromeDriverManager().install()) - указываем, что устанавливаем ChromeDriver;
- webdriver_manager - находит и устанавливает последнюю версию вебдрайвера, (ChromeDriver в нашем случае),
                      т.е. не надо явно указывать версию вебдрайвера;
- ChromeDriverManager() - это уже установленный класс, и когда создаем его экземпляр, то оттуда берём все свойства и методы.


- pytest -s -v   --->   команда для запуска теста из Terminal,
                        ищет все файлы в данной дериктории со словом <test> в названии файла
                        (-s и -v  -  это флаги, используются для получения доп.информации в ходе запуска и работы теста)

'''

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By                                      # класс By.ID
import time
from selenium.webdriver.support.wait import WebDriverWait                        # явное ожидание
from selenium.webdriver.support import expected_conditions as EC                 # явное ожидание - импорт ожидаемых условий

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))       # создали экземпляр браузера (или драйвера)
                                                                                  # и обозначили, что наш браузер --> Chrome
                                                                                  # все свойства и методы наш экземпляр будет
                                                                                  # брать из класса ChromeDriverManager


def test_open_page():                                               # создали тест (метод) для запуска проверяемой страницы сайта
    driver.get('https://openweathermap.org/')                       # метод get открывает вебстраницу
    driver.maximize_window()                                        # метод .maximize_window() открывает страницу в полном размере
    assert 'openweathermap' in driver.current_url                   # проверяем, что подстрока 'openweathermap' присутствует в url (при помощи оператора in)
                                                                    # метод current_url вернёт url-адрес текущей страницы в формате string

    print(driver.current_url)                                       # распечатаем, посмотрим, что дает нам метод driver.current_url
                                                                    # результат в виде < test_open_page PASSED      [100%]https://openweathermap.org/ >


def test_check_page_title():                                                # создали тест для проверки заголовка (title) текущей страницы
    driver.get('https://openweathermap.org/')                               # фикстура распространяется на уровень функций, поэтому эта строчка есть в каждой функции
    driver.maximize_window()
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'  # проверяем заголовок текущей страницы через строгое сравнение

# ------------- тест с неявным ожиданием -------------------------------------------
# (почему-то не работает явное ожидание, через time.sleep() всё работает)


# def test_fill_search_city_field():                                           # создали тест для заполнения поля
#     driver.get('https://openweathermap.org/')
#     driver.maximize_window()
#     search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")  # создали переменную, в которую запишется элемент, найденый по локатору
#     search_city_field.send_keys('New York')                                                       # метод .send_keys заполнит найденный элемент указанным текстом
#     time.sleep(10)                                                                                 # применили задержку по времени для заполнения формы (у меня ещё и сайт долго грузится...)
#     # driver.implicitly_wait(20)
#
#    driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']").click()                        # так можно записать в одну строку, без переменной

#     search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")               # нашли кнопку
#     search_button.click()                                                                                   # кликнули по кнопке
#     driver.implicitly_wait(10)                                                                              # неявное ожидание
#
#     search_option = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")  # выбрали строку в выпадающем меню
#     search_option.click()                                                                                              # кликнули по ней
#     time.sleep(10)
#     # driver.implicitly_wait(20)
#
#     expected_city = 'New York City, US'                                                                     # в переменной - ожидаемый текст в заголовке h2
#     displayed_city = driver.find_element(By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")                    # в переменной текст заголовка h2 после выбора города
#     time.sleep(10)
#     # driver.implicitly_wait(10)
#
#     displayed_city_text = displayed_city.text                                                               # из displayed_city взяли текст, который появится как h2
#     print(displayed_city_text)                                                                              # можно распечатать
#     assert displayed_city_text == expected_city                                                             # сравнили проверяемый заголовок с тем, что должно быть (переменная expected_city)


# ------ то же самое, но с явным ожиданием (и здесь time.sleep() работает, а явное ожидание не работает почему-то...) -----------------------

def test_fill_search_city_field():                                                               # создали тест для заполнения поля
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")  # создали переменную, в которую запишется элемент, найденый по локатору
    search_city_field.send_keys('New York')                                                       # метод .send_keys заполнит найденный элемент указанным текстом

    search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[class='button-round dark']")))                                  # нашли кнопку
    search_button.click()                                                                         # кликнули по кнопке

    search_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")))          # явное ожидание <элемент должен быть кликабельным — он отображается и включен>
    search_option.click()                                                                         # кликнули по ней
    time.sleep(10)                                                                                # это ожидание сррабатывает, без него - нет

    expected_city = 'New York City, US'                                                            # ожидаемый результат
    displayed_city = WebDriverWait(driver, 30).until(EC.presence_of_element_located(               # явное ожидание <наличие расположенного элемента>
        (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")))
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city
    driver.quit()                                                                                  # тоже почему-то не работает без time.sleep()...




'''
----------- Основные методы Selenium Webdriver ------------------------------------

-> driver.get               ------------->  откроет вебстраницу
-> driver.current_url        ------------>  получить url-адрес текущей страницы в формате string
- driver.current_window_handle  -------->  получить дескриптор текущего окна (по индексу переключаемся на одно или другое окно (что это???))
- driver.name                ----------->  получить имя браузера внизу экземпляра
- driver.orientation         ----------->  получить местоположение текущего устройства
- driver.page_source         ----------->  получить исходный код текущей страницы
-> driver.title               ----------->  получить заголовок текущей страницы
- driver.refresh()           ----------->  обновить текущую страницу
- driver.switch_to_alert()   ----------->  переключить фокус на предупреждение, которое появляется на текущей странице
- driver.switch_to_active_element()  --->  вернуть элемент с единственным фокусом текущей страницы
-> driver.find.element()    ------------->  найти элемент по определенному локатору
-> driver.maximize_window()  ------------>  открывает страницу сайта в полном размере
-> driver.minimize_window()  ------------>
-> element.send_keys('text')  ------------->  заполнить заданный элемент указанным текстом
-> element.click()          ------------->  выполнить клик по указанному элементу
- driver.close()           ------------->  закрыть текущее окно браузера
- driver.quit()            ------------->  закрыть все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии


(browser.close() закрывает текущее окно браузера. Это значит, что если ваш скрипт вызвал всплывающее окно,
 или открыл что-то в новом окне или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть.
 
 В свою очередь browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.)
 
 
 ------------ driver.quit() ------------------
Выход будет:
    - Закройте все окна и вкладки, связанные с этим сеансом WebDriver
    - Закройте процесс браузера
    - Закройте процесс фонового драйвера
    - Сообщите Selenium Grid, что браузер больше не используется, чтобы его можно было использовать в другом сеансе 
      (если вы используете Selenium Grid).
      
Если не вызвать quit, на вашем компьютере останутся запущенными дополнительные фоновые процессы и порты, 
которые впоследствии могут вызвать проблемы.

 '''