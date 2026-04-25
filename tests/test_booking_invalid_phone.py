import allure
from playwright.sync_api import expect
from datetime import datetime, timedelta
from utils.data_loader import load_booking_data


@allure.feature("Booking invalid phone")
@allure.story("Booking with invalid phone number")
def test_booking_invalid_phone(page):

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
    frame.locator("input[name='customer-phone1']").fill(customer["wrong_phone"])
    phone = (customer["wrong_phone"])
    print(" Wrong number is:", phone)


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
