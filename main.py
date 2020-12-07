from flask import Flask, render_template, jsonify,make_response

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
 
from model import Coin, Base

app = Flask(__name__)

engine = create_engine('postgresql://admin:admin@localhost/crypto_app')

connection = engine.connect()

metadata = MetaData()

coins = Table('coin', metadata, autoload=True, autoload_with=engine)

query = select([coins])


ResultProxy = connection.execute(query)

ResultSet = ResultProxy.fetchall()

@app.route('/')
def index():
    return render_template('index.html',coins=ResultSet)
    

@app.route('/hello')
def hello():
    return jsonify({'hello': 'world'})
    



if __name__ == '__main__':
    app.run(debug=True)