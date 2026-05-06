import allure
from datetime import datetime, timedelta
from pages.booking_page import BookingPage
from utils.data_loader import load_booking_data


def get_future_workday(days_ahead=3):
    current = datetime.today()
    added_days = 0

    while added_days < days_ahead:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added_days += 1

    return current

@allure.feature("Booking")
@allure.story("New booking starts clean (session reset)")
def test_booking_form(page):

    data = load_booking_data()
    booking = BookingPage(page)

    # дата
    target_date = get_future_workday(3)
    month_index = str(target_date.month - 1)
    day_label = target_date.strftime("%B ") + str(target_date.day) + ","

    with allure.step("Open booking page"):
        booking.open(data["url"])
        booking.open_booking()

    with allure.step("Filling Postal Code"):
        booking.select_service()
        booking.fill_postal(data["postal_code"])


    with allure.step("Reload page to reset session"):
        page.goto(data["url"])  # или page.reload()
        booking.open_booking()

        booking.screenshot("After reload")

    with allure.step("Verify postal is empty"):
        booking.select_service()

        postal_after = booking.frame.locator("#customer-zip_postal").input_value()

        booking.screenshot("Postal after reset")

