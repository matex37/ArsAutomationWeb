import pytest
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


data = load_booking_data()

service_types = data["service_types"]


@pytest.mark.parametrize("service_type", service_types)
@allure.feature("Booking")
@allure.story("Booking flow for all service types")
def test_booking_all_services(page, service_type):

    booking = BookingPage(page)

    target_date = get_future_workday(3)

    month_index = str(target_date.month - 1)

    day_label = target_date.strftime("%B ") + str(target_date.day) + ","

    # ===== OPEN =====

    booking.open(data["url"])

    booking.open_booking()

    # ===== STEP 1 =====
    # SELECT SERVICE FIRST

    booking.select_service(service_type)

    # ===== STEP 2 =====
    # POSTAL CODE

    booking.fill_postal(data["postal_code"])

    booking.click_next()

    # ===== STEP 3 =====
    # DATE

    booking.select_booking_date(
        month_index,
        day_label
    )

    booking.click_next()

    # ===== STEP 4 =====
    # CUSTOMER

    booking.fill_customer(data["customer"])

    booking.click_next()

    # ===== STEP 5 =====
    # APPLIANCE

    booking.fill_appliance(
        data["appliance"],
        data["dates"]
    )

    booking.click_next()

    # ===== DIFFERENT FLOWS =====

    if service_type == "Standard":

        booking.verify_payment()

        booking.select_cash()

        booking.verify_review()

    elif service_type == "Manufacturer Warranty":

        booking.verify_review()

    elif service_type == "Extended Warranty":

        booking.fill_extended_warranty_info(
            data["extended_warranty"]
        )
        booking.click_next()

        booking.verify_review()

    elif service_type == "Third-Party":

        booking.fill_third_party_payer(
            data["third_party"]["payer"]
        )

        booking.click_next()

        booking.verify_review()