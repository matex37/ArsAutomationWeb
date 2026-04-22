import json
import allure

# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)


def test_homepage_load(page):
    page.goto(data["url"])

    assert page.title() != ""
    assert page.locator("header").is_visible()


def test_navigation_menu_services(page):
    page.goto(data["url"])

    page.click("text=Services")
    page.wait_for_load_state("networkidle")

    assert "service" in page.url.lower()


def test_navigation_contact_us(page):
    page.goto(data["url"])

    page.click("text=Contact")
    page.wait_for_load_state("networkidle")

    assert "contact" in page.url.lower()


def test_navigation_blog(page):
    page.goto(data["url"])

    page.locator("nav >> text=Blog").first.scroll_into_view_if_needed()

    with page.expect_navigation():
        page.locator("nav >> text=Blog").first.click()


def test_logo_redirect_home(page):
    page.goto(data["url"])

    page.click("img[alt*='logo'], .logo")
    page.wait_for_load_state("networkidle")

