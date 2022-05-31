#from lib2to3.pgen2 import driver
# from selenium import webdriver
# driver = webdriver.Chrome()

# driver.get('https://www.youtube.com/')

# seearchbox = driver.find_element_by_xpath('//*[@id="search"]')


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('99999999999999999999999')

time.sleep(10)

driver.close()
#driver.quit()