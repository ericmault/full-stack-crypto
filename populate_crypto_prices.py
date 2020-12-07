from requests import Request, Session, request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
 
from model import Coin, Base
 
engine = create_engine('postgresql://admin:admin@localhost/crypto_app')

connection = engine.connect()

metadata = MetaData()

coins = Table('coin', metadata, autoload=True, autoload_with=engine)
 
 
print(coins.columns.keys())

print(repr(metadata.tables['coin']))


query = select([coins])

ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()
for x in ResultSet:
    #https://api.coingecko.com/api/v3/coins/bitcoin

    r = requests.get(f"https://api.coingecko.com/api/v3/coins/{x.coin_id}?tickers=true&market_data=false&community_data=false&developer_data=false&sparkline=false")
    print(r.json())


    
# chunk_size = 100
# for i in range(0, len(ResultSet), chunk_size):
#     symbol_chunk = ResultSet[i:i+chunk_size]
#     print(symbol_chunk[0].coin_id)
#     # r = requests.get(f"https://api.coingecko.com/api/v3/coins/{symbol_chunk.coin_id}?tickers=true&market_data=false&community_data=false&developer_data=false&sparkline=false")
#     # print(r.json)

