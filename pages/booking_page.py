from playwright.sync_api import expect
import allure

class BookingPage:

    def __init__(self, page):
        self.page = page
        self.frame = page.frame_locator("#main iframe")

    # ===== OPEN =====
    def open(self, url):
        self.page.goto(url)

    def open_booking(self):
        self.page.get_by_role("link", name="Book Online").click()
        self.screenshot("Booking page")
        self.page.mouse.wheel(0, 250)
        self.page.wait_for_selector("#main iframe")

    # ===== STEP 1 =====
    def select_service(self):
        self.frame.get_by_text("Standard").click()

    def fill_postal(self, postal):
        postal_input = self.frame.locator("#customer-zip_postal")
        postal_input.wait_for()
        postal_input.fill(postal)

        self.screenshot("Postal filled")

    def click_next(self):
        self.frame.get_by_text("Next").click()

    # ===== STEP 2 =====
    def select_booking_date(self, month_index, day_label):
        date_input = self.frame.get_by_role("textbox", name="Click to select")
        date_input.click()

        self.frame.get_by_label("Month").select_option(month_index)
        self.frame.get_by_label(day_label).click()

    # ===== STEP 3 =====
    def fill_customer(self, c):
        self.frame.locator("input[name='customer-first']").fill(c["first"])
        self.frame.locator("input[name='customer-last']").fill(c["last"])
        self.frame.locator("input[name='customer-email']").fill(c["email"])
        self.frame.locator("input[name='customer-address']").fill(c["address"])
        self.frame.locator("input[name='customer-city']").fill(c["city"])
        self.frame.get_by_role("combobox").select_option(c["state"])
        self.frame.locator("input[name='customer-phone1']").fill(c["phone"])

        self.screenshot("Customer data filled")

    # ===== STEP 4 =====
    def fill_appliance(self, a, dates):
        self.frame.locator("select[name='machine-make']").select_option(a["make"])
        self.frame.locator("select[name='machine-type']").select_option(a["type"])
        self.frame.locator("input[name='machine-model_number']").fill(a["model"])
        self.frame.locator("input[name='machine-serial_number']").fill(a["serial"])
        self.frame.locator("select[name='machine-dealer']").select_option(a["dealer"])

        self.screenshot("Appliance information filled")

        purchase = self.frame.get_by_role("textbox", name="Click to select")
        purchase.click()

        self.frame.get_by_label("Month").select_option(dates["purchase_month_index"])
        self.frame.get_by_label(dates["purchase_day"]).click()

        self.frame.locator("textarea[name='machine-problem_description']").fill(
            a["problem"]
        )

    # ===== STEP 5 =====
    def verify_payment(self):
        expect(self.frame.get_by_text("How will you pay for this appointment?")).to_be_visible()

        self.screenshot("How will you pay")

    def select_cash(self):
        self.frame.get_by_text("Cash").click(force=True)

    def verify_review(self):
        expect(self.frame.get_by_text("Let's review.")).to_be_visible()

        self.screenshot("Final screen")

    # ===== Screenshot =====#
    def screenshot(self, name):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def click_next(self):
        self.frame.get_by_text("Next").click()

    # проверяем CSS состояние
    def is_next_disabled(self):
        next_btn = self.frame.get_by_text("Next")

        class_attr = next_btn.get_attribute("class") or ""
        aria_disabled = next_btn.get_attribute("aria-disabled")
        pointer_events = next_btn.evaluate("el => getComputedStyle(el).pointerEvents")

        import allure
        allure.attach(
            f"class={class_attr}\naria-disabled={aria_disabled}\npointer-events={pointer_events}",
            name="Next button state"
        )

        return (
                "disabled" in class_attr.lower()
                or aria_disabled == "true"
                or pointer_events == "none"
        )