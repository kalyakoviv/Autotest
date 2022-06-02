import pytest
from selenium import webdriver

@pytest.fixture(scope="sessioin")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

