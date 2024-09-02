import uuid
from typing import Dict

from src.models.repositories.participants_repository import ParticipantRepository
from src.models.repositories.email_to_invite_repossitoory import EmailToInviteRepository


class Participantcreator:
    def __init__(self, participant_repository: ParticipantRepository, email_repository: EmailToInviteRepository) -> None:
        self.__participant_repository = participant_repository
        self.__email_repository = email_repository
    def execute(self, body, trip_id):
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            email_info = {
                "id":  email_id,
                "trip_id": trip_id,
                "email": body["email"],
            }
            participant_info = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }
            self.__email_repository.registry_email(email_info)
            self.__participant_repository.registry_participant(participant_info)
            return {
                "body": {
                    "participant_id": participant_id
                },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }