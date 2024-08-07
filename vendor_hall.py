import fitz  # PyMuPDF
import pandas as pd
import re

# Open the PDF
pdf_path = '/home/megan/Documents/Python/sheet-img/pages.pdf'
document = fitz.open(pdf_path)

vendor_booth_data = []

for page_num in range(document.page_count):
    page = document.load_page(page_num)
    text = page.get_text("text")

    # Define a regex pattern to match the vendor and booth number
    # The pattern looks for a vendor name followed by periods and then a booth number
    exhibit_hall_pattern = re.compile(r'(.+?)\s*\.+\s*(\d+(?:, \d+)*)')
    

    # Extract matches from the page text
    exhibit_hall_matches = exhibit_hall_pattern.findall(text)
    
    for match in exhibit_hall_matches:
        vendor_name = match[0].strip()
        trailing_period = re.sub(r'\.\s*$', '', vendor_name)
        
        booth_number = match[1].strip()
        vendor_booth_data.append([trailing_period, booth_number])

# Convert to DataFrame
df = pd.DataFrame(vendor_booth_data, columns=["Vendor/Sponsor", "Booth/Location"])

# Save to Excel
output_path = '/home/megan/Documents/Python/sheet-img/vendors_booths_and_sponsors6.xlsx'
df.to_excel(output_path, index=False)

print(f"Data successfully extracted and saved to {output_path}")
