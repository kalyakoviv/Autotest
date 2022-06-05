from selenium.webdriver.common.by import By
from .base_page import BasePage

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

    def should_be_search(self):
        assert self.search_present(By.NAME, "text"), "The search field is missing"

    def search_tenzor(self):
        search_tenz = self.browser.find_element(By.NAME, "text")
        search_tenz.click()
        search_tenz.send_keys("Тензор")

    def should_search_table_with_hints(self):
        assert self.search_table_with_hints(By.XPATH, ("/html/body/div[3]")), "There is no table with hints"