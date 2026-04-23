import json
import allure
from playwright.sync_api import expect
from datetime import datetime, timedelta

# загрузка данных
with open("booking_data.json", "r") as f:
    data = json.load(f)

@allure.feature("Booking")
@allure.story("Submit booking form")
def test_booking_form(page):

    page.goto(data["url"])

    page.get_by_role("link", name="Book Online").click()

    page.mouse.wheel(0, 250)
    page.wait_for_timeout(2000)

    frame = page.frame_locator("#main iframe")
    frame.get_by_text("Standard").click()

    page.wait_for_timeout(3000)

    # postal
    postal = frame.locator("#customer-zip_postal")
    postal.wait_for(timeout=15000)
    postal.fill(data["postal_code"])

    frame.get_by_text("Next").click()

    # выбрать дату
    date_input = frame.get_by_role("textbox", name="Click to select")
    date_input.click()

    # выбрать любую дату (как откроется календарь)
    frame.get_by_role("img").first.click()

    frame.get_by_text("Next").click()

    # Открыть выбор даты
    date_input = frame.get_by_role("textbox", name="Click to select")
    date_input.click()

    # (опционально) переключить месяц
    frame.get_by_label("Month").select_option(data["dates"]["month_index"])

    #  Выбрать день
    frame.get_by_label(data["dates"]["day_label"]).click()

    # Подтвердить и идти дальше
    frame.get_by_text("Next").click()

    # ===== CUSTOMER =====
    customer = data["customer"]

    frame.locator("input[name='customer-first']").fill(customer["first"])
    frame.locator("input[name='customer-last']").fill(customer["last"])
    frame.locator("input[name='customer-email']").fill(customer["email"])
    frame.locator("input[name='customer-address']").fill(customer["address"])
    frame.locator("input[name='customer-city']").fill(customer["city"])
    frame.get_by_role("combobox").select_option(customer["state"])
    frame.locator("input[name='customer-phone1']").fill(customer["phone"])

    frame.get_by_text("Next").click()

    # ===== APPLIANCE =====
    appliance = data["appliance"]

    frame.locator("select[name='machine-make']").select_option(appliance["make"])
    frame.locator("select[name='machine-type']").select_option(appliance["type"])
    frame.locator("input[name='machine-model_number']").fill(appliance["model"])
    frame.locator("input[name='machine-serial_number']").fill(appliance["serial"])
    frame.locator("select[name='machine-dealer']").select_option(appliance["dealer"])

    # purchase date
    purchase_date = frame.get_by_role("textbox", name="Click to select")
    purchase_date.click()

    frame.get_by_label("Month").select_option(data["dates"]["purchase_month_index"])
    frame.get_by_label(data["dates"]["purchase_day"]).click()

    frame.locator("textarea[name='machine-problem_description']").fill(
        appliance["problem"]
    )

    frame.get_by_text("Next").click()

    # ASSERTS
    expect(frame.get_by_text("How will you pay for this appointment?")).to_be_visible()
    expect(frame.get_by_text("Cash")).to_be_visible()
    expect(frame.get_by_text("Check")).to_be_visible()
    expect(frame.get_by_text("Credit/Debit")).to_be_visible()

    frame.get_by_text("Cash").click(force=True)

    # дошли до финального шага
    expect(frame.get_by_text("Let's review.")).to_be_visible()


def get_target_date(days_ahead):
    return datetime.today() + timedelta(days=days_ahead)

