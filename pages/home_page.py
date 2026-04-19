from pages.base_page import BasePage

class HomePage(BasePage):

    def open_home(self):
        self.open("https://appliancesrepairservice.ca/")

    def go_to_contact(self):
        self.page.click("text=Contact")