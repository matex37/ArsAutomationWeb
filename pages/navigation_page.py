import allure


class NavigationPage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def is_loaded(self):
        return self.page.locator("header").is_visible()

    def get_title(self):
        return self.page.title()

    def click_services(self):
        self.page.locator("nav a.nav-link[href='/our-services/']").click()
        self.page.wait_for_load_state("networkidle")

    def click_contact(self):
        self.page.get_by_role("link", name="Contact").click()
        self.page.wait_for_load_state("networkidle")

    def click_blog(self):
        blog_link = self.page.get_by_role("link", name="Blog")
        blog_link.scroll_into_view_if_needed()
        blog_link.click()
        self.page.wait_for_load_state("load")

    def click_logo(self):
        self.page.locator("img[alt*='logo'], .logo").first.click()
        self.page.wait_for_load_state("networkidle")

    def get_url(self):
        return self.page.url