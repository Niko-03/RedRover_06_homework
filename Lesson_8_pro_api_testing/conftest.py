# ---------------------- про_ФИКСТУРЫ -----------------------------------------------

# выносим сюда установку нашего драйвера (инициализируем драйвер)

from selenium import webdriver                                       # необходимые импорты
import pytest
from webdriver_manager.chrome import ChromeDriverManager             # определились с браузером (Chrome)
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='session')                   # задаём декоратор, чтобы pytest распознавал функцию def driver(), как фикстуру (в () определяем, на какой уровень распространяется фикстура)
def driver():                                       # фикстура (как функция def driver() )
    print('start browser')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # создали экземпляр выбранного драйвера (браузера) и установили драйвер в фикстуру
    driver.maximize_window()                        # полноэкранный режим отображения веб-страницы
    yield driver                                    # yield почти то же самое, что и retern (???)
    driver.quit()                                   # закрыть все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии










