from sqlalchemy import create_engine, Column, Integer, Boolean, DateTime, VARCHAR
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:123123@127.0.0.1/swagger_CarRental')
engine.connect()


SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)
BaseModel = declarative_base()


class car(BaseModel):
    __tablename__ = "car"
    car_id = Column(Integer, primary_key=True)
    model = Column(VARCHAR(45))
    brand = Column(VARCHAR(45))
    status = Column(VARCHAR(45))


class order(BaseModel):
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    car_id = Column(Integer)
    beginningDate = Column(DateTime)
    amountOfDays = Column(Integer)
    complete = Column(Boolean)


class user(BaseModel):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))
    surname = Column(VARCHAR(45))
    username = Column(VARCHAR(45))
    password = Column(VARCHAR(45))


class status(BaseModel):
    __tablename__ = "status"
    status_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(45))