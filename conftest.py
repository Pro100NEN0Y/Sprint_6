import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Настраиваем и запускаем Firefox
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()