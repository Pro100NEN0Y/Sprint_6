import allure

@allure.suite("Тестирование переходов по логотипам")
@allure.sub_suite("Проверка логотипа Самоката")
def test_click_logo_scooter_opens_main_page(driver, main_page):
    
    # 1. Открываем главную страницу Самоката
    main_page.open_url("https://qa-scooter.praktikum-services.ru/")
    
    # 2. Кликаем по кнопке «Заказать» вверху (чтобы уйти на страницу оформления заказа)
    main_page.click_order_button(main_page.TOP_ORDER_BUTTON)
    
    # 3. Кликаем по логотипу «Самокат»
    main_page.click_to_element(main_page.LOGO_SCOOTER)
    
    # 4. Проверяем, что текущий URL — это снова главная страница Самоката
    current_url = main_page.get_current_url()
    
    # 5. Проверяем соответствие URL ожидаемому результату
    assert current_url == "https://qa-scooter.praktikum-services.ru/"