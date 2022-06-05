from pages.main_page import MainPage
import time

# Зайти на yandex.ru
def test_open(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(1)

# Проверить наличие поля поиска
def test_should_be_search(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search()

# Ввести в поиск Тензор
def test_tenzor(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.search_tenzor()

# Проверить, что появилась таблица с подсказками (suggest)
def test_should_search_table_with_hints(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.search_tenzor()
    page.should_search_table_with_hints()

# При нажатии Enter появляется таблица результатов поиска
def test_enter(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.search_enter_clicking()

# Проверить 1 ссылка ведет на сайт tensor.ru
def test_tenzor_ru(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_tenzor_ru()

# Полный цикл
def test_number_1(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.test_number_1()
