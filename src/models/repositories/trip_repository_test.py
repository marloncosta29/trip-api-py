import uuid
from datetime import datetime, timedelta
from src.models.repositories.trip_repository import TripRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip_infos = {
        "id": trip_id,
        "destination": "ilhas de ferias",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Janaina",
        "owner_email": "janaina@email.com"
    }
    trip_repository.create_trip(trip_infos)

def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip = trip_repository.find_trip_by_id(trip_id)
    print(trip)
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trip_repository = TripRepository(conn)
    trip_repository.update_trip_status(trip_id)

    


