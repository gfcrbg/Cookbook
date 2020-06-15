### [Video Editing Mailer Form (Responses)](https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=1235288961)


Linked to Google Form: [Video Editing Mailer Form](https://docs.google.com/forms/d/e/1FAIpQLSe8E5jPB79x-8maTPPbFIm5DOgMAB0QmNgnr9bEDxTHRcyZog/viewform)

## Formulas
Last Updated: 6/15/2020

### [Tab] Main
1. Cell C3   
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Cory Sunaz!A2:I"))`

2. Cell O3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Emily Turner!A2:K"))`

3. Cell AA3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Chelsea Lewallen!A2:K"))`

4. Cell AM3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Jamie Spring!A2:K"))`

5. Cell AY3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Shelby Wideman!A2:K"))`

6. Cell BK3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Chris Davis!A2:K"))`

7. Cell BW3  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Manesh Upadhyaya!A2:K"))`

### [Tab] Cory Sunaz
1. Cell A2   
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Cory Sunaz'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Cory Sunaz", "SM Notified", " ")`

### [Tab] Emily Turner
1. Cell A2   
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Emily Turner'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Emily Turner", "SM Notified", " ")`

### [Tab] Chelsea Llewellan
1. Cell A2    
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Chelsea Lewallen'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Chelsea Llewellan", "SM Notified", " ")`

### [Tab] Jame Spring
1. Cell A2   
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Jamie Spring'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Jamie Spring", "SM Notified", " ")`

### [Tab] Shelby Wideman
1. Cell A2   
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Shelby Wideman'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Shelby Wideman", "SM Notified", " ")`

### [Tab] Chris Davis
1. Cell A2  
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Chris Davis'" )`

2. Cell K2 (column K)  
`=IF(E2 = "Chris Davis", "SM Notified", " ")`

### [_Hidden_ Tab] Manesh Upadhyaya
1. Cell A2    
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571", "Form Responses 1!A2:I"), "select * where Col5 = 'Manesh Upadhyaya'" )`

2. Cell K2 (column K)    
`=IF(E2 = "Manesh Upadhyaya", "SM Notified", " ")`

## Google Apps Script
1. Custom Menu 
2. Sidebar - Contains instructions on how to use the sheet.

## Misc.
The Scout Manager filter must only sort by the name of the scout manager in the respected tab.


