from sqlalchemy import create_engine, text
import json
import pandas as pd
import requests

def getData(symbol, name = "NaN"):
    """
    Takes in the symbol and optionally the full name and returns a tuple
    containing metadata of the stock/currency etc 
    and a pandas dataframe containing 1m trading data from 
    most recent 5 days of data.
    """
    with open('headers.json') as f:
        headers = json.load(f)
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?metrics=high?&interval=1m&range=5d'
    receivedHtml = requests.get(url, headers=headers)
    htmlJson = receivedHtml.json()
    chart = htmlJson['chart']
    importantInfo = chart['result'][0]['meta']
    symbolInfoTuple = (importantInfo['symbol'], name, importantInfo['currency'], importantInfo['exchangeName'], importantInfo['instrumentType'])
    oneMinuteData = {
        'time' : chart['result'][0]['timestamp'],
        'high'  : chart['result'][0]['indicators']['quote'][0]['high'],
        'open'  : chart['result'][0]['indicators']['quote'][0]['open'],
        'low'   : chart['result'][0]['indicators']['quote'][0]['low'],
        'volume': chart['result'][0]['indicators']['quote'][0]['volume'],
        'close' : chart['result'][0]['indicators']['quote'][0]['close']
    }
    dfStockData = pd.DataFrame.from_dict(oneMinuteData)
    dfStockData['time'] = pd.to_datetime(dfStockData['time'], unit='s')
    dfStockData.set_index(['time'], inplace=True)
    return symbolInfoTuple, dfStockData

def createEngine():
    """
    Returns an sqlalchemy engine to a postgresql database
    """
    with open('accessCredentials.json') as f:
        accessDetails = json.load(f)
        hostname = accessDetails["hostname"]
        database = accessDetails['database']
        username = accessDetails['username']
        port_id = accessDetails['port_id']
        pwd = accessDetails['pwd']
    urlMydb = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username,pwd,hostname,port_id,database)
    return create_engine(urlMydb, echo=True)

def createStockTable(symbol, name = "NaN"):
    """
    Updates the database to include latest prices of the stock 
    """
    symbolInfoTuple, dfStockData  = getData(symbol, name)
    engine = createEngine()
    dfEmpty = dfStockData[0:0]
    with engine.connect() as conn:
        stmt = "SELECT symbol FROM stocks WHERE symbol = \'{}\'".format(symbol)
        result = conn.execute(text(stmt))
        dfEmpty.to_sql("{}".format(symbol), conn, if_exists = "append", method = 'multi')
        conn.commit()
        if int(result.rowcount) == 0:
            insertScript = "INSERT INTO stocks VALUES "+str(symbolInfoTuple)
            conn.execute(text(insertScript))
        else:
            stmt = "SELECT MAX(Time) FROM \"{}\"".format(symbol)
            result = conn.execute(text(stmt))
            if int(result.rowcount) != 0:
                for row in result:
                    maxTime = row[0]
                dfStockData = dfStockData[dfStockData.index > maxTime]
        dfStockData.to_sql("{}".format(symbol), conn, if_exists = "append", method = 'multi')
        conn.commit()

createStockTable("AAPL", "Apple Inc")