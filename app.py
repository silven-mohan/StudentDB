#app.py

# import modules:
import mysql.connector

# -------- Database Connection ------------
def connect_database():
    return mysql.connector.connect(
        host="ip",
        user="root",
        password="",
        database="STUDDB"
    )