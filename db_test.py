import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ARYAN;"
    "DATABASE=EmployeeDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

conn.close()