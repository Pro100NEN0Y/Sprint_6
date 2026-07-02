import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title("Позитивный флоу оформления заказа самоката")
    @pytest.mark.parametrize(
        "order_button_locator_name, name, surname, address, metro, phone, date, rent_time, color, comment",
        [
            # Набор данных №1: Верхняя кнопка
            ("TOP_ORDER_BUTTON", "Иван", "Петров", "ул. Ленина, д. 10", "Черкизовская", "79991112233", "28.06.2026", "сутки", "чёрный жемчуг", "Позвонить за час"),
            # Набор данных №2: Нижняя кнопка
            ("BOTTOM_ORDER_BUTTON", "Анна", "Смирнова", "Проспект Мира, д. 25, кв. 4", "Сокольники", "89112223344", "29.06.2026", "двое суток", "серая безысходность", "Оставить у двери")
        ]
    )
    def test_positive_order_flow(self, driver, order_button_locator_name, name, surname, address, metro, phone, date, rent_time, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Шаг 1: Открываем главную страницу
        main_page.open_main_page()
        
        # Шаг 2: Выбираем кнопку заказа на основе параметров
        if order_button_locator_name == "TOP_ORDER_BUTTON":
            locator = main_page.TOP_ORDER_BUTTON
        else:
            locator = main_page.BOTTOM_ORDER_BUTTON
            
        # Шаг 3: Переходим к оформлению
        main_page.click_order_button(locator)
        
        # Шаг 4: Заполняем форму "Для кого самокат"
        order_page.fill_first_order_form(name, surname, address, metro, phone)
        
        # Шаг 5: Заполняем форму "Про аренду"
        order_page.fill_second_order_form(date, rent_time, color, comment)
        
        # Шаг 6: Подтверждаем заказ
        order_page.confirm_order()
        
        # Шаг 7: Проверяем результат
        assert order_page.is_order_placed_success(), "Окно успешного заказа не появилось!"