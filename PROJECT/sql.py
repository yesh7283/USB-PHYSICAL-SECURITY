import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7283",
        database="sup_database"
    )
    if conn.is_connected():
        print("Successfully connected to the database")
        conn.close()
except Error as e:
    print(f"Error: {e}")
