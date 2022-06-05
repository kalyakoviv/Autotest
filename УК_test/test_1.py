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
    time.sleep(1)
    page.should_be_search()
    time.sleep(7)

# Ввести в поиск Тензор

def test_tenzor(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(1)
    page.should_be_search()
    time.sleep(7)
    page.search_tenzor()
    time.sleep(2)

