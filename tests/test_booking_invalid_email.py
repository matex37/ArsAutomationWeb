import allure
from playwright.sync_api import expect
from datetime import datetime, timedelta
from utils.data_loader import load_booking_data


@allure.feature("Booking invalid email")
@allure.story("Booking with invalid email")
def test_booking_invalid_email(page):

    data = load_booking_data()

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
    frame.get_by_label("Month").select_option(month_index)

    #  Выбрать день
    frame.get_by_label(day_label).click()

    # Подтвердить и идти дальше
    frame.get_by_text("Next").click()

    # ===== CUSTOMER =====
    customer = data["customer"]

    frame.locator("input[name='customer-first']").fill(customer["first"])
    frame.locator("input[name='customer-last']").fill(customer["last"])
    frame.locator("input[name='customer-email']").fill(customer["wrong_email"])
    frame.locator("input[name='customer-address']").fill(customer["address"])
    frame.locator("input[name='customer-city']").fill(customer["city"])
    frame.get_by_role("combobox").select_option(customer["state"])
    frame.locator("input[name='customer-phone1']").fill(customer["phone"])

    email = (customer["wrong_email"])
    print(" Wrong email is:", email)

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
def get_future_workday(days_ahead=3):
    current = datetime.today()

    added_days = 0
    while added_days < days_ahead:
        current += timedelta(days=1)

        # 0=Monday ... 6=Sunday
        if current.weekday() < 5:  # рабочий день
            added_days += 1

    return current

target_date = get_future_workday(3)
print("Selected date:", target_date.strftime("%B %d,"))


month_index = str(target_date.month - 1)  # Playwright select
day_label = target_date.strftime("%B ") + str(target_date.day) + ","