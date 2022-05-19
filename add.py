import pyodbc


try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ernie\Downloads\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('''
                INSERT INTO Table1(ID, FullName, Age, Address, Birthdate, SemGrade) 
                VALUES(?,?,?,?,?,?)''',
                (11, 'Ernest Danniel R. Tiston', 18,'Cavite', '3/15/2004', 90))

    database.commit()

    print("Data Added")

except pyodbc.Error:
    print("Error in Connection")