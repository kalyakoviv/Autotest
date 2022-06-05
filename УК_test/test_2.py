from pages.main_page import MainPage
import time

# Зайти на yandex.ru
def test_open(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    time.sleep(1)

# Проверить, что ссылка «Картинки» присутствует на странице
def test_should_be_search(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_images()

# Кликаем на ссылку «Картинки»
def test_search_images_clicking(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_images_clicking()

# Проверяем, что перешли на url https://yandex.ru/images/
def test_search_images_url(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.search_images_url()

# Открыть первую категорию
def test_open_category(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()

# Проверить, что название категории отображается в поле поиска
def test_check_category(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.check_category()

# Открыть 1 картинку
def test_open_image(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.open_image()

# Проверить, что картинка открылась
def test_check_image_open(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.check_image_open()




