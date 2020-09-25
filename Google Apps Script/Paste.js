// copy data from sheet A and paste to sheet B

function paste() {
  var ss=SpreadsheetApp.getActive();
  var sh1=ss.getSheetByName(" "); // enter the name of the sheet
  var sh2=ss.getSheetByName(" "); // enther the name of the sheet
// Shopped Month, Date, Survey Question, Issue, Issue #, Sassie ID, Store Location, Submitter, Concern
  sh1.getRange("A40:S40").copyTo(sh1.getRange("A42:S42"), {contentsOnly:true});
  sh1.getRange("T40:W40").copyTo(sh1.getRange("T42:W42"), {contentsOnly:false});
  sh1.getRange("A42:W42").copyTo(sh2.getRange(sh2.getLastRow()+1,1,1,1), SpreadsheetApp.CopyPasteType.PASTE_NORMAL);
}
