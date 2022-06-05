from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/')

time.sleep(5)

driver.close()
driver.quit()



