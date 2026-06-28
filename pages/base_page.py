from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Метод для открытия URL
    def open_url(self, url):
        self.driver.get(url)

    # Ожидание, пока элемент станет видимым, и его поиск
    def find_element_with_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось дождаться видимости элемента: {locator}"
        )

    # Клик по элементу (сначала ждем его)
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    # Получение текста из элемента
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Прокрутка до элемента
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Клик через JavaScript (помогает, если элемент перекрыт другими объектами)
    def js_click(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    # Локаторы логотипов в шапке
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']/parent::a")
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']/parent::a")

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось дождаться видимости элемента: {locator}"
        )

    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_click(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # --- Новые методы для работы с логотипами и вкладками ---
    
    # Метод для переключения на только что открывшуюся вкладку
    def switch_to_new_window(self):
        # Получаем список всех открытых вкладок
        all_windows = self.driver.window_handles
        # Переключаемся на последнюю созданную вкладку
        self.driver.switch_to.window(all_windows[-1])

    # Метод для ожидания, пока в URL появится конкретный текст (нужно для Дзена)
    def wait_for_url_contains(self, text, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.url_contains(text),
            message=f"URL не содержит текст: {text}"
        )