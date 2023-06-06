# выносим в фикстуру установку нашего драйвера (инициализируем драйвер) в виде функции < def driver() >

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# задаём декоратор, чтобы pytest распознавал функцию def driver(), как фикстуру - в (scoupe='...') определяем,
# на какой уровень распространяется фикстура

# чтобы использовать эту фикстуру в наших тестовых методах, мы должны передать её, как параметр

# если скобки в фикстуре пустые < @pytest.fixture() >,то по умолчанию параметр - функция - (scoupe='function')

# тесты должны быть независимыми (одна проверка - один тест), поэтому  -->  @pytest.fixture(scoupe='function')

# через декоратор pytest знает, что данную фикстуру мы применяем в файле с тестами,
# где, в свою очередь, прописываем функцию < def driver() > в параметр нашего тестового метода

# То есть:     в файле conftest есть     @pytest.fixture(scope='function')
#                                        def driver():
#              а в файле test_     указываем функцию < def driver() > из файле conftest
#                                  как параметр в нашем тестовом методе < def test_open_page(driver): >


@pytest.fixture(scope='function')                                                   # декоратор (по умолчанию параметр -функция - (scoupe='function'))
def driver():                                                                       # фикстура (как функция  driver() )
    print('start browser')                                                          # и мы можем, например, делать что-то вроде лога (???)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # установили наш драйвер
    driver.maximize_window()                                                        # полноэкранный режим отображения веб-страницы
    yield driver                                                                    # yield driver — это все равно что return driver (???)
    driver.quit()                                                                   # закрыть все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии