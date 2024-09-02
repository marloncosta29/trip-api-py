from typing import Dict
from src.models.repositories.trip_repository import TripRepository


class TripFinder:
    def __init__(self, trip_repository: TripRepository) -> None:
        self.__trip_repository = trip_repository
    def execute(self, trip_id):
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip: raise Exception("Trip not found!")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],  
                        "destination":  trip[1], 
                        "start_date":  trip[2], 
                        "end_date":  trip[3], 
                        "owner_name":  trip[4], 
                        "owner_email":  trip[5],
                        "status":  trip[6], 

                    }
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }
    