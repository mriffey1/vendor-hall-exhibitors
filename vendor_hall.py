import pymupdf
import pandas as pd
import re
import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
service_account_creds = os.getenv("SERVICE_ACCOUNT_GOOGLE")
folder_path = os.getenv("MAIN_FOLDER_PATH")
workbook_url = os.getenv("GOOGLE_WORKBOOK")
map_path = os.path.join(folder_path, os.getenv("MAP_DIRECTORY_NAME"))


# Google Sheets API setup
def initialize_gspread():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(
        os.path.join(folder_path, service_account_creds), scopes=scope
    )
    return gspread.authorize(creds)


client = initialize_gspread()
spreadsheet = client.open_by_url(workbook_url)


def extract_vendor_booth_data(document):
    vendor_booth_data = []
    exhibit_hall_pattern = re.compile(r'(.+?)\s*\.+\s*(\d+(?:, \d+)*)')

    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text("text")
        exhibit_hall_matches = exhibit_hall_pattern.findall(text)

        for match in exhibit_hall_matches:
            vendor_name = match[0].strip()
            vendor_name = re.sub(r'\.\s*$', '', vendor_name)
            booth_number = match[1].strip()
            vendor_booth_data.append([vendor_name, booth_number])

    return pd.DataFrame(vendor_booth_data, columns=["Vendor/Sponsor", "Booth/Location"])


def update_google_sheet(worksheet, df):
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


def process_pdf(pdf_filename):
    pdf_path = os.path.join(map_path, pdf_filename)
    document = pymupdf.open(pdf_path)
    df = extract_vendor_booth_data(document)

    worksheet_title = pdf_filename.split('.')[0]
    try:
        worksheet = spreadsheet.add_worksheet(title=worksheet_title, rows=df.shape[0] + 1, cols=df.shape[1])
    except gspread.exceptions.APIError:
        print(f"Worksheet '{worksheet_title}' already exists, updating existing sheet.")
        worksheet = spreadsheet.worksheet(worksheet_title)
        worksheet.clear()

    update_google_sheet(worksheet, df)
    print(f"Data from '{pdf_filename}' successfully extracted and saved to Google Sheet tab '{worksheet_title}'")


def main():
    for pdf_filename in os.listdir(map_path):
        if pdf_filename.endswith('.pdf'):
            process_pdf(pdf_filename)


if __name__ == "__main__":
    main()
