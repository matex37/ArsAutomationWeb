import json
import allure

# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)

@allure.feature("Home_page")
@allure.story("Home page load")
def test_homepage_load(page):
    page.goto(data["url"])

    assert "Appliance" in page.title()