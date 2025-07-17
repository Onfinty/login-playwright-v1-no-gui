from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    url = "https://www.selenium.dev/selenium/web/web-form.html"
    page.goto(url)
    page.locator("#my-text-id").fill("Kero")
    page.get_by_text("password").fill('123456789')
    page.get_by_text("Textarea").fill('Onfinty will Have a lot of money')
    page.select_option('[name="my-select"]',"2")
    page.locator('[name="my-datalist"]').fill("New York")
    page.set_input_files('input[type="file"]',"kero.csv")
    page.locator("#my-check-2").click()
    page.locator("#my-radio-2").click()
    page.locator('input[type="color"]').fill("#ff0000")
    page.locator('input[name="my-date"]').click()
    page.locator('text="17"').click()
    page.locator("body").click()
    page.evaluate("document.querySelector('input[type=range]').value = 8")
    page.evaluate("document.querySelector('input[type=range]').dispatchEvent(new Event('input'))")
    page.locator('button[type="submit"]').click()
    submitted = page.locator('#message').text_content()
    if submitted =="Received!":
        print("Good Job, Kero... the Form submitted successfully")
        page.screenshot(path="Form submitted.png")
        browser.close()

