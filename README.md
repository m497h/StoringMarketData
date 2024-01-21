# READ ME
## Aims
The aim of this project are:
* to enable storage of large amounts of market data in particular to store 1 minutely market data from Yahoo finance for the long term
* to create new models in algorithmic trading 
* to provide visualisation tools for trading
* to provide porfolio management 

So far the first bullet point has been completed. Given an empty postgresql database, running the database_setup.py file will create a new stocks table. Then running update_database.py with symbol from Yahoo finance will create a new table in the postgresql database with the trading data on that symbol. Running update_database.py every 5 days is all that is required to upload and keep 1 minutely market data on that symbol.  
