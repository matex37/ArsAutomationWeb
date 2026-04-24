import json
import allure
from utils.data_loader import load_booking_data

@allure.feature("Internal links")
@allure.story("Test check internal links navigation")
def test_internal_links_navigation(page):
    data = load_booking_data()

    page.goto(data["url"])

    links = page.locator("a[href^='/']")
    count = links.count()

    for i in range(min(count, 5)):  # ограничим 5 ссылками
        link = links.nth(i)

        href = link.get_attribute("href")
        if not href:
            continue

        link.click()
        page.wait_for_load_state()

        assert page.url != ""

        page.go_back()