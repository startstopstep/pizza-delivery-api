from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///pizza-delivery-api.db',
                       echo=True)

Base = declarative_base()
Session = sessionmaker()
