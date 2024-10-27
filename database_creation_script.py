import os
import mysql.connector
from mysql.connector import Error
import json

# Get the current working directory
current_dir = os.getcwd()
json_file_path = os.path.join(current_dir, 'mysql_db_acc_detail.json')

# Open and read the JSON file
with open(json_file_path, 'r') as json_file:
    db_details = json.load(json_file)

database = db_details.get('database')
user = db_details.get('user')
password = db_details.get('password')
host = db_details.get('host')
port = db_details.get('port')

# Function to execute SQL commands from a file
def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
        # Split the script into individual statements and execute them
        for statement in sql_script.split(';'):
            if statement.strip():  # Skip empty statements
                try:
                    cursor.execute(statement)
                except Error as e:
                    print(f"Error executing statement: {statement[:30]}... -> {e}")

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,  # Replace with your username
            password=password # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Get the current working directory
            current_directory = os.getcwd()
            sql_file_path = os.path.join(current_directory, 'supermarket_db_schema.sql')

            # Execute SQL file
            execute_sql_file(cursor, sql_file_path)

            print("SQL file executed successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

create_database()

