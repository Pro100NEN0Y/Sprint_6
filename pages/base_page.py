import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу по URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Кликаем по элементу {locator}")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()