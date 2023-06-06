from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ================================================================================================================
# browser.get('https://suninjuly.github.io/xpath_examples')                # метод get - переход на страницу сайта

# def test_open():
#     browser.get('https://suninjuly.github.io/xpath_examples')
#
#
# time.sleep(5)

# ==================================================================================================================
# browser.get('https://suninjuly.github.io/cats.html')                                      # открыли станицу сайта
# time.sleep(5)
# bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")        # нашли элемент через xpath-запрос
# print(bullet_cat.text)
# #
# view_button = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")            # нашли несколько элементов через xpath-запрос
# print(view_button)
# assert len(view_button) == 6, 'Wrong length'                                              # ???
# # assert len(view_button) == 5, 'Wrong length'                                              # ??? будет ошибка

# =================================================================================================================


def open_page():
    browser.get('https://suninjuly.github.io/cats.html')

    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    print(bullet_cat.text)

    view_button = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_button)
    assert len(view_button) == 6, 'Wrong length'


def test_open_page():
    open_page()


