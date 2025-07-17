from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")


    username = input("Enter your Username please: ").strip().lower()
    password = input("Enter your Password: ").strip()

    
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator('button[type="submit"]').click()

    
    page.wait_for_selector("#flash")
    flash = page.locator("#flash").inner_text().split("×")[0].strip()

    
    if "Your username is invalid!" in flash:
        print("❌ Invalid Username or Password. Try again later.")
    elif "You logged into a secure area!" in flash:
        subheader = page.locator(".subheader").inner_text().strip()
        print("✅", subheader)

        
        logout = input("Do you want to log out? (y/n): ").strip().lower()
        if logout == "y":
            page.locator('a.button.secondary.radius').click()
            print("🚪 You logged out successfully.")
        else:
            print("🟢 Still Logged in. You can close the browser manually.")

    page.wait_for_timeout(10000)
