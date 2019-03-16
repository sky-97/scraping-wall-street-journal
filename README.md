# scraping-wall-street-journal

### what is wsg(wall street journal)?
The Wall Street Journal is a U.S. business-focused, English-language international daily newspaper based in New York City. The Journal, along with its Asian and European editions, is published six days a week by Dow Jones & Company, a division of News Corp.

### what is web scraping?
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer.
 
 
 ### Description
 I used company  stock symbol to get the details eg:apple symbol is AAPE,Then i created a database called stock.db where i made a table.created five columns name,current price,open and prior close.

* scraped 5 data points for each stock:
  * Current Price
  * Price change since open (%)
  * Price change since open ($ value)
  * Open, Prior close

### INSTALLING
* python 3
 * beautifulsoup library
 * requests library
 * sqlite3 for database
 
### folder
* stock.db :- it contains database.
* stock.py :- it contains all the code.
