from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class MainPage(BasePage):



    def category_1(self):
        images_clicking = self.browser.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]"))
        images_clicking.click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        category = self.browser.find_element(By.CSS_SELECTOR, '[class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
        category.click()
        time.sleep(5)

    def check_category(self):
        if self.browser.find_element(By.TAG_NAME, "title") != 0:
            print('Название категории отображается')
        else:
            print('Название категории не отобразилось')

    def open_image(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)

    def forward_button(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)
        button_forward = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_next"]')
        button_forward.click()
        time.sleep(5)

    def back_button(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)
        button_forward = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_next"]')
        button_forward.click()
        time.sleep(2)
        button_back = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_prev"]')
        button_back.click()
        time.sleep(2)

    def check_step_8(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR, '[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)
        img_3 = self.browser.current_url
        button_forward = self.browser.find_element(By.CSS_SELECTOR, 'div[class*="Button_type_next"]')
        button_forward.click()
        time.sleep(2)
        button_back = self.browser.find_element(By.CSS_SELECTOR, 'div[class*="Button_type_prev"]')
        button_back.click()
        time.sleep(2)
        img_4 = self.browser.current_url
        if img_3 == img_4:
            print("Картинка осталась из шага 8")
        else:
            print("Картинка не из шага 8")

    def test_number_2(self):
        assert self.search_present(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]")), "There is no link to 'Pictures'"
        time.sleep(2)
        images_clicking = self.browser.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]"))
        images_clicking.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        print("ssylka", self.browser.current_url)
        assert self.search_present(By.XPATH, ('//*[@id="tabs-navigation-placeholder"]/div/a[2]/div[2]')), "This is not a website https://yandex.ru/images/"
        category = self.browser.find_element(By.CSS_SELECTOR, '[class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
        category.click()
        time.sleep(2)
        if self.browser.find_element(By.TAG_NAME, "title") != 0:
            print('Название категории отображается')
        else:
            print('Название категории не отобразилось')
        image_op = self.browser.find_element(By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(2)
        assert self.search_present(By.CSS_SELECTOR,'[class ="Modal Modal_visible Modal_theme_normal MMViewerModal ImagesViewer"]'), "The picture didn't open"
        time.sleep(5)
        img_1 = self.browser.current_url
        button_forward = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_next"]')
        button_forward.click()
        time.sleep(2)
        img_2 = self.browser.current_url
        if img_1 != img_2:
            print("Картинка сменилась")
        else:
            print("Картинка не сменилась")
        button_back = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_prev"]')
        button_back.click()
        time.sleep(2)
        img_4 = self.browser.current_url
        if img_1 == img_4:
            print("Картинка осталась из шага 8")
        else:
            print("Картинка не из шага 8")


    def change_image(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR, '[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)
        img_1 = self.browser.current_url
        button_forward = self.browser.find_element(By.CSS_SELECTOR,'div[class*="Button_type_next"]')
        button_forward.click()
        time.sleep(5)
        img_2 = self.browser.current_url
        if img_1 != img_2:
            print("Картинка сменилась")
        else:
            print("Картинка не сменилась")


    def check_image_open(self):
        image_op = self.browser.find_element(By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
        image_op.click()
        time.sleep(5)
        assert self.search_present(By.CSS_SELECTOR,'[class ="Modal Modal_visible Modal_theme_normal MMViewerModal ImagesViewer"]'), "The picture didn't open"
        time.sleep(5)

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

    def should_images(self):
        assert self.search_present(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]")), "There is no link to 'Pictures'"
        time.sleep(3)

    def search_images_url(self):
        images_clicking = self.browser.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]"))
        images_clicking.click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        print("ssylka", self.browser.current_url)
        assert self.search_present(By.XPATH, ('//*[@id="tabs-navigation-placeholder"]/div/a[2]/div[2]')), "This is not a website https://yandex.ru/images/"

    def check_images_clicking(self):
        images_clicking = self.browser.find_element(By.XPATH, ("/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]"))
        images_clicking.click()
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

    def test_number_1(self):
        assert self.search_present(By.NAME, "text"), "The search field is missing"
        search_tenz = self.browser.find_element(By.NAME, "text")
        search_tenz.click()
        search_tenz.send_keys("Тензор")
        assert self.search_table_with_hints(By.XPATH, ("/html/body/div[3]")), "There is no table with hints"
        search_tenz.send_keys(Keys.RETURN)
        tenzor_ru = self.browser.find_element(By.XPATH, ('//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/h2/span'))
        tenzor_ru.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        print("ssylka", self.browser.current_url)
        assert self.search_present(By.NAME, "headerLogo"), "This is not a website tensor.ru"