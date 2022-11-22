/*
Function creates custom menu when sheet is open.
> Contains items that perform various functions.

*/

function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('READ THIS')
      .addItem('Instructions', 'menuItem1') 
      .addToUi();
}

function menuItem1() {
  var html = HtmlService.createHtmlOutputFromFile('sidebar')
      .setTitle('Instructions')
      .setWidth(300);
  SpreadsheetApp.getUi() // Or DocumentApp or SlidesApp or FormApp.
      .showSidebar(html);
}
