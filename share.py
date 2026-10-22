import os
import zipfile
import re

input_folder = "/Users/aarnavgupta/Desktop/shares/April"
output_file = "/Users/aarnavgupta/Desktop/shares/April/merged_output.html"

# Extract date from filename
def extract_date(filename):
    match = re.search(r'_(\d{8})\.htm\.zip$', filename)
    if match:
        return match.group(1)
    return "00000000"

zip_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".zip")]

# Sort by date (YYYYMMDD)
zip_files.sort(key=extract_date)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for zip_name in zip_files:
        zip_path = os.path.join(input_folder, zip_name)
        print(f"\nProcessing ZIP: {zip_name}")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                if member.lower().endswith(('.htm', '.html')):
                    print(f"  Merging: {member}")
                    content = zip_ref.read(member).decode('utf-8', errors='ignore')

                    outfile.write(f"\n<!-- {member} -->\n")
                    outfile.write(content)

print("\nMerging completed successfully!")