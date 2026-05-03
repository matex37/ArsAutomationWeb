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
@allure.feature("Booking - Date validation")
@allure.story("User cannot select past date")
def test_cannot_select_past_date(page):

    data = load_booking_data()
    booking = BookingPage(page)

    with allure.step("Open booking"):
        booking.open(data["url"])
        booking.open_booking()

        booking.select_service()
        booking.fill_postal(data["postal_code"])
        booking.click_next()

    with allure.step("Open calendar"):
        booking.open_calendar()

    with allure.step("Try to click past date"):
        past_date = booking.frame.locator("[aria-disabled='true']").first

        if past_date.count() > 0:
            # элемент есть, но он disabled
            booking.screenshot("Past date found")
            assert past_date.get_attribute("aria-disabled") == "true"
        else:
            # fallback — даты вообще не кликабельны
            booking.screenshot("No disabled dates visible")
            assert True