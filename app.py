#app.py

# import modules:
import mysql.connector

# -------- Database Connection ------------
def connect_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="STUDDB"
    )



# ---------- ADD Student -------------------
def add_student():
    ID = int(input("Enter Student ID: "))
    NAME = input("Enter the Student Name: ")
    AGE = int(input("Enter Age: "))
    EMAIL = input("Enter the Student Email: ")
    YEAR = int(input("Enter the year in which the student is studying: "))


    query = "INSERT INTO STUD (ID, NAME, AGE, EMAIL, YEAR) VALUES (%s, %s, %s, %s, %s)"

    values = (ID, NAME, AGE, EMAIL, YEAR)

    db = connect_database()
    cursor = db.cursor()

    try:
        cursor.execute(query, values)
        db.commit()
        print("Student added successfully.")

    except mysql.connector.error as Error:
        print("Error: ", Error)

    finally:
        cursor.close()
        db.close()


add_student()

#--------Search Student--------

def search_student():
    ID = int(input("Enter id: "))

    query = "SELECT * from STUD WHERE ID = %s"
    values = ID 
    db = connect_database()
    cursor = db.cursor()

    try:
        cursor.execute(query, values)
        print("Student found.")

        student = cursor.fetchone()
        if student:
            print("ID: ",student[0])
            print("name: ",student[1])
            print("age : ",student[2])
            print("email: ",student[3])
            print("year: ",student[4])
        else:
            print("student data not found")
    except mysql.connector.error as Error:
        print("Error: ", Error)

    finally:
        cursor.close()
        db.close()

search_student()

    
