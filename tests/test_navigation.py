import json
import allure
from utils.data_loader import load_booking_data

@allure.feature("Navigation")
@allure.story("Test navigation pages")
def test_homepage_load(page):
    data = load_booking_data()
    page.goto(data["url"])

    assert page.title() != ""
    assert page.locator("header").is_visible()


def test_navigation_menu_services(page):
    data = load_booking_data()
    page.goto(data["url"])

    page.click("text=Services")
    page.wait_for_load_state("networkidle")

    assert "service" in page.url.lower()


def test_navigation_contact_us(page):
    data = load_booking_data()
    page.goto(data["url"])

    page.click("text=Contact")
    page.wait_for_load_state("networkidle")

    assert "contact" in page.url.lower()


def test_navigation_blog(page):
    data = load_booking_data()
    page.goto(data["url"])

    blog_link = page.get_by_role("link", name="Blog")

    blog_link.scroll_into_view_if_needed()
    blog_link.click()

    page.wait_for_load_state("load")

    assert "blog" in page.url.lower()


def test_logo_redirect_home(page):
    data = load_booking_data()
    page.goto(data["url"])

    page.click("img[alt*='logo'], .logo")
    page.wait_for_load_state("networkidle")

