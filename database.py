from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base, engine
from in_app_purchase import IAP
from app import App

# Create session to commit item with
def create_session():
    Session = sessionmaker(bind=engine)
    send_session = Session()
    return send_session

# Function to add an in app purchase to db
def add_in_app_purchase(in_app_purchase):
    add_item_session = create_session()
    add_item_session.add(in_app_purchase)
    add_item_session.commit() # Commit in_app_purchase to database

# Get the list of purchases based on the user search
def get_purchase_list(query):
    get_purchases_session = create_session()
    if query[0].lower() == "app name":
        return get_purchases_session.query(IAP).filter_by(app_name=query[1]).all()
        print("here")
    elif query[0].lower() == "purchase name":
        return get_purchases_session.query(IAP).filter_by(purchase_name=query[1]).all()
    elif query[0].lower() == "date":
        return get_purchases_session.query(IAP).filter_by(date=query[1]).all()
    elif query[0].lower() == "state":
        return get_purchases_session.query(IAP).filter_by(state=query[1]).all()
    else:
        return []

# Get all sales
def get_all_sales():
    get_all_items = create_session()
    return get_all_items.query(IAP).all()

# App new app to database
def add_new_app(new_app):
    session = create_session()
    session.add(new_app) # Add new app to the database
    session.commit() # Commit new app

# Return all app names
def app_names():
    session = create_session()
    name_list = []
    for app in session.query(App).all():
        name_list.append(app.app_name)
    return name_list

# Return list of ids
def list_of_ids():
    all_items = get_all_sales()
    id_list = []
    for item in all_items:
        id_list.append(item.id)
    return id_list

# Delete item
def delete_by_id(id):
    session = create_session()
    item_to_delete = session.query(IAP).filter_by(id=id).one()
    session.delete(item_to_delete)
    session.commit()
