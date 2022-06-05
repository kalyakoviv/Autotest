import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element_by_xpath("/html/body/div[1]/form/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div[1]/form/div[3]/input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//*[@id="submit_button"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла