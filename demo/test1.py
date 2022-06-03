from YandexPages import SearchHelper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "пук" and "Видео" in elements

test_yandex_search(webdriver.Chrome(ChromeDriverManager().install()))