from sqlite3 import Connection
from typing import Dict
class EmailToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def registry_email(self, email_info:  Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO emails_to_invite
                    (id, trip_id, email)
                VALUES
                    (?, ?, ?)
            ''',
            (
                email_info["id"],
                email_info["trip_id"],
                email_info["email"],
            )
        )
        self.__conn.commit()
    def get_registry_email_by_id(self, email_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE id = ?''', (email_id,)
        )
        email = cursor.fetchone()
        return email
    def find_registry_email_by_trip_id(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE trip_id = ?''', (trip_id,)
        )
        email = cursor.fetchmany()
        return email