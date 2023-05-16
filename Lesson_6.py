''' ------------------- СТРУКТУРА ВЕБ-СТРАНИЦЫ ------------------------------------------------------------------------

-DOCUMENT OBJECT MODEL (DOM) - это представление HTML- документа в виде дерева тегов.

--------------------------- HTML ------------------------------------------------------------------------------------

- HTML (HyperText Markup Language — язык гипертекстовой разметки текста)- любая страница в интернете представляет собой html-файл,
                                                                         в котором с помощью языка разметки html описана её структура;

    - теги - специальные пометки, с помощью которых задаются начало и конец элементов на веб-странице с помощью языка html,
    - задача тегов - обозначить, какой именно тип информации они представляют (картинка, ссылка, текст, блок и т.д.),
    - у тегов есть атрибуты, которые определяют свойства элементов,
    - страница на языке html имеет иерархическую структуру;
    - иерархия тегов:
                    - предок (ancestor) - тег, внутри которого находятся прочие теги,
                    - потомок (descend ant) - вложенные теги,
                    - родитель (parent) - предок, имеющий первый уровень вложенности,
                    - дочерний элемент (child) - потомок, содержащийся непосредственно в родителе.


------------------------------ CSS ---------------------------------------------------------------------------------

- CSS (Cascading Style Sheets - каскадные таблицы стилей) - используется в вёрстке для красивого оформления страниц;
- СЕЛЕКТОРЫ (от англ. SELECT - выбирать) - это элементы каскадной таблицы стилей CSS, которые указывают на тот элемент на веб-странице,
                                           к которому должны будут применяться стили.

- поиск элементов по css-селекторам можно осуществить:
                      - с помощью ID - уникальный указатель на элемент,
                      - с помощью TAG - обозначает тип представляемой информации,
                      - с помощью значения атрибута,
                      - с помощью CLASS - чаще всего используют для задания правил вёрстки с помощью CSS.


---------------------------- JavaScript ----------------------------------------------------------------------------

- JavaScript - позволяет сделать веб-страницу интерактивной, т.е. реагировать на действия пользователей,
               запрашивать у пользователя данные и возвращать их.




-------------------------- ПОИСК ЭЛЕМЕНТОВ НА ВЕБ-СТРАНИЦЕ осуществляется ---------------------------------------------

- с помощью значений тегов  или атрибутов элементов: id, class и т.д.,
- с помощью SCC-селекторов - путь к элементу описывается через синтаксис CSS,
- с помощью языка запросов XPATH


- Fn + F12 - открыли DevTools
- Ctrl + F - появится поисковая строка

- пример: если в поисковой строке ввести title - увидим все теги title (8 штук, например),
          чтобы взять конкретный элемент, используем xpath - добавим // перед названием тега.

- перед названием класса ставим (.) - пример:  .entry-content

- пример запроса xpath: .entry-content p - здесь взяли div определённого класса и обратились к параграфу (p) внутри этого div`а.
                        если у родителя несколько одинаковых элементов, то к конкретному можно обратиться так: .entry-content p:nth-child(1)



--------------------------- ПОИСК ПО CSS-селекторам --------------------------------------------------------------------

Селектор                 Пример                       Пример описания
.class                   .intro                     выберет все элементы class="intro"
#id                      #firstname                 выберет все элементы id="firstname"
#id > div                #primary > div             выберет первый из дочерних элементов <div> в родительском элементе с id="primary"
#id div                  #primary div               выберет элемент <div> на любом уровне вложенности в родительском элементе с id="primary"
*                        *                          выберет все элементы
element                  p                          выберет все <p> элементы
element,element          div,p                      выберет все <div> элементы и все <p> элементы
element element          div p                      выберет все <p> элементы внутри <div> элемента
                         .<div> p:nth-child(2)      выберет дочерний элемент (по номеру, номер по порядку)
element > element        div > p                    выберет все <p> элементы, родительским элементом которых является элемент <div>
element + element        div + p                      выберет все элементы <p>, которые размещаются сразу после элементов <div>


------------------------------ Составные CSS-селекторы -------------------------------------------------------------

Не всегда есть возможность найти элемент на странице, используя простой селектор, т.к. такой селектор находит сразу несколько элементов.
В этом случае используют составные CSS-селекторы.

-------------- использование потомков: -----------

<div class="table">
    <bento/>
    <plate>
            <apple/>
    </plate>
    <apple/>
</div>

- для поиска элемента <apple/> внутри <plate> команда -->  plate apple
- символ пробела " " разделяет описание предка и потомка.


------------- использование дочерних элементов: ----------------

<div class="table">
    <plate>
        <bento>
             <apple/>
        </bento>
    </plate>
    <plate>
        <apple/>
    </plate>
    <plate/>
    <apple/>
    <apple class="small"/>
</div>

- для выбора элемента <apple/>, следующего прямо за <plate>, надо указать  -->   plate > apple



------------использование порядкового номера дочернего элемента: ----------------

-NTH-CHILD - псевдоселектор - позволяет выбирать элемент по порядковому номеру.

<div class="table">
    <plate/>                    #  plate:nth-child(1)  или  plate:first-child
    <plate/>                    #  plate:nth-child(2)
    <plate/>                    #  plate:nth-child(3)  или  plate:last-child
    <plate id="fancy"/>
</div>



---------------------------------- XPATH (XML PATH LANGUAGE) ----------------------------------------------------------

- это язык запросов, который использует древовидную структуру документа (DOM).

- XPATH-запрос всегда начинается с символа / - аналогичен символу > в CSS-селекторе,
                             или с символа // - аналогичен пробелу;

- их смысл:
    element1/element2  -->  выбирает элементы element2, которые являются прямыми потомками element1;
    element1//element2  -->  выбирает элементы element2, которые являются прямыми потомками element1 любой степени вложенности.
    (// - двойной форвард-слеш - означает --> возьми элемент в любом месте этого документа, в любой иерархии, на любом уровне вложенности)



- абсолютный (ABSOLUTE) XPATH:
        / HTML / BODY / DIV[2] / DIV[1] / DIV / H4[1] / B / HTML[1] / BODY[1] / DIV[2] / DIV[1] / DIV[1] / H4[1] / B[1]
        (элемент ищется с самого начала дерева...)

- относительный (RELATIVE) XPATH:
       // DIV[@CLASS='FEATURED-BOX CLOUMNSIZE1'] // H4[1] // B[1]
       пример: //div[@id='primary']/div  - выберет следующий div
               //div[@id='primary']/div  - выберет все div`ы в указанном id



- символ [] используется для фильтрации:
            - по атрибуту  -->  //p[@id='value']
            - по порядковому номеру  -->  //div[@class='value']/div[3]
            - по полному совпадению текста  -->  //p[text()='text sample']
            - по частичному совпадению текста  -->  //p[contains(text(), 'text sample')]

- символ * используется для выбора всех элементов - удобно, когда точно не известен тег элемента, который мы ищем,
            например:   //div/*[@class='value']


-------------------------- ПРИМЕЧАНИЕ -----------------------------------------

- с помощью CSS-селектора - синтаксис позволяет спускаться от предка к потомку (работает быстрее, чем XPATH).
     Когда невозможно подобрать CSS-селектор, используем XPATH-запрос.

- с помощью XPATH-запроса - можно двигаться как сверху вниз, так и снизу вверх (но ищет по структуре всего документа, работает медленнее, чем CSS-селекторы).
    Например, если у родительского элемента нет какого-то отличительного атрибута, то можно выйти на него от дочернего элемента.
    И при помощи XPATH можно выбрать элемент по конкретному тексту, или его части.

- пример XPATH-запроса <снизу вверх>   //*[@id='site-title']/../..   -->  две точки (..) означают переход на уровень выше от выбранного элемента.

- динамический id может иметь некоторое количество цифр/букв, и при обновлении страницы они меняются (например, сайт google.com).

------------------------------------ ТРЕНАЖЁРЫ -------------------------------------------------------------------------

- CSS - https://flukeout.github.io/

- XPATH - https://topswagcode.com/xpath/


















----------------- DEV TOOLS (инструменты разработчика)--------------------------

- Elements - для просмотра html и css элементов на веб-странице (можно так: ПКМ на элементе -> Просмотреть код)

- Console -

- Sources -

- Network -

- Performance -

- Memory -

- Application -

- Security -

- Lighthouse -

- AdBlock -



















'''


