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
@allure.story("Negative - wrong email")
def test_invalid_email(page):
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
        booking.click_next()

    with allure.step("Choose the visit day"):
        booking.select_booking_date(month_index, day_label)
        booking.click_next()

    # 👇 КЛЮЧЕВОЕ МЕСТО
    customer = data["customer"].copy()
    customer["email"] = "abracadabra_email"  # ❌ wrong email

    with allure.step("Fill customer with wrong email"):
        booking.fill_customer(customer)

    with allure.step("Click Next"):
        booking.click_next()

    with allure.step("Verify we did NOT move forward"):
        # остаёмся на той же странице (customer step)
        assert booking.frame.locator("input[name='customer-email']").is_visible()