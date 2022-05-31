from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.youtube.com/')
seearchbox = driver.find_element_by_xpath('//*[@id="search"]
')



