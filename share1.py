import os
import re

input_folder = "/Users/aarnavgupta/Desktop/shares/April"
output_file = "/Users/aarnavgupta/Desktop/shares/April/merged_output.html"

# Natural numeric sorting (so 10.html comes after 2.html)
def natural_key(filename):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', filename)]

# Get only html files (not zip)
html_files = [f for f in os.listdir(input_folder)
              if f.lower().endswith(('.html', '.htm'))]

# Sort numerically
html_files.sort(key=natural_key)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for filename in html_files:
        file_path = os.path.join(input_folder, filename)
        print(f"Merging: {filename}")

        with open(file_path, 'r', encoding='utf-8') as infile:
            outfile.write(f"\n<!-- {filename} -->\n")
            outfile.write(infile.read())

print("\nMerging completed successfully!")