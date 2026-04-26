import allure


class NavigationPage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)
        self.stable_screenshot("open_page")


    def is_loaded(self):
        return self.page.locator("header").is_visible()

    def get_title(self):
        return self.page.title()

    def click_services(self):
        self.page.locator("nav a.nav-link[href='/our-services/']").click()
        self.page.wait_for_load_state("networkidle")
        self.stable_screenshot("click_services")

    def click_contact(self):
        self.page.get_by_role("link", name="Contact").click()
        self.page.wait_for_load_state("networkidle")
        self.stable_screenshot("click_contact")

    def click_blog(self):
        blog_link = self.page.get_by_role("link", name="Blog")
        blog_link.scroll_into_view_if_needed()
        blog_link.click()
        self.page.wait_for_load_state("load")
        self.stable_screenshot("click_blog")

    def click_logo(self):
        self.page.locator("img[alt*='logo'], .logo").first.click()
        self.page.wait_for_load_state("networkidle")
        self.stable_screenshot("click_logo")

    def get_url(self):
        return self.page.url

    def attach_screenshot(self, name):
        screenshot = self.page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def stable_screenshot(self, name):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(500)

        # подождать, пока DOM точно готов
        self.page.wait_for_function("document.readyState === 'complete'")

        allure.attach(
            self.page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )


