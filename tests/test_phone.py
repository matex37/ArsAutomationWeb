import json
import allure
from utils.data_loader import load_booking_data
from playwright.sync_api import expect
from datetime import datetime, timedelta

@allure.feature("Contact")
@allure.story("Phone link")
def test_phone_clickable(page):
    data = load_booking_data()
    page.goto(data["url"])

    with allure.step("Find phone link"):
        phone = page.locator('a[href^="tel:"]')

    with allure.step("Check phone is visible"):
        assert phone.is_visible()