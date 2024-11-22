from sqlalchemy import (
Column,
Integer,
String,
Float,
Date,
SmallInteger
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Categories(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    fio = Column(String)
    login = Column(String)
    password = Column(String)
    pin_code = Column(SmallInteger)
    
class PaymentList(Base):
    __tablename__ = "payment_list"
    
    id = Column(Integer, primary_key=True)
    pay_day = Column(Date)
    category_id = Column(Integer, ForeignKey(Categories.id))
    pay_name = Column(String)
    pay_count = Column(SmallInteger)
    pay_cost = Column(Float)
    user_id = Column(Integer, ForeignKey(Users.id))
    
    user_rel = relationship("Users")
    category_rel = relationship("Categories")
    
def create_connection():
    engine = create_engine("postgresql://postgres@localhost:5432/paymentdb", echo = True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session(bind=engine)
    return session