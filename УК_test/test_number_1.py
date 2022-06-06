from pages.main_page import MainPage
from selenium.webdriver.common.keys import Keys

import time

def test_1(browser):
    main_page = MainPage(browser, url='https://yandex.ru/')
    main_page.main_page_link() # Зайти на yandex.ru
    main_page.check_presence_search_field() # Проверить наличие поля поиска
    main_page.enter_tensor_search() # Ввести в поиск Тензор
    main_page.table_with_hints_appeared() # Проверить, что появилась таблица с подсказками (suggest)
    main_page.ENTER_search_results()    # При нажатии Enter появляется таблица результатов поиска
    main_page.opening_first_link()
    main_page.checking_first_link() # Проверить 1 ссылка ведет на сайт tensor.ru
