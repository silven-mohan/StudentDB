#app.py

# import modules:
import mysql.connector

# -------- Database Connection ------------
def connect_database():
    return mysql.connector.connect(
        host="localhost",
        port = 3306,
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


#--------Search Student--------

def search_student():
    ID = int(input("Enter id: "))

    query = "SELECT * from STUD WHERE ID = %s"
    values = (ID,) 
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



# ---------- Main Menu ------------

while True:
    print("\n=== Student Database Management ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Details of a student")
    print("4. Search for a student")
    print("5. Delete a student entry")
    print("6. Exit")

    choice = int(input("Choose one of the option: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        search_student()
    elif choice == 5:
        pass
    elif choice == 6:
        exit()
    else:
        print("Invlaid Option! Try Again!!")