from pages.main_page import MainPage


def test_search_tenzor(browser):
    main_page = MainPage(browser, url='https://yandex.ru/')
    main_page.main_page_link() # Зайти на yandex.ru
    main_page.check_presence_search_field() # Проверить наличие поля поиска
    main_page.enter_tensor_search() # Ввести в поиск Тензор
    main_page.table_with_hints_appeared() # Проверить, что появилась таблица с подсказками (suggest)
    main_page.enter_search_results()    # При нажатии Enter появляется таблица результатов поиска
    main_page.opening_first_link() # Открыть первую ссылку
    # Проверить 1 ссылка ведет на сайт tensor.ru
    browser.switch_to.window(browser.window_handles[1])
    browser.refresh()
    tap_link = browser.current_url
    assert 'tensor.ru' in tap_link, "Ссылка не ведет на сайт tensor.ru"
