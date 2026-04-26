import allure
from playwright.sync_api import expect
from datetime import datetime, timedelta
from utils.data_loader import load_booking_data


def get_future_workday(days_ahead=3):
    current = datetime.today()
    added_days = 0

    while added_days < days_ahead:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added_days += 1

    return current

@allure.feature("Booking invalid phone")
@allure.story("Booking with invalid phone number")
def test_booking_invalid_phone(page):
    data = load_booking_data()

    # ===== DATE (внутри теста!) =====
    target_date = get_future_workday(3)
    month_index = str(target_date.month - 1)
    day_label = target_date.strftime("%B ") + str(target_date.day) + ","

    with allure.step("Open homepage"):
        page.goto(data["url"])

    with allure.step("Open booking form"):
        page.get_by_role("link", name="Book Online").click()

    # скролл
    page.mouse.wheel(0, 250)

    # ждать iframe
    page.wait_for_selector("#main iframe", timeout=15000)
    frame = page.frame_locator("#main iframe")

    # ===== STEP 1 =====
    with allure.step("Select service + postal"):
        frame.get_by_text("Standard").click()

        postal = frame.locator("#customer-zip_postal")
        postal.wait_for()
        postal.fill(data["postal_code"])

        allure.attach(page.screenshot(), name="Postal code", attachment_type=allure.attachment_type.PNG)

        frame.get_by_text("Next").click()

    # ===== STEP 2 =====
    with allure.step("Select booking date"):
        date_input = frame.get_by_role("textbox", name="Click to select")

        date_input.click()

        frame.get_by_label("Month").select_option(month_index)
        frame.get_by_label(day_label).click()

        frame.get_by_text("Next").click()

    # ===== STEP 3 =====
    with allure.step("Fill customer info"):
        c = data["customer"]

        frame.locator("input[name='customer-first']").fill(c["first"])
        frame.locator("input[name='customer-last']").fill(c["last"])
        frame.locator("input[name='customer-email']").fill(c["email"])
        frame.locator("input[name='customer-address']").fill(c["address"])
        frame.locator("input[name='customer-city']").fill(c["city"])
        frame.get_by_role("combobox").select_option(c["state"])
        frame.locator("input[name='customer-phone1']").fill(c["wrong_phone"])

        allure.attach(page.screenshot(), "Customer", allure.attachment_type.PNG)

        frame.get_by_text("Next").click()

    phone = (c["wrong_phone"])
    print(" Wrong phone is:", phone)

    frame.get_by_text("Next").click()
    next_btn = frame.get_by_text("Next")

    # проверяем CSS состояние
    class_attr = next_btn.get_attribute("class") or ""
    aria_disabled = next_btn.get_attribute("aria-disabled")
    pointer_events = next_btn.evaluate("el => getComputedStyle(el).pointerEvents")

    assert (
            "disabled" in class_attr.lower()
            or aria_disabled == "true"
            or pointer_events == "none"
    )
