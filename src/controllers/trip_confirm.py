from src.models.repositories.trip_repository import TripRepository

class TripConfirm:
    def __init__(self, trip_repository: TripRepository) -> None:
        self.__trip_repository = trip_repository
    def execute(self, trip_id):
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {
                "body": None,
                "status_code": 204
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }