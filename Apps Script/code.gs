function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu("Add Thumbnails")
    .addItem("Insert Image", "showSidebar")
    .addToUi();
}

function showSidebar() {
  var html =
    HtmlService.createHtmlOutputFromFile("Sidebar").setTitle("Insert Image");
  SpreadsheetApp.getUi().showSidebar(html);
}

function uploadImageToDrive(imageBase64, fileName) {
  var folderId = "1nxcsC4_u_SYOgkaw2K1h4yNxFBAAV0--"; // Replace with your Google Drive folder ID
  var folder = DriveApp.getFolderById(folderId);

  // Create a blob from the base64 string
  var blob = Utilities.newBlob(
    Utilities.base64Decode(imageBase64),
    "image/png",
    fileName
  );

  // Upload the image to the specified Google Drive folder
  var file = folder.createFile(blob);
  file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);

  // Get the URL of the uploaded image
  var fileId = file.getId();
  var fileUrl = "https://drive.google.com/uc?export=view&id=" + fileId;

  // Find the cell in Column A that matches the fileName
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getRange("A:A").getValues();

  // Loop through Column A to find the matching fileName
  for (var i = 0; i < data.length; i++) {
    if (data[i][0] === fileName) {
      // If match found, insert the formula in Column E of the same row
      sheet.getRange(i + 1, 6).setFormula('=IMAGE("' + fileUrl + '")');
      return; // Exit after inserting the formula
    }
  }

  // If no match found
  SpreadsheetApp.getUi().alert(
    "No matching cell found in Column A for the file name: " + fileName
  );
}

function fetchNamesFromSheet() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getRange("A:A").getValues();
  var names = data.flat().filter((name) => name); // Filter out empty values
  return names;
}
