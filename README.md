# READ ME
## Aims
The aim of this project are:
* to enable storage of large amounts of market data in particular to store 1 minutely market data from Yahoo finance for the long term
* to create new models in algorithmic trading 
* to provide visualisation tools for trading
* to provide porfolio management 

So far the first bullet point has been completed. Given an empty postgresql database, running the database_setup.py file will create a new stocks table. Then running update_database.py with symbol from Yahoo finance will create a new table in the postgresql database with the trading data on that symbol. Running update_database.py every 5 days is all that is required to upload and keep 1 minutely market data on that symbol.  

### What does database_setup.py do?
Given an accessCredentials.json file (which contains the database login information to a postgresql database) a connection is made a postgresql database using sqlalchemy. Then using sqlalchemy orm a stocks table is created in the postgresql database. The stocks table contains many columns which fully describe a stock/commodities/currency etc. 

### What does update_database.py do?
Given an accessCredentials.json file (which contains the database login information to a postgresql database) a connection is made a postgresql database using sqlalchemy in particular using psycopg2. Then given a particular symbol or a market entity from yahoo finance 1 minutely data is scraped directly from yahoo finance (no external module is required but a headers.json file which will allow a http request to be sent yahoo finance from python and be successful) and then uploaded to the postgresql table with table name the same as the symbol. Running the file again will append any new trading data to the table.  
