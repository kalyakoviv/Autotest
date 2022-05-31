from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.youtube.com/')

seearchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('9999999999999999')