import allure

@allure.feature("Contact")
@allure.story("Phone link")
def test_phone_clickable(page):
    page.goto("https://appliancesrepairservice.ca/")

    with allure.step("Find phone link"):
        phone = page.locator('a[href^="tel:"]')

    with allure.step("Check phone is visible"):
        assert phone.is_visible()