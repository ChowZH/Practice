# Assignment 2: Address Book
## 1. Function of the program: 
1.1 Save information (name, address, phone number, birthday)
1.2 Allow listing of all entries & searching for entries (by category/roll number)
1.3 Allow editing of entry via roll number

## 2. Detailed functions of each option:
2.1 New Entry:
2.1.1 Asks user for details including name, address, phone number, and birthday.
2.1.2 Appends DATABASE.in with new entry
2.1.3 Returns position of new entry in DATABASE.in as number

2.2 List all/Search:
2.2.1 List all
2.2.2 List by name
2.2.3 List by address
2.2.4 List by phone number
2.2.5 List by birthday
2.2.6 List by roll number

2.3 Edit:
2.3.1 Get target to edit, replaces target with new details, updates DATABASE.in

## 3. Specifications:
### A2_main.py
- A2_person.py is imported as "p"
- Roll number assigned in main.py, stored as attribute in address_book list, not as element in DATABASE.in
- Search function for name and address case sensitive.
- Search function for phone number and birthday returns entries containing query digits

### A2_person.py
- Constructor: creates person object
- __str__ returns entire entry as string

### DATABASE.in
- Format of entries as follows:
*name*:*address*:*phone_number*:*date_of_birth*

### A2_workflow
- Psuedocode for main python file

### A2_draft.py
- Code in alpha. Non-functional
- Moved project to A2_main.py

### TEST.py
- Code snippets to test functions before implementation in draft.py or main.py

## 3. Change log:
### A1. Basic functionality for making new entry
- Primary program loop with query for first branch of each option
- Entering details including name, address, phone, birthday
- Saved as entry in DATABASE.in
#### A1.1. Added input checking functionality
- Excludes all invalid inputs
#### A1.2. Added ID for entries
- Roll number for entries in DATABASE.in used for searching in the future
#### A1.3. Added utility functions
- Detail confirmation step before entry
- Premature exit options
- Return ID/roll number after entry
- Return to primary loop after entry
### A2. Expanding search functionality
- List all/list by category functionality
#### A2.1 Added edit functionality
- Editing address_book list possible
#### A2.2 Expanded edit functionality
- Edit now affects DATABASE.in
- Also added correctness test preventing some invalid inputs

### B1. Redone entire code
- Moved old code to draft.py, now using A2_main.py with A2_draft.py as refernce
### B1.1 Tidying up code (final)
- Renamed confusing variables to make more sense in context
- Added comments where appropriate
- Ideally would exclude draft.py and test.py in final version