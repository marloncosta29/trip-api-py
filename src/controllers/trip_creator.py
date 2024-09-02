from typing import Dict
import uuid
from src.models.repositories.trip_repository import TripRepository
from src.models.repositories.email_to_invite_repossitoory import EmailToInviteRepository

from src.drivers.email_sender import send_email

class TripCreator:
    def __init__(self, trip_repository: TripRepository, email_repository: EmailToInviteRepository) -> None:
        self.__trip_repository = trip_repository
        self.__email_repository = email_repository
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id}
            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__email_repository.registry_email({
                        "id": str(uuid.uuid4()),
                        "trip_id": trip_id,
                        "email": email
                    })
            send_email(
                [body['owner_email']], 
                'localhost:3000/trips/{trip_id}/confirm'
            )
            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }