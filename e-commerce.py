from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

    #!---------------------!
    products = page.locator(".card.thumbnail")
    count = products.count()

    product_list = []
    hrefs = []
    all_products_data = []

    for i in range(count):
        product = products.nth(i)
        product_list.append(product)
        product_link = product.locator(".title").get_attribute("href")
        hrefs.append(product_link)
        text = product.locator(".title").get_attribute("title")
        price = product.locator('span[itemprop="price"]').inner_text()
        reviews_text = (
            product.locator(".review-count.float-end").inner_text().split("reviews")
        )
        stars = product.locator("span.ws-icon-star").count()
        prd_info = product.locator(".card-text").inner_text()
        reviews = int(reviews_text[0].strip())
        all_products_data.append(
            {"name": text, "price": price, "stars": stars, "reviews": reviews}
        )
        prd_num = i + 1
        #! The Print of the product
        print(
            f"[{prd_num}]{text}--({price})-- have {"⭐" * stars} from {reviews} users"
        )

    #! The Product INFO
    def info():
        while True:
            try:
                choice = int(
                    input(
                        "Type the product number that you want to know more about it: "
                    )
                )
                prd_info = product_list[choice - 1].locator(".card-text").inner_text()
                print(f"\n📝 Product Description: {prd_info}")
                break
            except IndexError:
                print("Sorry That procuct dose not exist")
                choice = int(
                    input(
                        f"Type the product number that you want to know more about it (FROM 1 TO {count}): "
                    )
                )
                prd_info = product_list[choice - 1].locator(".card-text").inner_text()
                print(f"\n📝 Product Description: {prd_info}")
                break

    #! The Product Link
    def link():
        choice = int(input("Type the product number that you want to get its link: "))
        selected_href = hrefs[choice - 1]
        full_link = "https://webscraper.io" + selected_href
        print(full_link)

    #! The Best Product
    def best():

        best = max(all_products_data, key=lambda p: (p["stars"], p["reviews"]))
        print(
            f"✨ {best['name']} with {best['stars']} stars and {best['reviews']} reviews – Price: {best['price']}"
        )

    def txt():
        User = input("Enter the name to that text file: ")
        path = input("Enter the path to put that text file: ")
        with open(
            f"{path}/{User}.txt",
            "a",
            encoding="UTF-8",
        ) as file:

            file.write(json.dumps(all_products_data, ensure_ascii=False, indent=4))

    print("-----------------------------Onfinty------------------------------------")
    print(
        "[1] See a product info\n[2] Product Link \n[3] See the best product\n [4] Import info as txt file"
    )
    print()
    user_input = input("What do you want to do ?? (1:4) : ")
    if user_input == "1":
        info()
    elif user_input == "2":
        link()
    elif user_input == "3":
        best()
    elif user_input == "4":
        txt()
    else:
        print("invalid choice")
