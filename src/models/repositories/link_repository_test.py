import uuid
from datetime import datetime, timedelta
from src.models.repositories.link_repository import LinkRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_create_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    link_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "www.google.com",
        "title": "Vianjando com o google"
    }
    link_repository.create_link(link_info)
def test_get_links_by_trip_id():
    conn = db_connection_handler.get_connection()
    link_repository = LinkRepository(conn)
    trip_id_to_test = str(uuid.uuid4())

    link_info_1 = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id_to_test,
        "link": "www.amazon.com",
        "title": "Vianjando com o amazon"
    }
    link_info_2 = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id_to_test,
        "link": "www.ilhas-paradise.com",
        "title": "Conhecendo as melhores ilhas"
    }
    link_repository.create_link(link_info_1)
    link_repository.create_link(link_info_2)
    links = link_repository.get_links_by_trip_id(trip_id_to_test)
    assert len(links) == 2