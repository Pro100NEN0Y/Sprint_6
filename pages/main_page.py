import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Кнопка «Заказать» вверху страницы
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_')]//button[text()='Заказать']")
    
    # Кнопка «Заказать» внизу страницы (ищем кнопку с текстом "Заказать" внутри контента страницы)
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_')]//button[text()='Заказать']")

    # URL главной страницы
    URL = 'https://qa-scooter.praktikum-services.ru/' # Или точный URL Самоката из твоего задания

    # Динамический локатор для стрелочки вопроса (num — это индекс от 0 до 7)
    QUESTION_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-{}']")
    
    # Динамический локатор для открывающегося текста ответа
    ANSWER_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-{}']")

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.open_url(self.URL)

    @allure.step("Кликаем на вопрос номер {num}")
    def click_question(self, num):
        method, locator_string = self.QUESTION_LOCATOR
        formatted_locator = (method, locator_string.format(num))
        
        self.scroll_to_element(formatted_locator)
        # Меняем обычный клик на js_click
        self.js_click(formatted_locator)

    @allure.step("Получаем текст ответа номер {num}")
    def get_answer_text(self, num):
        method, locator_string = self.ANSWER_LOCATOR
        formatted_locator = (method, locator_string.format(num))
        
        # .strip() удалит невидимые пробелы по краям, если они есть
        return self.get_text_from_element(formatted_locator).strip()
    
    @allure.step("Кликаем по кнопке 'Заказать' (локатор: {locator})")
    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.js_click(locator)