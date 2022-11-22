/*
Will clear designated cells on button click.
*/

function clear() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var range = sheet.getRange(" "); // enter cell range
  range.clear({formatOnly: false, contentsOnly: true});
}
