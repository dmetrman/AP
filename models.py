from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    brand = Column(String)
    model = Column(String)
    status = Column(String)

    def __repr__(self):
        return "<Car(brand='{}', model='{}', status='{}')>" \
            .format(self.brand, self.model, self.status)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return "<User(name='{}')>" \
            .format(self.name)


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    car_id = Column(Integer(), ForeignKey('car.id'))
    beginningDate = Column(DateTime)
    amountOfDays = Column(Integer)
    complete = Column(String)

    def __repr__(self):
        return "<Order(user='{}', car='{}', beginningDate='{}', amountOfDays={}, complete='{}')>" \
            .format(self.user_id, self.car_id, self.beginningDate, self.amountOfDays, self.complete)