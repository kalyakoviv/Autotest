from pages.main_page import MainPage

import time

# Зайти на yandex.ru
def test_open_123(browser):
    main_page = MainPage(browser, url='https://yandex.ru/')
    main_page.main_page_link()
    time.sleep(1)

# Зайти на yandex.ru
def test_open(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open
    time.sleep(3)


def main_page_link(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()


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

# Нажать кнопку вперед
def test_forward_button(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.forward_button()

# Проверить, что картинка сменилась
def test_change_image(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.change_image()

# Нажать назад
def test_back_button(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.back_button()

# Проверить, что картинка осталась из шага 8
def test_check_step_8(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.category_1()
    page.check_step_8()

# Полный цикл
def test_Number_2(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.test_number_2()