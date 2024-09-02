from src.models.repositories.participants_repository import ParticipantRepository

class ParticipantConfirm:
    def __init__(self, participant_repository: ParticipantRepository) -> None:
        self.__participant_repository = participant_repository
    def execute(self, participant_id):
        try:
            self.__participant_repository.confirm_participant(participant_id)
            return {
                "body": None,
                "status_code": 204
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }