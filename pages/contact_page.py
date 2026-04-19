from pages.base_page import BasePage

class ContactPage(BasePage):

    def is_open(self):
        return "contact" in self.page.url.lower()