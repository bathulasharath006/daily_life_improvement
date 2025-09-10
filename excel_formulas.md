# Excel Formulas

- **VLookUp :** = VLOOKUP(search_key, range, index, [is_sorted])

  - Exa: =VLOOKUP(A2, 'Final List'!$A$2:$B$285, 2, FALSE)
  - Use =IFERROR( Formula_or_value, if_error_value) , for better handling the #NA values.
  - =IFERROR(VLOOKUP(A2,IMPORTRANGE("https://docs.google.com/spreadsheets/d/SHEET_ID/edit?usp=sharing", "Final List(THIS_IS_SUBSHEET_NAME)!$A$2:$B$466"),2, FALSE), "Data Unavailable")  , for referencing different sheet.

- Extra: 

  - =CONCAT(value1, value2), Joins two columns and gives new value.
  - =COUNTIF(A:A, A2)>1  ,  Unique Values get FALSE and Duplicates get TRUE.




=XLOOKUP(
  C2,
  IMPORTRANGE("1WJbLDpxljX16lD_LPKHCmZbv1TGp8ED_u5G1IviQYVo", "Consolidated Lab Marks!C2:C274"),
  IMPORTRANGE("1WJbLDpxljX16lD_LPKHCmZbv1TGp8ED_u5G1IviQYVo [FILE_ID]", "Consolidated Lab Marks!J2:N274"),
  "Not Found"
)

