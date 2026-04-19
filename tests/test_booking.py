import allure
from playwright.sync_api import expect

@allure.feature("Booking")
@allure.story("Submit booking form")
def test_booking_form(page):
    page.goto("https://appliancesrepairservice.ca/")

    # открыть форму
    page.get_by_role("link", name="Book Online").click()

    # 👉 СКРОЛЛ
    page.mouse.wheel(0, 250)
    page.wait_for_timeout(2000)

    # 👉 ДОБАВИЛИ КЛИК (по области формы)
    frame = page.frame_locator("#main iframe")
    frame.get_by_text("Standard").click()

    # ещё немного подождать загрузку формы
    page.wait_for_timeout(3000)

    # postal code
    postal = frame.locator("#customer-zip_postal")
    postal.wait_for(timeout=15000)

    postal.click()
    postal.fill("L6A 5A4")

    frame.get_by_text("Next").click()

    # выбрать дату
    date_input = frame.get_by_role("textbox", name="Click to select")
    date_input.click()

    # выбрать любую дату (как откроется календарь)
    frame.get_by_role("img").first.click()

    frame.get_by_text("Next").click()

    # Открыть выбор даты
    date_input = frame.get_by_role("textbox", name="Click to select")
    date_input.click()

    # (опционально) переключить месяц
    frame.get_by_label("Month").select_option("4")

    #  Выбрать день
    frame.get_by_label("May 1,").click()

    # Подтвердить и идти дальше
    frame.get_by_text("Next").click()

    # STEP 3 — Customer info
    frame.locator("input[name='customer-first']").fill("Test")
    frame.locator("input[name='customer-last']").fill("Test")
    frame.locator("input[name='customer-email']").fill("test@gmail.com")
    frame.locator("input[name='customer-address']").fill("25 ilan Ramon")
    frame.locator("input[name='customer-city']").fill("Maple")
    frame.get_by_role("combobox").select_option("ON")
    frame.locator("input[name='customer-phone1']").fill("(438) 246-9560")

    frame.get_by_text("Next").click()

    # STEP 4 — Appliance info
    frame.locator("select[name='machine-make']").select_option("LG")
    frame.locator("select[name='machine-type']").select_option("BUILT IN STOVE")
    frame.locator("input[name='machine-model_number']").fill("45678946654")
    frame.locator("input[name='machine-serial_number']").fill("78945651546")
    frame.locator("select[name='machine-dealer']").select_option("COSCTO")

    # purchase date
    purchase_date = frame.get_by_role("textbox", name="Click to select")
    purchase_date.click()

    frame.get_by_label("Month").select_option("0")
    frame.get_by_label("January 7,").click()

    # problem description
    frame.locator("textarea[name='machine-problem_description']").fill("test description problem")

    frame.get_by_text("Next").click()

    expect(frame.get_by_text("How will you pay for this appointment?")).to_be_visible()
    expect(frame.get_by_text("Cash")).to_be_visible()
    expect(frame.get_by_text("Check")).to_be_visible()
    expect(frame.get_by_text("Credit/Debit")).to_be_visible()

