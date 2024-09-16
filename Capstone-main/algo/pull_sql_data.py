import pandas as pd
import sys, os, pyodbc

sqlServer = "capstone-database.database.windows.net"
username = "capstone"
password = "groupn14!"
database = "DataStorage"
driver = "{ODBC Driver 18 for SQL Server}"

try:

    connection = pyodbc.connect(
        f'Driver={driver};'
        f'Server=tcp:{sqlServer};'
        f'Database={database};'
        f'UID={username};'
        f'PWD={password};'
        'Encrypt=yes;'
        'TrustServerCertificate=no;'
        'Connection Timeout=30;'
    )

    # establish cursor to interact with SQL DB
    cursor = connection.cursor()

    cursor.execute("SELECT TempC FROM dbo.archive")

    rows = cursor.fetchall()

    for row in rows:
        tempC = row

    print("Temperature: {tempC}")

    cursor.close()
    connection.close()

except Exception as e:
    print("An error occured when connecting to the database:", e)
    sys.exit(1)