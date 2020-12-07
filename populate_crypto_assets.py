from requests import Request, Session, request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from model import Coin, Base
 
engine = create_engine('postgresql://admin:admin@localhost/crypto_app')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# # Insert a Person in the person table
# new_person = Person(name='new person')
# session.add(new_person)
# session.commit()
 
# # Insert an Address in the address table
# new_address = Address(post_code='00000', person=new_person)
# session.add(new_address)
# session.commit()


#https://www.coingecko.com/api/documentations/v3#/coins/get_coins_list
r = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=200&page=1&sparkline=false")


# print(r.json()[0])
for x in r.json():

    print(x['id'],x['symbol'],x['name'])
    new_coin = Coin(coin_id=x['id'],symbol =x['symbol'] , name =x['name'])
    session.add(new_coin)
    session.commit()
    

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#   'start':'1',
#   'limit':'5000',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': '5bb5e0e4-b748-45a8-951e-8bd5980f601c',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
  
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)