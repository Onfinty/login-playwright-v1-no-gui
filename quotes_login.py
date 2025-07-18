from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/login")

    #! The login filler
    page.locator("#username").fill("Onfinty")
    page.locator("#password").fill("onfinty@123")
    page.locator('input[type="submit"]').click()

    #! The quotes page..
    while True:
        quotes = page.locator("div.quote")

        count = quotes.count()
        for i in range(count):
            quote_text = quotes.nth(i).locator("span.text").inner_text()
            author = quotes.nth(i).locator("small.author").inner_text()

            with open("quotes.txt","a",encoding="UTF-8") as file:

                file.write(f"{quote_text} - {author}\n")

        next_button = page.locator("li.next a")

        if not next_button.is_visible():
            print("There are no longer pages")
            break
        next_button.click()
        page.wait_for_timeout(1000)

    page.wait_for_timeout(30000)
