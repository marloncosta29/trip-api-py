import uuid
from datetime import datetime, timedelta
from src.models.repositories.email_to_invite_repossitoory import EmailToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email_id = str(uuid.uuid4())

def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_registry = EmailToInviteRepository(conn)

    email_trip_info = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "johndoe@email.com"
    }
    emails_to_invite_registry.registry_email(email_trip_info)

def test_get_registry_email_by_id():
    conn = db_connection_handler.get_connection()
    emails_to_invite_registry = EmailToInviteRepository(conn)
    email = emails_to_invite_registry.get_registry_email_by_id(email_id)
    print(email)
def test_find_registry_email_by_trip_id():
    conn = db_connection_handler.get_connection()
    emails_to_invite_registry = EmailToInviteRepository(conn)
    email = emails_to_invite_registry.find_registry_email_by_trip_id(trip_id)
    print(email)