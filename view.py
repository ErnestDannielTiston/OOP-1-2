import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ernie\Downloads\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('SELECT * FROM table1')
    for x in database.fetchall():
        print(x)




except pyodbc.Error:
    print("Error in Connection")