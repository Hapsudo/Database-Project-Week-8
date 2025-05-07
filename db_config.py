# For Database Configuration 
# config.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="student_portal"
    )

