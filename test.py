from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://yandex.ru/")
time.sleep(1)

search = driver.find_element_by_name("text")

search.send_keys("Тензор")
time.sleep(5)

search.send_keys(Keys.RETURN)
time.sleep(5)

tenzor = driver.find_elements_by_xpath('//*[@id="search-result"]/li[1]/div/div[1]/a/h2')
tenzor.click()
time.sleep(5)

pass