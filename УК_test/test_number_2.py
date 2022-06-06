from pages.main_page import MainPage

import time

def test_1(browser):
    main_page = MainPage(browser, url='https://yandex.ru/')
    main_page.main_page_link() # Зайти на yandex.ru
    main_page.should_images() # Проверить, что ссылка «Картинки» присутствует на странице
    main_page.images_click() # Кликаем на ссылку «Картинки»
    main_page.search_images_0() # Проверяем, что перешли на url https://yandex.ru/images/
    main_page.open_1_categoty() # Открыть первую категорию
    main_page.check_category_images() # Проверить, что название категории отображается в поле поиска
    main_page.open_image_number_1() # Открыть 1 картинку
    main_page.check_open_image_1() # Проверить, что картинка открылась
    main_page.press_button_forward() # Нажать кнопку вперед
    time.sleep(2)