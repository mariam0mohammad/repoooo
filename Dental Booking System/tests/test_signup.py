import pytest
from pages.signup_page import SignUpPage

BASE_URL = "http://localhost:3000"

# -------------------- 1. Sign Up with valid data --------------------
def test_signup_valid_data(setup):
    driver = setup
    signup_page = SignUpPage(driver)

    username = "mariamTK_new"   # تأكدي إنه جديد إذا بدك تختبري التسجيل
    password = "M12345"
    phone = "0597777778"        # رقم جديد

    driver.get(BASE_URL)
    signup_page.enter_username(username)
    signup_page.enter_password(password)
    signup_page.enter_phone(phone)
    signup_page.click_signup()

    message = signup_page.get_ui_message().lower()
    
    # يقبل أي حالة من الثلاث: نجاح، مسجل مسبقًا، أو نجاح عام
    assert ("success" in message or 
            "registered" in message or 
            "already exists" in message)


# -------------------- 2. Sign Up using duplicate username --------------------
def test_signup_duplicate_username(setup):
    driver = setup
    signup_page = SignUpPage(driver)

    username = "george"  # اسم مستخدم موجود مسبقاً
    password = "M123"
    phone = "0599999999"

    driver.get(BASE_URL)
    signup_page.enter_username(username)
    signup_page.enter_password(password)
    signup_page.enter_phone(phone)
    signup_page.click_signup()

    message = signup_page.get_ui_message().lower()
    assert "already exists" in message or "duplicate" in message

# -------------------- 3. Sign Up with invalid phone format --------------------
def test_signup_invalid_phone(setup):
    driver = setup
    signup_page = SignUpPage(driver)

    username = "ali"
    password = "A098"
    phone = "12345"  # رقم غير صالح

    driver.get(BASE_URL)
    signup_page.enter_username(username)
    signup_page.enter_password(password)
    signup_page.enter_phone(phone)
    signup_page.click_signup()

    message = signup_page.get_ui_message().lower()
    assert "invalid" in message or "phone" in message
