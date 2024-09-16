import pandas as pd
import datetime
import sys, pyodbc

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
    sql = connection.cursor()

    print("successfully connected to ", sqlServer)

except Exception as e:
    print("An error occured when connecting to the database:", e)
    sys.exit(1)

file = r'generate/generativeSheet.xlsx'
df = pd.read_excel(file)

# rename dataframe labels to remove ' ' and special char
df.rename(columns={'Humid%': 'Humid'}, inplace=True)
df.rename(columns={'Temp C': 'Temp'}, inplace=True)
df.rename(columns={'Logging Time': 'LTime'}, inplace=True)

# retrieve the current time/date to compare with table
now = datetime.datetime.now()

# minor fix to Github actions time displacement 19:32 (Git time zone) -> 14:32 (Norman time zone)
now = now  - datetime.timedelta(hours=5)

currTime = now.time()
currDate = now.date()
hour = now.hour
min = now.minute

# compare now with value table
for i in range(len(df)):

    # get the hour and minute of each row on table
    compHour = df.iloc[i, 2].hour
    compMin = df.iloc[i, 2].minute

    # check if they are the same
    if compHour == hour:
        if compMin == min:

            # create a query for each of the rows by extracting the headers from the dataset and the values of the data in the dataset
            query = f"""INSERT INTO weatherBox ({df.columns[0]}, {df.columns[2]}, {df.columns[3]}, {df.columns[4]}, {df.columns[5].split()[0]}, {df.columns[6].replace("%", "")}) 
            VALUES ('{currDate}', '{currTime.replace(microsecond=0)}', {int(df.iloc[i, 3])}, {int(df.iloc[i, 4])}, {int(df.iloc[i, 5])}, {int(df.iloc[i, 6])});"""
            break

# print the query for 
print(f"executing {query}")

# execute query
sql.execute(query)

# commit changes made to database
connection.commit()

# close cursor and connection to sql database
sql.close()
connection.close()
