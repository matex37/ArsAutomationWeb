import pytest
from playwright.sync_api import sync_playwright
from config import HEADLESS

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        page = browser.new_page()
        yield page
        browser.close()