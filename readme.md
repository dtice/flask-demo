# CONNER PRACTICE API

## TODO
1. Build a POST endpoint to receive a .csv file
2. Should return the same CSV file but:
  - Dates are added with 3 days (i.e. 09/15 becomes 09/18)
  - Numeric columns are squared (multiplied by themselves)
  - String columns are converted to UPPER CASE
  - int columns are squared

## ASSUMPTIONS:
- Every column in the CSV is uniform (i.e. there are no string values in date columns, no int values in string columns, etc.)
- The type of column is in the column name (i.e. "dog_name[string]")
- Every CSV file has a first line including the headers

## Examples:
- INPUT:
```
owner_name[string],date_coming[date],num_dogs[int],dog_breed[string]
"dill","09/13/2026",3,"husky"
"conner","09/15/2027",100,"malamute"
```

- OUTPUT:
```
owner_name[string],date_coming[date],num_dogs[int],dog_breed[string]
"DILL","09/16/2026",9,"HUSKY",
"CONNER","09/18/2027",10000,"MALAMUTE"
```