import json
import allure
from utils.data_loader import load_booking_data

@allure.feature("Form")
@allure.story("Validation")
def test_form_empty_validation(page):
    data = load_booking_data()
    page.goto(data["url"])

    with allure.step("Submit empty form"):
        page.click('button[type="submit"]')

    with allure.step("Check validation error"):
        assert page.locator("text=required").is_visible()