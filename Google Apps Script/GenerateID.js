/*
Generates a random integer in a defined range in a specified cell range.
*/

function generateID() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[0];
  var cell = sheet.getRange("P20"); // enter cell range
  cell.setValue(Math.floor(Math.random() * 100));
}

