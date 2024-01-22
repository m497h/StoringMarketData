# READ ME
## Aims
The aim of this project are:
* to enable storage of large amounts of market data in particular to store 1 minutely market data from Yahoo finance for the long term
* to create new models in algorithmic trading 
* to provide visualisation tools for trading
* to provide porfolio management 

So far the first bullet point has been completed. Given an empty postgresql database, running the database_setup.py file will create a new stocks table. Then running update_database.py with symbol from Yahoo finance will create a new table in the postgresql database with the trading data on that symbol. Running update_database.py every 5 days is all that is required to upload and keep 1 minutely market data on that symbol.  

## Content

### What does database_setup.py do?
Given an accessCredentials.json file (which contains the database login information to a postgresql database) a connection is made a postgresql database using sqlalchemy. Then using sqlalchemy orm a stocks table is created in the postgresql database. The stocks table contains many columns which fully describe a stock/commodities/currency etc. 

### What does update_database.py do?
Given an accessCredentials.json file (which contains the database login information to a postgresql database) a connection is made a postgresql database using sqlalchemy in particular using psycopg2. Then given a particular symbol (of a stock/commodity...) from yahoo finance 1 minutely data is scraped directly from yahoo finance (no external module is required but a headers.json file which will allow a http request to be sent yahoo finance from python and be successful) and then uploaded to the postgresql table with table name the same as the symbol. Running the file again will append any new trading data to the table.  

### What does server.py and client.py do?
server.py sets up a server on the local machine which listens on port 8000 for any messages. Running client.py allows the user to send a message to the server and given the correct message the server will close. These files will be updated so that there is an api to the database which stores the market data.
