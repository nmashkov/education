import os
from dotenv import load_dotenv

from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey,
                        create_engine)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# env init
load_dotenv('./files/.env')
DB_PATH = os.environ.get('DB_PATH',
                         'postgresql://postgres:156628@localhost/mydatabase')
# db init
engine = create_engine(DB_PATH)
# create if not exist tables in db
Base = declarative_base()


# DB MODELS FOR USER, ITEM AND POSITION
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    adult = Column(Boolean)
    message = Column(String)
    
    items = relationship("Item", back_populates="owner")
    positions = relationship("Position", back_populates="employee")
 

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    
    
class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    pos_name = Column(String, index=True)
    description = Column(String, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))

    employee = relationship("User", back_populates="positions")


# make db session
SessionLocal = sessionmaker(autoflush=True, bind=engine)
