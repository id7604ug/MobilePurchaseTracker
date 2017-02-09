from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from base import Base

class IAP(Base):
    # Table name
    __tablename__ = 'purchases'

    # Columns of table
    id = Column(Integer, primary_key=True)
    app_name = Column(String)
    purchase_name = Column(String)
    price = Column(Float)
    amount = Column(Integer)
    date = Column(String)
    purchase_state = Column(String)
    percent_off = Column(Integer) # Sale price percent

    # Return all information if the object is printed
    def __repr__(self):
        return "ID: {}; App Name: {}; Purchase Name: {}; Price: {}; Amount: {}; Date: {}; State: {}; Percent Off: {}".format(self.id, self.app_name, self.purchase_name, self.price, self.amount, self.date, self.purchase_state, self.percent_off)
