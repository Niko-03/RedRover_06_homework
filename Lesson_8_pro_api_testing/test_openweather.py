import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC     # импорт Expected conditions (явные ожидания)

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


def test_open_page(driver):                                        # создали тест для запуска проверяемой страницы сайта
    driver.get('https://openweathermap.org/')                      # метод driver.get() открывает страницу сайта
    # driver.implicitly_wait(20)                                   # не явное ожидание, более грамотная замена методу time.sleep
    # driver.maximize_window()                                     # метод .maximize_window() открывает страницу в полном размере - задано в фикстуре
    assert 'openweathermap' in driver.current_url                  # проверяем, что подстрока 'openweathermap' присутствует в url
    # print(driver.current_url)                                    # распечатаем, посмотрим, что дает нам метод driver.current_url


def test_check_page_title(driver):                                            # создали тест для проверки заголовка текущей страницы
    # driver.get('https://openweathermap.org/')                               # фикстура распространяется на уровень функций, поэтому эта строчка есть в каждой функции
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'    # проверяем заголовок текущей страницы (title) через строгое сравнение


def test_fill_search_city_field(driver):                                                           # создали тест для поиска элемента по определённому локатору
    # driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")   # создали переменную, в которую запишется элемент, найденый по локатору
    search_city_field.send_keys('New York')                                                        # метод .send_keys заполнит найденный элемент указанным текстом
    time.sleep(5)                                                                                  # применили задержку по времени для заполнения формы (у меня ещё и сайт долго грузится...)

    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")          # нашли кнопку
    search_button.click()                                                                              # кликнули по кнопке
    driver.implicitly_wait(20)                                                                         # задержка 20 сек
    # # time.sleep(10)

    # driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']").click()      # так можно записать в одну строку, без переменной

    # search_option = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")       # выбрали строку в выпадающем меню
    search_option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")))                                      # вариант с ожиданием
    search_option.click()                                                                                                     # кликнули по кнопке

    # driver.implicitly_wait(30)                                          # с такой задержкой почему-то не проходит тест на сравнение заголовка h2
    time.sleep(5)                                                         # с такой задержкой проходит тест на сравнение заголовка h2

    expected_city = 'New York City, US'                                                          # в переменной ожидаемый текст в заголовке h2
    # displayed_city = driver.find_element(By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")       # присвоили переменной текст заголовка h2 после выбора города
    displayed_city = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")))                                       # вариант с ожиданием

    displayed_city_text = displayed_city.text                                                    # переменной displayed_city_text присвоили значение (текст), которое появится как h2
    # print(displayed_city_text)
    assert displayed_city_text == expected_city                                                  # сравнили проверяемый заголовок с тем, что должно быть (переменная expected_city)
    # driver.close()                                                                             #  задано в фикстуре

