from sqlite3 import Connection
from typing import Dict, List

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def registry_activities(self, activities_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activitiess
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (   
               activities_info['id'],
               activities_info['trip_id'] ,
               activities_info['title'] ,
               activities_info['occurs_at'] 
            )
        )
        self.__conn.commit()
    
    def find_activitiess_from_trip(self, trip_id: str) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM activities
                WHERE p.trip_id = ?
            ''',
            (
                trip_id,
            )
        )
        activitiess = cursor.fetchall()
        return activitiess