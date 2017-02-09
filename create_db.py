from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base, engine
from in_app_purchase import IAP
from app import App

# Create each table
Base.metadata.create_all(engine)
