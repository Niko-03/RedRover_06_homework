from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# эту строку < driver.get('https://openweathermap.org/') > пишем в каждом тестовом методе
# потому, что в фикстуре мы сказали, что она - фикстура - распространяется на функцию(!)  -->  @pytest.fixture(scoupe='function')

# если фикстура распространяется на сессию - < @pytest.fixture(scope='session') >,
# то <driver.get('https://openweathermap.org/')> не надо писать в каждом тестовом методе

# если скобки в фикстуре пустые < @pytest.fixture() >,то по умолчанию параметр - функция - (scoupe='function')

# тесты должны быть независимыми (одна проверка - один тест), поэтому  -->  @pytest.fixture(scoupe='function') - распространяется на функцию


def test_open_page(driver):                                 # в скобках - наша фикстура, как параметр нашего тестового метода
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)                               # можно без этой строки, делать только assert


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
    print(driver.title)


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')

    search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[class='button-round dark']")))
    search_button.click()

    search_option = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")))
    search_option.click()
    time.sleep(10)

    expected_city = 'New York City, US'
    displayed_city = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")))
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city

