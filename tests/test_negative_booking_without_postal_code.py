import json
import allure
from utils.data_loader import load_booking_data
from playwright.sync_api import expect
import pytest
from playwright.sync_api import Error

@allure.feature("Negative test")
@allure.story("Submit without postal code")

def test_booking_without_postal(page):
    data = load_booking_data()
    page.goto(data["url"])

    page.get_by_role("link", name="Book Online").click()

    page.mouse.wheel(0, 250)
    page.wait_for_timeout(2000)

    frame = page.frame_locator("#main iframe")
    frame.get_by_text("Standard").click()

    page.wait_for_timeout(3000)

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