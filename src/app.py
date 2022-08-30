from decouple import config
from db import get_connection


try:
    connection=get_connection()
    with connection.cursor() as cursor:
        query="select * from profesor where id=1;"
        cursor.execute(query)
        row=cursor.fetchone()
        print(row)
    connection.close()
except Exception as ex:
    print(ex)