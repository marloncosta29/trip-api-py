from typing import Dict
from collections import defaultdict

from src.models.repositories.link_repository import LinkRepository

class LinkFinder:
    def __init__(self, link_repository: LinkRepository) -> None:
        self.__link_repository = link_repository
    def execute(self, trip_id):
        try:
            links = []
            links_list = self.__link_repository.get_links_by_trip_id(trip_id)
            for link in links_list:
                links.append({
                'id': link[0],
                'trip_id': link[1],
                'link': link[2],
                'title': link[3],
                })
            return {
                "body":{ "links": links},
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                 "status_code": 400
            }