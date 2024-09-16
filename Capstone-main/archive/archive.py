import pyodbc

def run_stored_procedure():
    # Define your connection parameters
    server = "capstone-database.database.windows.net"
    username = "capstone"
    password = "groupn14!"
    database = "DataStorage"

    # Define the connection string
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Initialize the connection variable
    conn = None

    try:
        # Establish connection
        conn = pyodbc.connect(conn_str, timeout=10)  # Setting a timeout for the connection attempt
        print("Connected to database")

        # Create a cursor object using the connection
        cursor = conn.cursor()
        # Execute the stored procedure
        cursor.execute("EXEC MoveWeatherDataToArchive")
        conn.commit()  # Commit the transaction
        print("Stored procedure executed successfully")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        if conn:
            conn.close()  # Ensure the connection is closed
            print("Connection closed")

# Run the function
run_stored_procedure()
