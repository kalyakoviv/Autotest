from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

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
        time.sleep(5)

    def search_tenzor(self):
        search_tenz = self.browser.find_element(By.NAME, "text")
        search_tenz.click()
        search_tenz.send_keys("Тензор")
        time.sleep(2)

    def should_search_table_with_hints(self):
        assert self.search_table_with_hints(By.XPATH, ("/html/body/div[3]")), "There is no table with hints"
        time.sleep(3)

    def search_enter_clicking(self):
        search_tenz = self.browser.find_element(By.NAME, "text")
        search_tenz.click()
        search_tenz.send_keys("Тензор")
        search_tenz.send_keys(Keys.RETURN)
        time.sleep(3)

    def check_tenzor_ru(self):
        search_tenz = self.browser.find_element(By.NAME, "text")
        search_tenz.click()
        search_tenz.send_keys("Тензор")
        search_tenz.send_keys(Keys.RETURN)
        tenzor_ru = self.browser.find_element(By.XPATH, ('//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/h2/span'))
        tenzor_ru.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        print("ssylka", self.browser.current_url)
        assert self.search_present(By.NAME, "headerLogo"), "This is not a website tensor.ru"