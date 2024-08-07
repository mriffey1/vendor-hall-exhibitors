import fitz
import pandas as pd
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/megan/Documents/Python/sheet-img/sheet.json', scope)
client = gspread.authorize(creds)


# Open the PDF
pdf_folder_path = '/home/megan/Documents/Python/sheet-img/maps'

spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1S1xNS1MtvtlooCEpoXrjngtvKeU9zfhKbrcqYL72xyw/edit?usp=sharing')

# Loop through each PDF in the folder
for pdf_filename in os.listdir(pdf_folder_path):
    if pdf_filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder_path, pdf_filename)
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
    
    # Create a new worksheet for each PDF file
    worksheet_title = pdf_filename.split('.')[0] 
    try:
        worksheet = spreadsheet.add_worksheet(title=worksheet_title, rows=df.shape[0] + 1, cols=df.shape[1])
    except gspread.exceptions.APIError:
        print(f"Worksheet {worksheet_title} already exists, updating existing sheet.")
        worksheet = spreadsheet.worksheet(worksheet_title)
        worksheet.clear()

    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print(f"Data from {pdf_filename} successfully extracted and saved to Google Sheet tab '{worksheet_title}'")

