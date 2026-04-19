import json
import allure
from playwright.sync_api import expect
from datetime import datetime, timedelta

# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)

@allure.feature("Contact")
@allure.story("Phone link")
def test_phone_clickable(page):
    page.goto(data["url"])

    with allure.step("Find phone link"):
        phone = page.locator('a[href^="tel:"]')

    with allure.step("Check phone is visible"):
        assert phone.is_visible()