from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/scroll")

    
    for _ in range(50):  
        page.evaluate("""
            () => {
                window.scrollBy(0, window.innerHeight);
            }
        """)
        time.sleep(1)  

    
    quotes = page.locator("div.quote")
    for i in range(quotes.count()):
        text = quotes.nth(i).locator("span.text").inner_text()
        author = quotes.nth(i).locator("small.author").inner_text()
        with open("quotes.txt","a",encoding="UTF-8") as file:

            file.write(f"{text} - {author}\n")

    page.wait_for_timeout(5000)
