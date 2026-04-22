import json
import allure

# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)

@allure.feature("Internal links")
@allure.story("Test check internal links navigation")
def test_internal_links_navigation(page):
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