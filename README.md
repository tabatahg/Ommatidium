# ommatidium

## Layered (simple to complex) approach for image to text app

# Overview

DB: SQL
API and frontend: python

Build app from simple to complex starting from back to front with an exception for the first iteration. 

SQL to server/api to frontend.

# May need to think about other online databases

# First iteration:

* Create SQL table with simple values: calories, proteins, carbohydrates, and fats
* Import Pandas and setup CSV into dictionary variable for SQL
* Also setup a JSON file into dictionary variable for SQL.
* Create connection string and scripts to read dictionary variable.
* Test with pseudo CSV data and create scripts for data flow from front to back.
* Retrieve data from DB to front-end in CSV file.

# Second iteration:

* DB is same as first iteration.
* Import pytesseract.  Setup for image to text conversion.
* Start with images from computer.
* Develop cleaning script to separate usable data from text. (My thoughts are to develop a filter function to select specific strings of data eg. {calories: value, protein: value, etc} then selected data into a dictionary.
* Image dictionary will use scripts from first iteration and follow the same data flow.
* After, retrieve data from DB to front-end into CSV file.

# Third iteration:

* Add ANTz functionality. Convert image dictionary into a CSV file that can be created into a glyph.
* Export node csv file.
* Process node csv file into glyph to be visually displayed.
* Once the glyph is fully fleshed out. Additional SQL elements can be added.

# Fourth iteration:

* Current thoughts are to either use a language that can wrap the existing program that will be dual compatible with either iOS or android. Or just focus on one, in which case I would choose iOs as it is supposedly faster to develop.
        * If possible, I would like input on whether there is any other considerations I should take note of for development with a cell phone or whether there is a better alternative.
	* Another concern is DB. It’s been noted that SQLite is a program that can serve as a DB for cell phones. Otherwise, an open source DB such as postgres or firebase may need to be used.
* Add cell phone camera functionality. Or ability to process with existing pictures within a cell phone.

# Fifth Iteration: 

* Develop UI/UX experience.  
* Iteration 1-4 will focus on functionality. This iteration will focus refactoring the code and making the program user friendly.


This is it.
Any suggestions or concerns are welcome.

