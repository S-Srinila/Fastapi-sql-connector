import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector(
        host="localhost",
        user="root",
        password="root@1234#",
        database="expenses_db",
    )
    except Error as e:(
        print("Database connection error:", e))
    return None



