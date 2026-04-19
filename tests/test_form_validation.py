import allure

@allure.feature("Form")
@allure.story("Validation")
def test_form_empty_validation(page):
    page.goto("https://appliancesrepairservice.ca/")

    with allure.step("Submit empty form"):
        page.click('button[type="submit"]')

    with allure.step("Check validation error"):
        assert page.locator("text=required").is_visible()