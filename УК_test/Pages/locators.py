from selenium.webdriver.common.by import By


class BasePageLocators():

    IMAGES_LOCATOR = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/nav/div/ul/li[5]/a/div[2]")
    IMAGES_RU_LOCATOR = (By.XPATH, '//*[@id="tabs-navigation-placeholder"]/div/a[2]/div[2]')
    CATEGORY_LOCATOR = (By.CSS_SELECTOR, '[class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    CATEGORY_NAME_LOCATOR = (By.TAG_NAME, "title")
    IMAGE_OPEN_LOCATOR = (By.CSS_SELECTOR,'[class="serp-item__preview"]:first-child')
    CHECK_IMAGE_OPEN_LOCATOR = (By.CSS_SELECTOR, '[class ="Modal Modal_visible Modal_theme_normal MMViewerModal ImagesViewer"]')
    BUTTON_FORWARD_LOCATOR = (By.CSS_SELECTOR,'div[class*="Button_type_next"]')
    BUTTON_BACK_LOCATOR = (By.CSS_SELECTOR,'div[class*="Button_type_prev"]')