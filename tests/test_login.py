import pytest
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Авторизация')
@allure.title('Авторизация с невалидными данными')
@allure.description('Авторизация с некорректными username и password')
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму некорректные данные: username: "invalid_username" и password: "invalid_password"'):
        login_page.login(username="invalid_username", password="invalid_password")

    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == "Invalid credentials. Please try again.", "Wrong error message"


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Авторизация')
@allure.title('Авторизация с валидными данными')
@allure.description('Авторизация с корректными username и password')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step(f'Ввести в форму корректные данные: username:{username} и password:{password}'):
        login_page.login(username=username, password=username)

    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(message=f"Welcome {username}")
