from sqlite3 import Connection, Row
from typing import Dict

class LinkRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def create_link(self, link_info) -> Dict:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (
                link_info['id'],
                link_info['trip_id'],
                link_info['link'],
                link_info['title'],
            )
        )
        self.__conn.commit()
    def get_links_by_trip_id(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM links where trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        links = cursor.fetchall()
        return links