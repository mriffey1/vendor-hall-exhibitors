import pytest
from unittest.mock import patch, MagicMock
import os
from vendor_hall import process_pdf

# Mock environment variables
@patch.dict(os.environ, {
    'SERVICE_ACCOUNT_GOOGLE': 'tests/mock_credentials/mock_service_account.json',
    'MAIN_FOLDER_PATH': '/mock/folder/path',
    'GOOGLE_WORKBOOK': 'https://mock-url-for-google-workbook',
    'MAP_DIRECTORY_NAME': 'mock_map_directory'
})
@patch('gspread.authorize')
@patch('pymupdf.open')
def test_process_pdf(mock_pymupdf_open, mock_gspread_authorize):
    # Mock the PDF document
    mock_document = MagicMock()
    mock_document.page_count = 1
    mock_page = MagicMock()
    mock_page.get_text.return_value = "Vendor One........123, 456"
    mock_document.load_page.return_value = mock_page
    mock_pymupdf_open.return_value = mock_document

    # Mock Google Sheets worksheet
    mock_worksheet = MagicMock()

    # Mock spreadsheet client and worksheet
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.add_worksheet.return_value = mock_worksheet
    mock_spreadsheet.worksheet.return_value = mock_worksheet
    mock_gspread_authorize.return_value.open_by_url.return_value = mock_spreadsheet

    # Call the function to test
    process_pdf('mock.pdf')

    # Assertions
    mock_pymupdf_open.assert_called_once_with('/mock/folder/path/mock_map_directory/mock.pdf')
    assert mock_spreadsheet.add_worksheet.called or mock_spreadsheet.worksheet.called
    mock_worksheet.update.assert_called_once()
