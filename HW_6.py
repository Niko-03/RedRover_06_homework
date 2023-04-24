'''
6.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples

6.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html

'''

# 6.1

# вариант_1_CSS
# .bg-light div:nth-child(2) :nth-child(3)


# вариант_2_XPATH
# //button[text()='Gold']

# вариант_3_XPATH
# //body[@class='bg-light']/div[2]/button[3]


# 6.2

# вариант_1_CSS
# .row .col-sm-4:nth-child(5) p       --- по дочернему элементу в классе    (.class .class:nth-child(5) p)

# вариант_2_XPATH
# //p[text()='Fully charged cat']     --- по полному совпадению текста

# вариант_3_XPATH
# //div[@class='row']/div[5]/div/div/p   --- по элементам сверху вниз



