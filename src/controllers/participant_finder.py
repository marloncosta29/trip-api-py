from typing import Dict
from src.models.repositories.participants_repository import ParticipantRepository

class ParticipantFinder:
    def __init__(self, participant_repository: ParticipantRepository) -> None:
        self.__participanty_repository = participant_repository
    def execute(self, trip_id: str) -> Dict:
        try:
            participants_dict = self.__participanty_repository.find_participants_from_trip(trip_id)
            participants = []
            print(participants_dict)
            for participant in participants_dict:
                participants.append({
                    "id": participant[0], 
                    "name" : participant[1], 
                    "is_confirmed" : participant[2] if participant[2] else 0, 
                    "email": participant[3],
                })
            return {
                "body": {"participants": participants},
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }    
    