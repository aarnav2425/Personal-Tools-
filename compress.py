import fitz  # PyMuPDF

input_pdf = "/Users/aarnavgupta/Desktop/shares/April/1.pdf"
output_pdf = "/Users/aarnavgupta/Desktop/shares/April/1_under5mb.pdf"

doc = fitz.open(input_pdf)
new_doc = fitz.open()

for page in doc:
    # 🔥 Render page at 150 DPI instead of 300+
    pix = page.get_pixmap(dpi=150)
    
    # Convert page to compressed JPEG
    img_bytes = pix.tobytes("jpeg")
    
    # Create new page
    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
    
    # Insert compressed image
    new_page.insert_image(page.rect, stream=img_bytes)

new_doc.save(
    output_pdf,
    garbage=4,
    deflate=True,
    clean=True
)

doc.close()
new_doc.close()

print("✅ PDF reduced successfully!")