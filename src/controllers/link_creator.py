from typing import Dict
import uuid

from src.models.repositories.link_repository import LinkRepository

class LinkCreator:
    def __init__(self, link_repository: LinkRepository) -> None:
        self.__link_repository = link_repository
    def execute(self, body, trip_id):
        try:
            link_id =  str(uuid.uuid4())
            link_info = {
                "id": link_id,
                "trip_id": trip_id,
                "title": body["title"],
                "link": body["url"],
            }
            self.__link_repository.create_link(link_info)
            return {
                "body":{ "id": link_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }