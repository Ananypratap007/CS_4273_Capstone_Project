from flask import Blueprint, render_template, jsonify, request
from flask import render_template
from weather import WeatherInfo
from datetime import datetime
# from algo import Algorithm
import pyodbc


views = Blueprint('views',__name__)

# Azure SQL Database configuration
server = 'capstone-database.database.windows.net'
database = 'DataStorage'
username = 'capstone'
password = 'groupn14!'
driver = '{ODBC Driver 17 for SQL Server}'  # Use the appropriate driver

# Create a connection string
connection_string = f'Driver={driver};Server=tcp:{server};Database={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'

@views.route('/', methods=['GET'])
def index_page():
    data = {}
    data['outside'] = get_data_from_weather_API()
    data['inside'] = get_data_from_sensor()
    data["user_input"]= get_user_input_data()
    return render_template("index.html", data=data)

@views.route('/window', methods=['GET'])
def window_page():
    return render_template("window.html")

@views.route('/update_data', methods=['POST'])
def update_data():
    input = request.json
    data = {}
    outside = get_data_from_weather_API()
    updated_inside = get_updated_data(outside, input.get("inside"), input.get("user"))
    data["outside"] = outside
    data["inside"] = updated_inside
    return jsonify(data)


@views.route('/update_control', methods=['POST'])
def update_control():
    data = request.json
    temp = data.get('temperature')
    humidity = data.get('humidity')
    light = data.get('light')
    response = {'message': 'Data received successfully'}
    return jsonify(response)

def get_updated_data(outside, inside, user):
    action = get_window_action(outside, inside, user)
    window_trigger(action)
    inside['temperature'] = update_inside_data(float(outside.get('temperature')), float(inside.get('temperature')))
    inside['humidity'] = update_inside_data(float(outside.get('humidity')), float(inside.get('humidity')))
    return inside

def insert_user_control_data():
    weatherInfo = WeatherInfo("Norman", "US", "67527409760b0484db2e2c1951850f0a")
    temperature = user_input.get('temperature')
    lux = user_input.get('light')
    humidity = user_input.get('humidity')


    try:
        # Establish a connection
        conn = create_db_connection()
        cursor = conn.cursor()
        print("SQL connection is opened")

        # Stored procedure execution
        stored_procedure = 'EXEC InsertUserData @Temperature=?, @Humidity=?, @Lux=?'
        params = (temperature, humidity, lux)

        cursor.execute(stored_procedure, params)
        conn.commit()  # Commit the transaction

        print("User data inserted successfully!")

    except Exception as e:
        print(f"Error inserting data: {e}")
        response = {'message': 'Error storing user data'}
        return jsonify(response), 500

    finally:
        if conn:
            conn.close()
            print("SQL connection is closed")

def get_data_from_weather_API():
    weatherInfo = WeatherInfo("Norman", "US", "67527409760b0484db2e2c1951850f0a")
    data = weatherInfo.get_weather_data()
    try:
        # Establish a connection
        conn = create_db_connection()
        cursor = conn.cursor()
        print("SQL connection is opened")


        # Create a cursor object using the cursor() method
        cursor = conn.cursor()

        # Data to be inserted
        current_datetime = datetime.now()
        date = current_datetime.strftime('%Y-%m-%d')
        time = current_datetime.strftime('%H:%M')
        lux = 0
        temp = data["temperature"]
        humid = data["humidity"]

        # Stored procedure execution
        stored_procedure = 'EXEC InsertWeatherData @Date=?, @Time=?, @Lux=?, @Temp=?, @Humid=?'
        params = (date, time, lux, temp, humid)

        cursor.execute(stored_procedure, params)
        conn.commit()  # Commit the transaction

        print("Data inserted successfully!")

    except Exception as e:
        print("An error occurred when connecting to the database:", e)
    finally:
        # Closing the connection
        if conn:
            cursor.close()
            conn.close()
            print("SQL connection is closed")


    return data

def get_data_from_sensor():
    try:
        # Establish a connection
        conn = create_db_connection()
        cursor = conn.cursor()
        
        query = query = """
                        SELECT TOP 1*
                        FROM dbo.weatherBox
                        ORDER BY date DESC, time DESC
                        """

        # execute the query
        cursor.execute(query)
        results = list(cursor.fetchone())

        # Get column names
        columns = [column[0] for column in cursor.description]
        
        # Create a dictionary with column names as keys and data as values
        data_dict = {col: val for col, val in zip(columns, results)}

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return data_dict 
    
    except Exception as e:
        return str(e)

def get_user_input_data():
    try:
        # Establish a connection
        conn = create_db_connection()
        cursor = conn.cursor()
        
        query = query = """
                        SELECT TOP 1*
                        FROM dbo.userInputData
                        ORDER BY created_at DESC
                        """

        # execute the query
        cursor.execute(query)
        results = list(cursor.fetchone())

        # Get column names
        columns = [column[0] for column in cursor.description]
        
        # Create a dictionary with column names as keys and data as values
        data_dict = {col: val for col, val in zip(columns, results)}

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return data_dict 
    
    except Exception as e:
        return str(e)

def create_db_connection():
    print("Attempt to connect to DB .....")
    return pyodbc.connect(connection_string)

def get_window_action(outside_data, inside_data, user_input):
    
    outTemp = float(outside_data.get('temperature'))
    inTemp = float(inside_data.get('temperature'))
    userTemp = float(user_input.get('temperature'))

    outHumid = float(outside_data.get('humidity'))
    inHumid = float(inside_data.get('humidity'))
    userHumid = float(user_input.get('humidity'))
    
    return check_window_action(comparition(outTemp, inTemp, userTemp), comparition(outHumid, inHumid, userHumid))
                               
def comparition(outside, inside, user):
    if user is not None:
        if outside == inside and outside == user:
            return None
        elif outside >= inside:
            return outside < user
        else:
            return outside >= user
    return None

def check_window_action (action1, action2):
    if action1 == action2:
        return action1
    else:
        return True

def update_inside_data(target, current):
    dif = target - current
    placeHolder = 0.1 
    updated_value = round(current + dif * placeHolder, 2)
    return updated_value

def window_trigger(action):
    if action == True:
        print("Window open")
    elif action == False:
        print("Window close")
    else:
        print("Do nothing")
