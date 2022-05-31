from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/')

# seearchbox = driver.find_element_by_xpath("//*[@id="search"]")
# searchbox.send_keys('igor qa')

# seearchbox = driver.find_element_by_xpath('//*[@id="search"]')

time.sleep(5)

driver.close()
driver.quit()



