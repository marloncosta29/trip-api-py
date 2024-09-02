import uuid
from typing import Dict
from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
    def __init__(self, activity_controller: ActivitiesRepository) -> None:
        self.__activity_controller = activity_controller
    def execute(self, body, trip_id):
        try:
            id = uuid.uuid4()
            activity_info = {
                'id': id,
                'trip_id': trip_id,
                'title': body["title"],
                'occurs_at': body["occurs_at"]
            }
            self.__activity_controller.registry_activities(activity_info)
            return {
                "body": {
                    "activity_id": id
                },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }