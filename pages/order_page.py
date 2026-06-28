import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    # --- Локаторы Первой формы («Для кого самокат») ---
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Динамический локатор для выбора станции из выпадающего списка
    METRO_OPTION_TEMPLATE = (By.XPATH, ".//div[text()='{}']")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # --- Локаторы Второй формы («Про аренду») ---
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    # Динамический локатор для выбора срока аренды (например, "сутки", "двое суток")
    RENT_TIME_OPTION_TEMPLATE = (By.XPATH, ".//div[@class='Dropdown-option' and text()='{}']")
    
    # Чекбоксы цвета (выбираем по тексту)
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    
    # Финальная кнопка «Заказать» в конце формы (ищем по тексту кнопки внутри контейнера кнопок)
    FINAL_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    
    # Кнопка подтверждения «Да» в модальном окне
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    
    # Окно успешного заказа
    ORDER_PLACED_HEADER = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")

    @allure.step("Заполняем первую форму: Имя='{name}', Фамилия='{surname}', Адрес='{address}', Метро='{metro}', Телефон='{phone}'")
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.find_element_with_wait(self.NAME_INPUT).send_keys(name)
        self.find_element_with_wait(self.SURNAME_INPUT).send_keys(surname)
        self.find_element_with_wait(self.ADDRESS_INPUT).send_keys(address)
        
        # Выбор метро: кликаем, вводим название, кликаем по выпадающей опции
        metro_field = self.find_element_with_wait(self.METRO_INPUT)
        metro_field.send_keys(metro)
        method, locator_str = self.METRO_OPTION_TEMPLATE
        formatted_metro_locator = (method, locator_str.format(metro))
        self.click_to_element(formatted_metro_locator)
        
        self.find_element_with_wait(self.PHONE_INPUT).send_keys(phone)
        self.click_to_element(self.NEXT_BUTTON)

    @allure.step("Заполняем вторую форму: Дата='{date}', Срок='{rent_time}', Цвет='{color}', Комментарий='{comment}'")
    def fill_second_order_form(self, date, rent_time, color, comment):
        # Заполнение даты и закрытие календаря нажатием Enter
        date_field = self.find_element_with_wait(self.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        # Выбор срока аренды
        self.click_to_element(self.RENT_TIME_DROPDOWN)
        method, locator_str = self.RENT_TIME_OPTION_TEMPLATE
        formatted_rent_locator = (method, locator_str.format(rent_time))
        self.click_to_element(formatted_rent_locator)
        
        # Выбор цвета самоката
        if color == "чёрный жемчуг":
            self.click_to_element(self.BLACK_COLOR_CHECKBOX)
        elif color == "серая безысходность":
            self.click_to_element(self.GREY_COLOR_CHECKBOX)
            
        self.find_element_with_wait(self.COMMENT_INPUT).send_keys(comment)
        self.click_to_element(self.FINAL_ORDER_BUTTON)

    @allure.step("Подтверждаем заказ в модальном окне")
    def confirm_order(self):
        self.click_to_element(self.CONFIRM_YES_BUTTON)

    @allure.step("Проверяем появление окна об успешном создании заказа")
    def is_order_placed_success(self):
        # Метод вернет True, если элемент с текстом "Заказ оформлен" станет видимым
        return self.find_element_with_wait(self.ORDER_PLACED_HEADER).is_displayed()