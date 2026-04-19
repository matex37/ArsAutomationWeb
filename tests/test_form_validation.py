import json
import allure
# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)

@allure.feature("Form")
@allure.story("Validation")
def test_form_empty_validation(page):
    page.goto(data["url"])

    with allure.step("Submit empty form"):
        page.click('button[type="submit"]')

    with allure.step("Check validation error"):
        assert page.locator("text=required").is_visible()