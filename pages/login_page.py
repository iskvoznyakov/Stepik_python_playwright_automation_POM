from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator('#username')
        self.password_field = page.locator('#password')
        self.login_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')

    def navigate(self):
        """Открывает страницу логина"""
        self.page.goto('https://zimaev.github.io/pom/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными логином и паролем"""
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text()
