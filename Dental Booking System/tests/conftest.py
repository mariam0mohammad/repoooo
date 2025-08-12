import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:3000"  # غيّريه إذا السيرفر على بورت ثاني

@pytest.fixture
def setup():
    # تشغيل متصفح Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
