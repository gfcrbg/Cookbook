### [Video Editing Mailer Form (Responses)](https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=1235288961)


Linked to Google Form: [Video Editing Mailer Form](https://docs.google.com/forms/d/e/1FAIpQLSe8E5jPB79x-8maTPPbFIm5DOgMAB0QmNgnr9bEDxTHRcyZog/viewform)

## Formulas

### [Tab] Master
1. Cell A2 -  
`=QUERY(ImportRange("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit?ts=5db07b8b#gid=264954571","Form Responses 1!A2:I" ))`

2. Cells J2:J - 
`=IF(ISTEXT(R2), TRIM(R2),IF(ISTEXT(S2), TRIM(S2),IF(ISTEXT(T2), TRIM(T2),IF(ISTEXT(U2), TRIM(U2),IF(ISTEXT(V2), TRIM(V2),IF(ISTEXT(W2), TRIM(W2)))))))`

3. Cells K2:K - 
`=IF(L2 = "SM Notified", "SM Notified", IF(L2 = "SM Addressed","SM Addressed", IF(M2 = "SM Notified", "SM Notified", IF(M2 = "SM Addressed","SM Addressed", IF(N2 = "SM Notified", "SM Notified", IF(N2 = "SM Addressed","SM Addressed", IF(O2 = "SM Notified", "SM Notified", IF(O2 = "SM Addressed","SM Addressed", IF(P2 = "SM Notified", "SM Notified",IF(P2 = "SM Addressed","SM Addressed", IF(Q2 = "SM Notified", "SM Notified", IF(Q2 = "SM Addressed","SM Addressed"))) )))))))))`

### [Tab] Cory Sunaz
1. Cell A2 
`=QUERY(IMPORTRANGE("https://docs.google.com/spreadsheets/d/1a3xgQz9oYaODT5mjT5B4cX-65b9XCnGxMABjk9ETCew/edit#gid=264954571","Form Responses 1!A2:I"))`

### [Tab] Emily Turner


### [Tab] Chelsea Llewellan


### [Tab] Jame Spring


### [Tab] Shelby Wideman


### [Tab] Manesh Upadhyaya




