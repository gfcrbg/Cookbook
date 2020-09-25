/*
Will clear designated cells on button click.
*/

function inputClear() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var range = sheet.getRange("A1:A28");
  range.clear({formatOnly: false, contentsOnly: true});
}
