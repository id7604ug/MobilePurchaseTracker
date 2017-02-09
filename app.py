from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from base import Base

class App(Base):
    # Table name
    __tablename__ = 'apps'

    # Columns of table
    id  = Column(Integer, primary_key=True)
    app_name = Column(String)
    items = Column(String)

    # Return all information if the object is printed
    def __repr__(self):
        return "ID: {}; App Name: {}; Items: {}".format(self.id, self.app_name, self.items)
