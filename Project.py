import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="signifydb"
)
cursor = conn.cursor()

createDB = "create database Employee"
useDB = "use Employee"
cursor.execute(createDB)
cursor.execute(useDB)

createTable = """CREATE TABLE IF NOT EXISTS Employees (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    salary INT
)"""
cursor.execute(createTable)

while True:
    print("1.Add employee \n2.Display employee \n3.Search employee \n4.Delete employee \n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = int(input("Enter employee id: "))
        name = input("Enter employee name: ")
        salary = int(input("Enter employee salary: "))
        insertQ = f"INSERT INTO Employees (id, name, salary) VALUES ({id}, '{name}', {salary})"
        cursor.execute(insertQ)
        conn.commit()
    elif choice == 2:
        cursor.execute("SELECT * FROM Employees")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    elif choice == 3:
        id = int(input("Enter employee id: "))
        cursor.execute(f"SELECT * FROM Employees WHERE id={id}")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    elif choice == 4:
        id = int(input("Enter employee id: "))
        cursor.execute(f"DELETE FROM Employees WHERE id={id}")
        print("Employee deleted")
        conn.commit()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

cursor.close()
conn.close()
