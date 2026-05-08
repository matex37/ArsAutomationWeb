import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized", "--force-device-scale-factor=1"]
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page", None)

    if not page:
        return

    try:
        if not page.is_closed():

            screenshot = page.screenshot(full_page=True)

            allure.attach(
                screenshot,
                name="FAILED SCREEN",
                attachment_type=allure.attachment_type.PNG
            )

    except Exception:
        # NEVER break pytest execution
        pass