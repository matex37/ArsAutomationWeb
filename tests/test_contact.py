from pages.home_page import HomePage
from pages.contact_page import ContactPage

def test_go_to_contact(page):
    home = HomePage(page)
    contact = ContactPage(page)

    home.open_home()
    home.go_to_contact()

    assert contact.is_open()