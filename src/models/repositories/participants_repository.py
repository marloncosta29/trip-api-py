from sqlite3 import Connection
from typing import Dict, List

class ParticipantRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def registry_participant(self, participant_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (   
               participant_info['id'],
               participant_info['trip_id'] ,
               participant_info['emails_to_invite_id'] ,
               participant_info['name'] 
            )
        )
        self.__conn.commit()
    def confirm_participant(self, participant_id):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE
                    id = ?
            ''',
            (participant_id,)
        )
        self.__conn.commit()
    def find_participants_from_trip(self, trip_id: str) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                FROM participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        participants = cursor.fetchall()
        return participants