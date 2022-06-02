from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://yandex.ru/")
time.sleep(1)

search = driver.find_element_by_name("text")

search.send_keys("Тензор")
time.sleep(5)

suggest = driver.find_element_by_xpath("/html/body/div[3]")
time.sleep(5)

search.send_keys(Keys.RETURN)
time.sleep(5)

tenzor = driver.find_element_by_xpath('//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/h2/span')
tenzor.click()
time.sleep(10)

pass