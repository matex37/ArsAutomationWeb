from pages.home_page import HomePage
from utils.logger import get_logger

log = get_logger()

def test_home(page):
    log.info("Opening home page")

    home = HomePage(page)
    home.open_home()

    log.info("Checking title")
    assert "Repair" in page.title()