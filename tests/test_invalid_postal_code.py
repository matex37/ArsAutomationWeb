import allure
from datetime import datetime, timedelta
from pages.booking_page import BookingPage
from utils.data_loader import load_booking_data
from playwright.sync_api import expect



def get_future_workday(days_ahead=3):
    current = datetime.today()
    added_days = 0

    while added_days < days_ahead:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added_days += 1

    return current

@allure.feature("Booking")
@allure.story("Postal Code Validation")
def test_invalid_postal_not_ontario(page):

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
        booking.fill_postal(data["wrong_postal_code"])
        booking.click_next()
        page.wait_for_load_state("networkidle")
        frame = booking.frame
    with allure.step("Verify service area error message"):
        frame.locator("text=we do not yet serve your area").wait_for(state="visible")
        booking.screenshot("Error in iframe")


