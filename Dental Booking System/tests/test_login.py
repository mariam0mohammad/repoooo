import pytest
from pages.login_page import LoginPage

BASE_URL = "http://localhost:3000"

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    driver.get(BASE_URL)
    login_page.enter_username("validuser")
    login_page.enter_password("validpass")
    login_page.click_login()

    assert 'dental booking system' in driver.title.lower() or 'dental booking system' in driver.page_source.lower()


def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    driver.get(BASE_URL)
    login_page.enter_username("validuser")
    login_page.enter_password("wrongpass")
    login_page.click_login()

    error_msg = login_page.get_error_message()
    assert "invalid" in error_msg or "wrong" in error_msg


def test_login_empty_fields(setup):
    driver = setup
    login_page = LoginPage(driver)

    driver.get(BASE_URL)

    # إزالة required من الحقول حتى نقدر نرسل الطلب
    driver.execute_script("document.getElementById('login-username').removeAttribute('required')")
    driver.execute_script("document.getElementById('login-password').removeAttribute('required')")

    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()

    error_msg = login_page.get_error_message()
    assert "required" in error_msg or "empty" in error_msg or "invalid" in error_msg
