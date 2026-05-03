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

@allure.feature("Booking data")
@allure.story("Booking back preserves data")
def test_booking_back_preserves_data(page):

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

    with allure.step("Fill customer data"):
        customer = data["customer"]

        booking.fill_customer(customer)

        # 👉 сохраняем значения ДО возврата
        first_before = booking.frame.locator("input[name='customer-first']").input_value()
        email_before = booking.frame.locator("input[name='customer-email']").input_value()

        allure.attach(page.screenshot(), name="Before Back", attachment_type=allure.attachment_type.PNG)

    with allure.step("Go back and forward again"):
        booking.click_back()
        booking.click_next()

    with allure.step("Verify data is preserved"):
        first_after = booking.frame.locator("input[name='customer-first']").input_value()
        email_after = booking.frame.locator("input[name='customer-email']").input_value()

        assert first_before == first_after
        assert email_before == email_after

        allure.attach(page.screenshot(), name="After Back", attachment_type=allure.attachment_type.PNG)