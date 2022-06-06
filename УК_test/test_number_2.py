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
    img_1 = browser.current_url
    main_page.press_button_forward() # Нажать кнопку вперед
    img_2 = browser.current_url
    # Проверить, что картинка сменилась
    if img_1 != img_2:
        print("Картинка сменилась")
    else:
        print("Картинка не сменилась")

    main_page.press_button_back() # Нажать назад
    time.sleep(2)
    img_3 = browser.current_url
    # Проверить, что картинка осталась из шага 8
    if img_1 == img_3:
        print("Картинка осталась из шага 8")
    else:
        print("Картинка не соответствует картинке из шага 8")
