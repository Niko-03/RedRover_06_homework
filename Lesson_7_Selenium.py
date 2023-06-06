# смотри файлы:
# проект Lesson_7_pro_selenium --> test_lesson_7_openweather.py
# проект QA_auto_Python_HW --> Lesson_7_Selenium.py
# проект QA_auto_Python_HW --> Lesson_pro_tests.py

'''     SELENIUM WEBDRIVER

- это программная библиотека для управления браузерами (короткое название webdriver);

- используется для UI-тестирования (для тестирования сайта с точки зрения пользователя).
- Селениум "заходит" на страницу, кликает по кнопкам, отмечает наличие каких-то элементов, вводит какие-то данные...
- чтобы Селениум мог взаимодействовать с элементами, ему надо показать, где искать тот или иной элемент - используются селекторы.

- для начала работы с selenium webdriver необходимо определить три ключевых элемента:
                    - браузер,
                    - драйвер браузера,
                    - скрипт для драйвера браузера.


WebDriver– это драйвер браузера, то есть не имеющая пользовательского интерфейса программная библиотека,
которая позволяет различным другим программам взаимодействовать с браузером, управлять его поведением,
получать от браузера какие-то данные и заставлять браузер выполнять какие-то команды.
Исходя из этого определения, ясно, что WebDriver не имеет прямого отношения к тестированию.
Он всего лишь предоставляет автотестам доступ к браузеру.

Драйвер браузера:
Драйвер — это веб-сервис, который отправляет команды браузеру. У каждого браузера свои команды управления,
которые реализованы по-разному, поэтому и драйверы нужны разные.

Скрипт с набором команд для драйвера браузера:
В этом скрипте прописан алгоритм действий для браузера, с помощью него WebDriver эмулирует поведение пользователя.


----------- Основные методы Selenium Webdriver ------------------------------------

- driver.current_url        ------------>  получить url-адрес текущей страницы в формате string
- driver.current_window_handle  -------->  получить дескриптор текущего окна (по индексу переключаемся на одно или другое окно (что это???))
- driver.name                ----------->  получить имя браузера внизу экземпляра
- driver.orientation         ----------->  получить местоположение текущего устройства
- driver.page_source         ----------->  получить исходный код текущей страницы
- driver.title               ----------->  получить заголовок текущей страницы
- driver.refresh()           ----------->  обновить текущую страницу
- driver.switch_to_alert()   ----------->  переключить фокус на предупреждение, которое появляется на текущей странице
- driver.switch_to_active_element()  --->  вернуть элемент с единственным фокусом текущей страницы
- driver.find.element()    ------------->  найти элемент по определенному локатору
- driver.maximize_window()  ------------>  открывает страницу сайта в полном размере
- driver.minimize_window()  ------------>
- element.send_keys()      ------------->  заполнить заданный элемент
- element.click()          ------------->  выполнить клик по указанному элементу
- driver.close()           ------------->  закрыть текущее окно браузера
- driver.quit()            ------------->  закрыть все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии


(browser.close() закрывает текущее окно браузера. Это значит, что если ваш скрипт вызвал всплывающее окно,
 или открыл что-то в новом окне или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть.
 В свою очередь browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии.)



---------------------- про ASSERT -----------------------------------------------------------------------

Инструкции assert в Python — это булевы выражения, которые проверяют, является ли условие истинным (True).
Они определяют факты (утверждения) в программе.
Assertion — это проверка, которую можно включить, а затем выключить, завершив тестирование программы.

(Ключевое слово assert сравнивает два значения и возвращает True, если они равны, и False — если нет.)



---------------------- ОЖИДАНИЯ в Selenium (два вида) -----------------------------------------------------------------------
(посмотреть на сайте   selenium.dev/documentation/webdriver/waits/)
(статья на Хабре https://habr.com/ru/articles/273089/)


- не всегда test успевает кликнуть по элементу, бывает так, что необходимо доп.время для загрузки,
- или элемент появляется (или пропадает) на странице после определённых действий.
- Для этого используют ОЖИДАНИЯ.

Selenium WebDriver предоставляет два типа ожиданий — неявное (implicit) и явное (explicit).
ЯВНОЕ ожидание заставляет WebDriver ожидать возникновение определенного условия до произведения действий.
НЕЯВНОЕ ожидание заставляет WebDriver опрашивать DOM определенное количество времени, когда пытается найти элемент.


----------- ЯВНОЕ ожидание - Explicit wait - конкретно говорим драйверу какого события ждать ----------------------------------

- Explicit wait - импортируется    <from selenium.webdriver.support.wait import WebDriverWait>
- импорт ожидаемых условий      <from selenium.webdriver.support import expected_conditions as EC>
Например, WebDriverWait в комбинации с ExpectedCondition помогут написать код, ожидающий ровно столько, сколько необходимо.

=========================== пример кода ================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
==================== конец примера ========================================

Этот код будет ждать 10 секунд до того, как отдаст исключение TimeoutException или если найдет элемент за эти 10 секунд, то вернет его.
WebDriverWait по умолчанию вызывает ExpectedCondition каждые 500 миллисекунд до тех пор, пока не получит успешный return.
Успешный return для ExpectedCondition имеет тип Boolean и возвращает значение true,
либо возвращает not null для всех других ExpectedCondition типов.


------------ Ожидаемые условия (Expected conditions) - конкретные условия для явных ожиданий ---------------------------------

- импорт ожидаемых условий      <from selenium.webdriver.support import expected_conditions as EC>

Существуют некие условия, которые часто встречаются при автоматизации веб-сайтов. Ниже перечислены реализации каждого.
Связки в Selenium Python предоставляют некоторые удобные методы, так что вам не придется писать класс expected_condition самостоятельно
или же создавать собственный пакет утилит.

- alert is present    -->  оповещение присутствует
- element exists      -->  элемент существует
- element is visible  -->  элемент виден
- title contains      -->  заголовок содержит
- title is            -->  название
- element staleness   -->  элемент устарелости
- visible text        -->  видимый текст

--- переведено через ЯндексПереводчик -----------

- presence_of_element_located                           -->  наличие расположенного элемента
- visibility_of_element_located                         -->  видимость расположенного элемента
- visibility_of                                         -->  видимость
- presence_of_all_elements_located                      -->  наличие всех элементов, расположенных
- text_to_be_present_in_element                         -->  текст, который должен присутствовать в элементе
- text_to_be_present_in_element_value                   -->  текст, который должен присутствовать в значении элемента
- frame_to_be_available_and_switch_to_it                -->  рамка должна быть доступна и переключите на неерамка должна быть доступна и переключите на нее
- invisibility_of_element_located                       -->  невидимость расположенного элемента
- element_to_be_clickable — it is Displayed and Enabled  -->  элемент должен быть кликабельным — он отображается и включен
- staleness_of                                          -->  несвежесть
- element_to_be_selected                                -->  элемент, подлежащий выбору
- element_located_to_be_selected                        -->  элемент, расположенный для выбора
- element_selection_state_to_be                         -->  состояние выбора элемента должно быть
- element_located_selection_state_to_be                 -->  элемент, расположенный в состоянии выбора, который должен быть


Модуль expected_conditions уже содержит набор предопределенных условий для работы с WebDriverWait.

======= пример ==================================================================
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
========================================================================


--------------- НЕЯВНОЕ ожидание - Implicit wait ----------------------------------

driver.implicitly_wait(10)                  #  ждём 10 сек  -->  применяем, когда не знаем, какой вид явного ожидания применить
                                            # это более грамотная замена методу time.sleep()


Неявное ожидание — это указание WebDriver опрашивать DOM в течение определенного времени при попытке найти элемент или элементы,
если они не доступны немедленно. Значение по умолчанию — 0, что означает отключено.
После установки неявное ожидание устанавливается на время жизни сеанса.

Неявное ожидание появления элементов отключено по умолчанию, и его нужно будет включать вручную для каждого сеанса.
Смешивание явных и неявных ожиданий приведет к непредвиденным последствиям,
а именно к ожиданию ожидания в течение максимального времени, даже если элемент доступен или условие истинно.

Предупреждение: не смешивайте неявные и явные ожидания. Это может привести к непредсказуемому времени ожидания.
Например, установка неявного ожидания в 10 секунд и явного ожидания в 15 секунд может привести к тайм-ауту через 20 секунд.


=========================== пример кода ================================================

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)                                   # жди 10 секунд (например)  - более грамотная замена методу time.sleep
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

=========================== ещё пример ================================================

driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")

=========================== конец примера ================================================

---------- про FluentWait -----------------------------------------------------------

FluentWait принимает ещё один параметр - количество проверок


Экземпляр FluentWait определяет максимальное время ожидания условия, а также частоту проверки условия.

Пользователи могут настроить ожидание, чтобы игнорировать определенные типы исключений во время ожидания,
например, NoSuchElementExceptionпри поиске элемента на странице.


- FluentWait - кроме прочего принимает параметр <сколько раз проверить>   --> poll_frequency=1 (например)
             - или игнорирование каких-то ошибок                          -->   ignored_exceptions=[]


=========================== пример кода ================================================

driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))

=========================== конец примера ================================================





------------------------------ PYTEST ---------------------------------------------------------------------------------

- это среда тестирования, основанная на Python, её используют для написания и выполнения тестового кода;
- выполнение определённого набора тестов с помощью фильтрации;
- параметризация тестов - запуск одного и того же теста с разными наборами параметров;
- полная обратная совместимость с UNITTEST - возможность запуска тестов, написанных на нём;
- выполнение нескольких тестов параллельно;
- отчёт с результатами выполнения тестов, цветной отчёт в консоли выглядит удобнее - красные FAILED видны сразу;
- удобный ASSERT (стандартный из Python), не надо запоминать разные ASSERT`ы, как например в UNITTEST.



----------------------- про UNITTEST - встроенный в PYTEST тестовый фреймворк (справочно) -----------------------------------------------------------------------

Unittest - инструмент для тестирования в Python. Это стандартный модуль для написания юнит-тестов на Python.
Unittest это порт JUnit с Java. Иными словами, и в коде модуля, и при написании тестов легко прослеживается ООП стиль,
что весьма удобно для тестирования процедур и классов.

Модуль unittest предоставляет базовый класс TestCase, который можно использовать для создания новых тестовых случаев.

Набор тестов (test suite) - несколько тестовых случаев, наборов тестов или и того и другого.
Он используется для объединения тестов, которые должны быть выполнены вместе.

Исполнитель тестов (test runner) - компонент, который управляет выполнением тестов и предоставляет пользователю результат.
Исполнитель может использовать графический или текстовый интерфейс или возвращать специальное значение,
которое сообщает о результатах выполнения тестов.

Модуль unittest предоставляет богатый набор инструментов для написания и запуска тестов.




-------------------------------- ФИКСТУРЫ (FIXTURES) - широко применяются в Pytest -------------------------------------

- фикстуры в контексте pytest - это вспомогательные функции для тестов, они не являются частью тестового сценария;
- в pytest фикстуры можно задавать глобально, передавать их в тестовые методы, как параметры;
- pytest также имеет набор встроенных фикстур;
- фикстуры обеспечивают надёжность тестов, согласованность и повторяемость их результатов.
  При инициализации можно настраивать сервисы, состояния, переменные окружения;
- для фикстур можно задавать область покрытия (SCOPE). Например, "FUNCTION", "CLASS", "MODULE", "SESSION".
  Соответственно, фикстура будет вызываться один раз либо для тестового метода, либо для класса, модуля или сессии.

- фикстура задаётся файлом conftest.py в корне проекта.


------------------- ПРИМЕР ФИКСТУРЫ -----------------------------------------------
- сначала прописываем все импорты


@pytest.fixture(scope='function')                   # задаём декоратор, чтобы pytest распознавал функцию def driver(), как фикстуру
                                                    # в () определяем, на какой уровень распространяется фикстура

def driver():                                       # фикстура (как функция def driver() )
    print('start browser')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # создали экземпляр выбранного драйвера (браузера) и установили драйвер в фикстуру
    driver.maximize_window()                        # полноэкранный режим отображения веб-страницы
    yield driver                                    # yield почти то же самое, что и retern (???)
    driver.quit()                                   # закрыть все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии


- затем в основном файле (test.py) в наши функции добавляем в качестве параметра driver (название функции из фикстуры)

- если фикстура распространяется на уровень функций, то метод driver.get (открытие страницы сайта)
  прописываем в каждой функции нашего файла (test.py)    < @pytest.fixture(scope='function') >

- если фикстура распространяется на уровень сессии  < @pytest.fixture(scope='session') >
  то запуск веб-страницы будет только один раз, и тесты, прописанные в файле test.py, отработают с одним открытием окна.

- если в scope ничего не указано < @pytest.fixture() >, то по умолчанию < @pytest.fixture(scope='function') >





---------------------- PAGE OBJECT MODEL (POM) ---------------------------------------------------------------------------------

- POM - это паттерн программирования, широко применяемый в атоматизации тестирования.
  Его основная идея состоит в том, что любую страницу веб-приложения можно представить в виде объекта класса.
  С этой точки зрения:
             - способы взаимодействия со страницей - это методы класса,
             - элементы веб-страницы - атрибуты класса.

- POM позволяет отделить код, относящийся к тестам, от кода, описывающего страницу (локаторы)
  и способы взаимодействия с ней (открыть страницу, авторизоваться, положить товар в корзину и т.д.).
  Поэтому, при изменении вёрстки страницы, нет необходимости переписывать тесты,
  надо лишь внести изменения в класс, который описывает эту страницу.

-- на лекции -----------------

- main_page - страница сайта представлена как класс
- у этой страницы (класса) есть метод - искать погоду в определённом городе
- любое действие, произведённое на странице (клик по кнопке меню, заполнение строки поиска и т.д.) - это метод класса
- любой элемент на странице, виджет, карта... - это свойство

- base_page - базовая страница - здесь прописываются одинаковые элементы для каждой страницы (header, footer например)
'''

