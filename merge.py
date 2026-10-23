from PyPDF2 import PdfMerger
from pathlib import Path
import re

input_folder = Path("/Users/aarnavgupta/Desktop/Share Code")
output_file = input_folder / "merged.pdf"

merger = PdfMerger()

# Get all PDFs except the output file
pdf_files = [
    pdf for pdf in input_folder.glob("*.pdf")
    if pdf.name != "merged.pdf"
]

# Sort naturally: 1, 2, 3, ..., 10, 11
pdf_files.sort(
    key=lambda x: [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r'(\d+)', x.name)
    ]
)

print("PDFs will be merged in this order:")

for i, pdf in enumerate(pdf_files, 1):
    print(f"{i}. {pdf.name}")
    merger.append(str(pdf))

merger.write(str(output_file))
merger.close()

print(f"\nMerged {len(pdf_files)} PDFs into:")
print(output_file)