import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()