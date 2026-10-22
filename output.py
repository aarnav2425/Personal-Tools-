from playwright.sync_api import sync_playwright

input_file = "/Users/aarnavgupta/Desktop/shares/April/new.htm"
output_file = "/Users/aarnavgupta/Desktop/shares/April/2023_2024.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto(f"file://{input_file}")
    page.emulate_media(media="print")

    page.pdf(
        path=output_file,
        format="A4",
        margin={
            "top": "10mm",
            "bottom": "10mm",
            "left": "10mm",
            "right": "10mm"
        },
        print_background=True
    )

    browser.close()

print("✅ PDF created successfully!")