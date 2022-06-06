from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from .locators import BasePageLocators

class MainPage(BasePage):

    def main_page_link(self):
        page = MainPage(self.browser, self.url)
        page.open()

    def link_pictures_present_page(self):
        assert self.search_present(*BasePageLocators.IMAGES_LOCATOR), "Ссылка 'Картинки' отсутствует"

    def images_click(self):
        images_clk = self.browser.find_element(*BasePageLocators.IMAGES_LOCATOR)
        images_clk.click()

    def search_images_url_yandex(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        print("Текущая ссылка: ", self.browser.current_url)

    def open_first_categoty(self):
        category = self.browser.find_element(*BasePageLocators.CATEGORY_LOCATOR)
        category.click()

    def check_name_category_images(self):
        assert self.search_present(*BasePageLocators.CATEGORY_NAME_LOCATOR), "Название категории не отобразилось"

    def open_image_number_one(self):
        image_open = self.browser.find_element(*BasePageLocators.IMAGE_OPEN_LOCATOR)
        image_open.click()

    def check_open_image_number_one(self):
        assert self.search_present(*BasePageLocators.CHECK_IMAGE_OPEN_LOCATOR), "Картинка не открылась"

    def press_button_forward(self):

        button_forward = self.browser.find_element(*BasePageLocators.BUTTON_FORWARD_LOCATOR)
        button_forward.click()

    def press_button_back(self):
        button_back = self.browser.find_element(*BasePageLocators.BUTTON_BACK_LOCATOR)
        button_back.click()

    def check_presence_search_field(self):
        assert self.search_present(*BasePageLocators.YANDEX_SEARCH_LOCATOR), "Поле поиска отсутствует"

    def enter_tensor_search(self):
        search_tenz = self.browser.find_element(*BasePageLocators.YANDEX_SEARCH_LOCATOR)
        search_tenz.click()
        search_tenz.send_keys("Тензор")

    def table_with_hints_appeared(self):
        assert self.search_present(*BasePageLocators.TABLE_WITH_HINTS_APPEARED_LOCATOR), "Таблица с подсказками не появилась"

    def enter_search_results(self):
        search_enter = self.browser.find_element(*BasePageLocators.YANDEX_SEARCH_LOCATOR)
        search_enter.send_keys(Keys.RETURN)

    def opening_first_link(self):
        results = self.browser.find_element(*BasePageLocators.TENZOR_LOCATOR)
        results.click()
