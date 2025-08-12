from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "login-username")
        self.password_field = (By.ID, "login-password")
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.message_div = (By.ID, "message")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.message_div)
            )
            return error_element.text.lower()
        except:
            return ""
