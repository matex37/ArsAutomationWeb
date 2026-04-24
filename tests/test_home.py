import json
import allure
from utils.data_loader import load_booking_data

@allure.feature("Home_page")
@allure.story("Home page load")
def test_homepage_load(page):
    data = load_booking_data()
    page.goto(data["url"])

    assert "Appliance" in page.title()