### МОЙ ТЕСТ====================================================

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = 'https://openweathermap.org/'
#
#
# def test_should_open_given_link(driver):
#     driver.get(URL)
#     assert 'openweathermap' in driver.current_url
#
#
# def test_check_page_title(driver):
#     driver.get(URL)
#     assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
#
#
# def test_section_where_to(driver):
#     driver.get(URL)
#     element_section_where_to_h1 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h1 .white-text")
#     assert element_section_where_to_h1.text == 'OpenWeather'
#
#     element_section_where_to_h2 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h2 .black-text")
#     assert element_section_where_to_h2.text == 'Weather forecasts, nowcasts and history in a fast and elegant way'


### ТЕСТ МАРИНЫ ===========================================================

# from selenium.webdriver.common.by import By
# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# URL = 'https://openweathermap.org/'
# cities = ['New York', 'Los Angeles', 'Paris']
# load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
# search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
# search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
# search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
# search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
# displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
# sign_in_link = (By.CSS_SELECTOR, '.user-li a')
# pricing_link = (By.CSS_SELECTOR, '#desktop-menu a[href="/price"]')
# price_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
# accept_cookies = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')
#
#
# def test_should_open_given_link(driver):
#     driver.get(URL)
#     assert 'openweathermap' in driver.current_url
#
#
# def test_check_page_title(driver):
#     driver.get('https://openweathermap.org/')
#     assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'
#
#
# @pytest.mark.parametrize('city', cities)
# def test_fill_search_city_field(driver, city):
#     driver.get('https://openweathermap.org/')
#     wait = WebDriverWait(driver, 15)
#     wait.until_not(EC.presence_of_element_located(load_div))
#     search_city_input = driver.find_element(*search_city_field)
#     search_city_input.send_keys(city)
#     driver.find_element(*search_button).click()
#     wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
#     expected_city = city
#     wait.until(EC.text_to_be_present_in_element(displayed_city, city))
#     actual_city = driver.find_element(*displayed_city).text
#     assert expected_city in actual_city
#
#
# @pytest.mark.parametrize('city', cities)
# def test_all_dropdown_options_should_contain_valid_city(driver, city):
#     driver.get('https://openweathermap.org/')
#     wait = WebDriverWait(driver, 15)
#     wait.until_not(EC.presence_of_element_located(load_div))
#     search_city_input = driver.find_element(*search_city_field)
#     search_city_input.send_keys(city)
#     driver.find_element(*search_button).click()
#     options = driver.find_elements(*search_dropdown)
#     for option in options:
#         assert city in option.text
#
#
# @pytest.fixture()
# def open_and_load_page(driver, wait):
#     driver.get(URL)
#     wait.until_not(EC.presence_of_element_located(load_div))
#
#
# @pytest.fixture()
# def wait(driver):
#     wait = WebDriverWait(driver, 25)
#     yield wait
#
#
# def test_should_go_to_sign_in_page(driver, open_and_load_page, wait):
#     sign_link = wait.until(EC.presence_of_element_located(sign_in_link))
#     driver.execute_script("arguments[0].click();", sign_link)
#     assert "sign_in" in driver.current_url, f"\nWrong URL - {driver.current_url}"
#
#
# def test_should_be_valid_title_on_price_page(driver, open_and_load_page, wait):
#     element = driver.find_element(*pricing_link)
#     action_chains = ActionChains(driver)
#     action_chains.move_to_element(element)
#     driver.execute_script("arguments[0].click();", element)
#     pricing_text = driver.find_element(*price_page_title).text
#     assert pricing_text == "Pricing"
#
#
# def test_should_be_valid_text_in_sign_in_tab(driver, open_and_load_page, wait):
#     driver.find_element(*accept_cookies).click()
#     expected_text = 'Sign in'
#     element = driver.find_element(*sign_in_link)
#     sign_in_text = driver.execute_script("return arguments[0].textContent", element)
#     assert sign_in_text == expected_text



