"""
Initialises the database
"""

import json
from sqlalchemy import create_engine, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

with open('accessCredentials.json') as f:
    accessDetails = json.load(f)
    hostname = accessDetails["hostname"]
    database = accessDetails['database']
    username = accessDetails['username']
    port_id = accessDetails['port_id']
    pwd = accessDetails['pwd']

urlMydb = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username,pwd,hostname,port_id,database)
engine = create_engine(urlMydb, echo=False)

class Base(DeclarativeBase):
    pass

class Stocks(Base):
    __tablename__ = "stocks"

    symbol: Mapped[int] = mapped_column(String(15), primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=True)
    currency: Mapped[str] = mapped_column(String(30))
    exchangeName: Mapped[str] = mapped_column(String(30))
    instrumentType: Mapped[str] = mapped_column(String(30), nullable=True)

Base.metadata.create_all(engine)