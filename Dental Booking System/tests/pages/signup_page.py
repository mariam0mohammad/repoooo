import time
import requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//h2[text()='Sign Up']/following::input[1]")
        self.password_input = (By.XPATH, "//h2[text()='Sign Up']/following::input[2]")
        self.phone_input = (By.XPATH, "//h2[text()='Sign Up']/following::input[3]")
        self.signup_button = (By.XPATH, "//h2[text()='Sign Up']/following::button[1]")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_input).clear()
        self.driver.find_element(*self.phone_input).send_keys(phone)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()

    def get_api_response(self, username, password, phone):
        url = "http://localhost:3000/signup"
        data = {
            "username": username,
            "password": password,
            "phone": phone
        }
        response = requests.post(url, json=data)
        return response.status_code, response.json()

    def get_ui_message(self):
        """إرجاع الرسالة أو محتوى الصفحة بعد التسجيل"""
        time.sleep(1)  # انتظار قصير لظهور الرسالة

        try:
            alert = self.driver.switch_to.alert
            msg = alert.text.strip()
            alert.accept()
            return msg
        except NoAlertPresentException:
            pass

        try:
            msg_elem = self.driver.find_element(By.ID, "message")
            return msg_elem.text.strip()
        except NoSuchElementException:
            pass

        # إذا ما فيه رسالة مباشرة، رجع أول 100 حرف من نص الصفحة
        return self.driver.find_element(By.TAG_NAME, "body").text.strip()[:100]
