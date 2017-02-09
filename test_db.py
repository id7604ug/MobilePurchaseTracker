import database
from in_app_purchase import IAP


session = database.create_session()
print(session.query(IAP).filter_by(app_name="clash").all())
