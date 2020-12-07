
# brew services start postgresql
# brew services stop postgresql
# psql postgres
# \q
# psql postgres -U admin
# https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker



Base = declarative_base()


class Coin(Base):
    __tablename__ = 'coin'
    
    id = Column(Integer, primary_key=True)
    coin_id = Column(String)
    symbol = Column(String)
    name = Column(String)
    
    
    def __repr__(self):
        return "<Coin(coin_id='%s', symbol='%s', name='%s')>" % (self.coin_id, self.symbol, self.name)
    
    
engine = create_engine('postgresql://admin:admin@localhost/crypto_app')

Base.metadata.create_all(engine)
    
    
# Session = sessionmaker(bind=engine)



# session = Session()

# ed_user = User(name='ed')


# session.add(ed_user)






