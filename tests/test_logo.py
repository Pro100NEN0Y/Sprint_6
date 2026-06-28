import allure
from pages.main_page import MainPage

class TestLogoRedirects:

    @allure.title("Клик на логотип 'Самокат' возвращает на главную страницу")
    def test_logo_scooter_redirect_to_main(self, driver):
        main_page = MainPage(driver)
        
        # 1. Открываем главную страницу Самоката
        main_page.open_main_page()
        
        # 2. Кликаем по верхней кнопке заказа, чтобы уйти с главной страницы
        main_page.click_order_button(main_page.TOP_ORDER_BUTTON)
        
        # 3. Кликаем по логотипу «Самокат»
        main_page.click_to_element(main_page.LOGO_SCOOTER)
        
        # 4. Проверяем, что текущий URL — это снова главная страница Самоката
        current_url = driver.current_url
        assert current_url == main_page.URL, f"Ожидался URL главной страницы, но получили {current_url}"

    @allure.title("Клик на логотип 'Яндекс' открывает Дзен в новой вкладке")
    def test_logo_yandex_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        
        # 1. Открываем главную страницу Самоката
        main_page.open_main_page()
        
        # 2. Кликаем по логотипу «Яндекс»
        main_page.click_to_element(main_page.LOGO_YANDEX)
        
        # 3. Переключаемся на новую вкладку, которая открылась после клика
        main_page.switch_to_new_window()
        
        # 4. Ждем, пока страница Дзена загрузится (в URL должно появиться слово 'dzen' или 'yandex')
        main_page.wait_for_url_contains("dzen")
        
        # 5. Проверяем, что в текущем URL есть упоминание dzen
        assert "dzen.ru" in driver.current_url, f"Дзен не открылся. Текущий URL: {driver.current_url}"