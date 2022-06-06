from selenium.webdriver.common.by import By


class BasePageLocators():

    IMAGES_LOCATOR = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]")
    KATEGORY_LOCATOR = (By.CSS_SELECTOR, '[class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
