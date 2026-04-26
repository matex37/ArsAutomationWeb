import allure
from pages.navigation_page import NavigationPage
from utils.data_loader import load_booking_data


@allure.feature("Navigation")
@allure.story("Homepage loads")
def test_homepage_load(page):
    data = load_booking_data()
    nav = NavigationPage(page)

    with allure.step("Open homepage"):
        nav.open(data["url"])

    with allure.step("Verify homepage loaded"):
        assert nav.get_title() != ""
        assert nav.is_loaded()


@allure.feature("Navigation")
@allure.story("Navigate to Services")
def test_navigation_menu_services(page):
    data = load_booking_data()
    nav = NavigationPage(page)

    nav.open(data["url"])

    with allure.step("Our Services"):
        nav.click_services()

    from urllib.parse import urlparse

    path = urlparse(nav.get_url()).path
    assert path == "/our-services/"

@allure.feature("Navigation")
@allure.story("Navigate to Contact")
def test_navigation_contact_us(page):
    data = load_booking_data()
    nav = NavigationPage(page)

    nav.open(data["url"])

    with allure.step("Click Contact"):
        nav.click_contact()

    with allure.step("Verify URL"):
        assert "contact" in nav.get_url().lower()


@allure.feature("Navigation")
@allure.story("Navigate to Blog")
def test_navigation_blog(page):
    data = load_booking_data()
    nav = NavigationPage(page)

    nav.open(data["url"])

    with allure.step("Click Blog"):
        nav.click_blog()

    with allure.step("Verify URL"):
        assert "blog" in nav.get_url().lower()


@allure.feature("Navigation")
@allure.story("Logo redirects to homepage")
def test_logo_redirect_home(page):
    data = load_booking_data()
    nav = NavigationPage(page)

    nav.open(data["url"])

    with allure.step("Click logo"):
        nav.click_logo()

    with allure.step("Verify homepage URL"):
        assert nav.get_url().rstrip("/") == data["url"].rstrip("/")