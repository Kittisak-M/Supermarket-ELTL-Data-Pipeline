from faker import Faker
import random
import pandas as pd
import os
import logging
import json
import numpy as np

# branch table
# set = 20 branches
fake = Faker()

#### Generating Data Def function ####
# Thai cities to random
thai_cities = [
    'Bangkok', 'Chiang Mai', 'Phuket', 'Khon Kaen', 'Nakhon Ratchasima',
    'Ayutthaya', 'Nakhon Si Thammarat', 'Udon Thani', 'Hua Hin', 'Pattaya',
    'Sukhothai', 'Surat Thani', 'Ubon Ratchathani', 'Mae Hong Son', 'Lampang',
    'Ratchaburi', 'Nakhon Pathom', 'Songkhla', 'Loei', 'Trat', 'Chonburi',
    'Samut Prakan', 'Nonthaburi', 'Pathum Thani', 'Prachuap Khiri Khan', 'Phetchaburi',
    'Nakhon Nayok', 'Uttaradit', 'Kamphaeng Phet', 'Yasothon', 'Amnat Charoen',
    'Roi Et', 'Kalasin', 'Mukdahan', 'Sakon Nakhon', 'Saraburi',
    'Suphan Buri', 'Lopburi', 'Nakhon Phanom', 'Chaiyaphum', 'Buriram'
]

def generate_fake_branch_data(num_records):
    branch_data = []
    for _ in range(num_records):
        branch = {
            'branch_type': random.choice(['standalone', 'in_shopping_mall', 'in_community_mall', 'small_shop']),
            'city': random.choice(thai_cities),  # Random cities from list
            'country': 'Thailand',
            'phone_number': fake.phone_number(),
            'shop_open_date': fake.date_this_decade()
        }
        branch_data.append(branch)
    return branch_data

branches = generate_fake_branch_data(20) # number of records
branches_df = pd.DataFrame(branches)

# Product to category mapping
product_to_category = {
    # Fruits
    'Apple': 'Fruits',
    'Banana': 'Fruits',
    'Orange': 'Fruits',
    'Grapes': 'Fruits',
    'Strawberry': 'Fruits',
    'Blueberry': 'Fruits',
    'Pineapple': 'Fruits',
    'Mango': 'Fruits',
    'Peach': 'Fruits',
    'Cherry': 'Fruits',

    # Dairy
    'Milk': 'Dairy',
    'Cheese': 'Dairy',
    'Yogurt': 'Dairy',
    'Butter': 'Dairy',
    'Cream': 'Dairy',
    'Cottage Cheese': 'Dairy',

    # Bakery
    'Bread': 'Bakery',
    'Croissant': 'Bakery',
    'Bagels': 'Bakery',
    'Muffins': 'Bakery',
    'Donuts': 'Bakery',

    # Meat
    'Chicken Breast': 'Meat',
    'Ground Beef': 'Meat',
    'Pork Chops': 'Meat',
    'Steak': 'Meat',
    'Sausages': 'Meat',

    # Grains
    'Rice': 'Grains',
    'Pasta': 'Grains',
    'Quinoa': 'Grains',
    'Oats': 'Grains',
    'Barley': 'Grains',

    # Beverages
    'Soda': 'Beverages',
    'Orange Juice': 'Beverages',
    'Coffee': 'Beverages',
    'Tea': 'Beverages',
    'Water': 'Beverages',

    # Snacks
    'Chips': 'Snacks',
    'Pretzels': 'Snacks',
    'Nuts': 'Snacks',
    'Granola Bars': 'Snacks',
    'Cookies': 'Snacks',

    # Frozen Foods
    'Frozen Pizza': 'Frozen Foods',
    'Ice Cream': 'Frozen Foods',
    'Frozen Vegetables': 'Frozen Foods',
    'Frozen Fries': 'Frozen Foods',
    'Frozen Berries': 'Frozen Foods',

    # Condiments
    'Ketchup': 'Condiments',
    'Mustard': 'Condiments',
    'Mayonnaise': 'Condiments',
    'Barbecue Sauce': 'Condiments',
    'Soy Sauce': 'Condiments',

    # Household Supplies
    'Toilet Paper': 'Household Supplies',
    'Paper Towels': 'Household Supplies',
    'Laundry Detergent': 'Household Supplies',
    'Dish Soap': 'Household Supplies',
    'Cleaning Spray': 'Household Supplies',

    # Personal Care
    'Shampoo': 'Personal Care',
    'Conditioner': 'Personal Care',
    'Toothpaste': 'Personal Care',
    'Soap': 'Personal Care',
    'Deodorant': 'Personal Care',

    # Health Foods
    'Almond Milk': 'Health Foods',
    'Chia Seeds': 'Health Foods',
    'Spirulina': 'Health Foods',
    'Acai Berries': 'Health Foods',
    'Goji Berries': 'Health Foods'
}

def generate_all_products_data():
    product_data = []

    for product_name, category_name in product_to_category.items():
        product = {
            'product_name': product_name,
            'category_name': category_name

        }
        product_data.append(product)

    return product_data

products = generate_all_products_data()
products_df = pd.DataFrame(products)

# customers_table
# set 1000 customers

def generate_fake_customers_data(num_records):
    customer_data = []

    for _ in range(num_records):
        customer = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'city': fake.city(),
            'country': fake.country(),
            'registration_date': fake.date_this_decade()
        }
        customer_data.append(customer)

    return customer_data

customers = generate_fake_customers_data(1000)
customers_df = pd.DataFrame(customers)

# employees_table
# set = 100 employees
def generate_employees_data(num_records=50):
    employees_data = []

    for _ in range(num_records):
        employee = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'position': random.choice(['Manager', 'Sales Associate', 'Cashier', 'Stock Clerk', 'Supervisor']),
            'branch_id': random.randint(1, 20),  # 20 branches
            'salary': round(random.uniform(30000, 90000), 2),
            'hire_date': fake.date_this_decade(),
            'termination_date': fake.date_between(start_date='-1y', end_date='today') if random.choice([True, False]) else None,
            'email': fake.email(),
            'phone': fake.phone_number(),
            'is_active': random.choice([0, 1])
        }
        employees_data.append(employee)

    return employees_data

employees = generate_employees_data(100)

employees_df = pd.DataFrame(employees)

# inventory table
def create_inventory_data(num_branches, num_products):
    data = {
        'product_id': [],
        'branch_id': [],
        'quantity': [],
        'last_updated': []
    }

    for branch in range(1, num_branches + 1):
        for product in range(1, num_products + 1):
            data['product_id'].append(product)
            data['branch_id'].append(branch)
            data['quantity'].append(random.randint(0, 1000))
            data['last_updated'].append(fake.date_this_year())

    return pd.DataFrame(data)

inventory_df = create_inventory_data(20, 66)

# suppliers 20
def generate_fake_supplier_data(num_records):
    supplier_data = []

    for _ in range(num_records):
        supplier = {
            'supplier_name': fake.company(),
            'contact_name': fake.name(),
            'contact_email': fake.email(),
            'contact_phone': fake.phone_number(),
            'address': fake.address(),
            'city': fake.city(),
            'country': fake.country()
        }
        supplier_data.append(supplier)

    return supplier_data

suppliers = generate_fake_supplier_data(20)
suppliers_df = pd.DataFrame(suppliers)

## order
def generate_mock_orders(num_orders):
    orders = []
    for _ in range(num_orders):
        order = {
            'order_id' : np.nan,
            "customer_id": random.randint(1, 1000),  # 1000 customers for members
            # payment_id is auto increment in database
            "employee_id": random.randint(1, 50),  # 50 employees
            "branch_id": random.randint(1, 20),  # 20 branches
            "product_id": random.randint(1, 66),  # 66 products
            "order_date": fake.date_this_decade(),
            "amount": round(random.uniform(5.00, 500.00), 2),
            "quantities": random.randint(1, 30),
            "payment_method": random.choice(['credit_card', 'paypal', 'bank_transfer', 'cash']),
            "transaction_id": fake.uuid4(),  # Unique transaction ID
            "billing_address": fake.street_address(),
            "billing_city": fake.city(),
            "billing_country": fake.country()
        }
        orders.append(order)
    return orders
orders_data = generate_mock_orders(random.randint(500, 1500))
orders_df = pd.DataFrame(orders_data)

## Supplier
def generate_mock_supplier_orders(num_orders):
    supplier_orders = []
    for _ in range(num_orders):
        order = {
            'supplier_purchase_order_id' : np.nan,
            "supplier_id": random.randint(1, 20),
            "product_id": random.randint(1, 66),   # 66 products
            "employee_id": random.randint(1, 50),
            "branch_id": random.randint(1, 20),
            "order_date": fake.date_between(start_date='-2y', end_date='today'),
            "arrival_date": fake.date_between(start_date='-2y', end_date='today'),
            "quantity": random.randint(10, 500),
            "unit_price": round(random.uniform(5.0, 100.0), 2),
        }
        supplier_orders.append(order)
    return supplier_orders
supplier_orders_data = generate_mock_supplier_orders(random.randint(50, 300))
supplier_orders = pd.DataFrame(supplier_orders_data)
supplier_orders_data_df = pd.DataFrame(supplier_orders_data)
##### End Generate Data def function #####

########### DATABASE  ##############
# Import packages for Database connection code
import os
import json
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# # Get database Credential ##
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

# append df to my sql
def append_dataframe_to_mysql(df, table_name, host, database, user, password):
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
    engine = create_engine(connection_string)

    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

############### ETL def fucntion #############
import mysql.connector
import json

import json

def get_db_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None

def get_latest_id(column, table, filename="mysql_db_acc_detail.json"):
    """
    Get the latest (maximum) ID from the specified column and table.
    """
    config = get_db_config(filename)

    if not config:
        return None  # Exit if config loading failed

    try:
        connection = mysql.connector.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = f"SELECT MAX({column}) FROM {table}"
            cursor.execute(query)
            max_id = cursor.fetchone()[0]
            return max_id  # Return the maximum ID

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

############## END ETL def fucntion #############
########### END DATABASE #######################

import mysql.connector
import json

def get_db_config(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Configuration file not found.")
        return None

def get_max_id(column, table):
    config = get_db_config("mysql_db_acc_detail.json")
    if not config:
        return None  # Exit if config loading failed

    try:
        connection = mysql.connector.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Use backticks to avoid syntax error with reserved keywords
            query = f"SELECT MAX({column}) FROM `{table}`"
            cursor.execute(query)
            max_id = cursor.fetchone()[0]

            cursor.close()  # Close the cursor
            connection.close()  # Close the connection

            return max_id  # Return the maximum ID

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

################## Google drive def function #########################
import os
import json
import subprocess
import pickle
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime

## Def function ##
def upload_file_to_drive(file_name, folder_id):
    """
    Upload a file to Google Drive.
    :param file_name: The name of the file to upload.
    :param folder_id: The Google Drive folder ID where the file will be uploaded.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_drive_api_credential.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=creds)

    # Create a file metadata with the folder ID
    file_metadata = {
        'name': os.path.basename(file_name),  # Get just the filename for upload
        'parents': [folder_id]
    }

    # Read the file content
    media = MediaFileUpload(file_name, mimetype='application/sql')

    # Upload the file
    try:
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        timestamp = datetime.now().strftime("%d-%m-%Y")
        return f'Upload supermarket backup successfully in Google Drive on {timestamp}.'
    except Exception as e:
        return f"Error uploading file to Google Drive: {e}"
def get_folder_id_by_name(folder_name, parent_folder_id):
    """
    Search for a folder by its name inside a parent folder and return its folder ID.
    :param folder_name: The name of the folder to search for.
    :param parent_folder_id: The Google Drive folder ID where the search will be conducted.
    :return: The folder ID of the found folder or None if not found.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_drive_api_credential.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Build the Google Drive API service
    drive_service = build('drive', 'v3', credentials=creds)

    # Search for the folder inside the parent folder
    query = f"name = '{folder_name}' and '{parent_folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    folders = results.get('files', [])

    if folders:
        # If a folder is found, return its ID
        return folders[0]['id']
    else:
        return None

################## END Google drive def function #########################
################## Send e-mail ###################
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def send_success_email(to_emails,minute,second):
    sender_email = "example@gmail.com"
    password = "example"  # Use your App Password
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Prepare the email content
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Define the subject and body
    subject = f"ELT Process Completion Report - {current_date}"
    body = f"""
    Hello Team,

    The ELT process has been successfully completed today, {current_date}.
    ELT Process time taken is {minute} minutes and {second} seconds.

    Best regards,
    Kittisak M.
    """

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(to_emails)  # Join recipients with commas
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, to_emails, message.as_string())
        print("Complete report e-mail sent successfully!")
        logging.info("Complete report e-mail sent successfully!")
    except Exception as e:
        print(f"Failed to send complete report email: {e}")
        logging.error(f"Failed to send complete report email: {e}")
    finally:
        server.quit()

############## send Failed Email ###############
def send_failed_email(to_emails, error_message):
    sender_email = "example@gmail.com"
    password = "example"  # Use your App Password
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Prepare the email content
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Define the subject and body
    subject = f"ELT Process Failure Report - {current_date}!"
    body = f"""
    Hello Team,

    An error occurred during the ELT process on {current_date}.
    Error Message: {error_message[:100]}.
    Please contact [Name] at 097-xxxxxxx or via email at example@gmail.com for assistance.

    Best regards,
    Kittisak M.
    """

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ", ".join(to_emails)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Upgrade to a secure connection
        server.login(sender_email, password)
        server.sendmail(sender_email, to_emails, message.as_string())

        print("Failure report email sent successfully!")
        logging.info("Failure report email sent successfully!")
    except Exception as e:
        print(f"Failed to send failure report email: {e}")
        logging.error(f"Failed to send failure report email: {e}")
    finally:
        # Ensure the server is quit properly, only if it was initialized
        if 'server' in locals():
            server.quit()
################## END Send e-mail ###################

################## Delete File #######################
def delete_file(file_name, folder_id):
    """
    Deletes a file from Google Drive if it exists in the specified folder.

    Parameters:
        file_name (str): The name of the file to delete.
        folder_id (str): The ID of the folder to search in.

    Returns:
        bool: True if the file was deleted, False if not found.
    """
    # Search for the file by name within the specified folder
    query = f"name='{file_name}' and '{folder_id}' in parents and trashed=false"

    try:
        results = service.files().list(q=query, spaces='drive', pageSize=10,
                                       fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if items:
            # If the file exists, delete it
            for item in items:
                file_id = item['id']
                service.files().delete(fileId=file_id).execute()
                print(f"Deleted file '{file_name}' with ID '{file_id}' from the specified folder.")
                return True  # Return True after deleting
        else:
            print(f"File '{file_name}' does not exist in the specified folder.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
################## End  #######################

################## Storage check ###################
######### Local Storage ###########
import shutil

def check_disk_space(path="/"):
    total, used, free = shutil.disk_usage(path)

    print(f"Total: {total // (2**30)} GiB")
    logging.info(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    logging.info(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")
    logging.info(f"Free: {free // (2**30)} GiB")
    print(f"Percentage Used: {used / total * 100:.2f}%")
    logging.info(f"Percentage Used: {used / total * 100:.2f}%")


    percentage_used = used / total * 100

    # Check if used space exceeds 95%
    if percentage_used > 95:
        message = "Critical Warning: More than 95% of the disk space is used!"
        logging.warning(message)
        print(message)
    elif percentage_used > 90:
        message = "Warning: More than 90% of the disk space is used!"
        logging.warning(message)
        print(message)
    else:
        message = "Disk space usage is within acceptable limits."
        logging.info(message)
        print(message)

######################################

########## Google Drive Storage #########

import os
import pickle
import logging
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_google_drive():
    """Authenticate and return the Google Drive service."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('google_drive_api_credential.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

def check_google_drive_space(service):
    """Check the user's Google Drive space."""
    about = service.about().get(fields="storageQuota").execute()
    quota = about['storageQuota']

    total_space = int(quota['limit']) // (1024 ** 3)  # Convert to GiB
    used_space = int(quota['usage']) // (1024 ** 3)    # Convert to GiB
    free_space = total_space - used_space

    # Log and print disk usage information
    logging.info(f"Total: {total_space} GiB")
    logging.info(f"Used: {used_space} GiB")
    logging.info(f"Free: {free_space} GiB")
    percentage_used = (used_space / total_space) * 100
    logging.info(f"Percentage Used: {percentage_used:.2f}%")

    # Check the used space conditions
    if percentage_used > 95:
        message = "Critical Warning: More than 95% of Google Drive space is used!"
        logging.warning(message)
        print(message)
    elif percentage_used > 90:
        message = "Warning: More than 90% of Google Drive space is used!"
        logging.warning(message)
        print(message)
    else:
        message = "Google Drive space usage is within acceptable limits."
        logging.info(message)
        print(message)

######################################

### Start here
if __name__ == '__main__':
    ####### Email Config########
    recipients = ["kittisak.maungmanee@gmail.com"]
    ############################
    from datetime import datetime
    import logging
    import time

    etl_start_time = time.time()

    # Set up logging
    logging.basicConfig(filename=r'C:\supermarket\log\ELT_log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    ######## Check Storage ##########
    ## local storage
    check_disk_space()

    ## Google Drive
    drive_service = authenticate_google_drive()
    check_google_drive_space(drive_service)
    #################################
    # date format
    record_date = datetime.now().strftime("%d-%m-%Y")

    ####### START ELT process #######
    print(f"Starting ELT process on {record_date} ....")
    logging.info(f"Starting ELT process on {record_date} ....")
    ############## EXTRACT DATA ###################
    data_extraction_start_time = time.time()
    # branches_df
    # customers_df
    # employees_df
    # inventory_df
    # suppliers_df
    # payments_df
    # order_df
    # product_in_customers_df
    # product_df

    data_generators = [
    (generate_fake_branch_data, 20, 'branches_df', "Generated branch data"),
    (generate_fake_customers_data, 1000, 'customers_df', "Generated customer data"),
    (generate_employees_data, 100, 'employees_df', "Generated employee data"),
    (create_inventory_data, (20, 66), 'inventory_df', "Created inventory data"),
    (generate_fake_supplier_data, 20, 'suppliers_df', "Generated supplier data"),
    (generate_all_products_data, None, 'product_df', "Generated product data"),
    (generate_mock_orders, (random.randint(500, 1500)), 'orders_df', "Generated mock order data"),
    (generate_mock_supplier_orders, (random.randint(50, 300)), 'supplier_order_df', "Generated mock supplier order data")
    ]

    try:
        print(f"Extracting data from python faker() generated on {record_date} ....")
        logging.info(f"Extracting data from python faker() generated on {record_date} ....")

        start_time = time.time()

        branches = generate_fake_branch_data(20)  # number of records
        branches_df = pd.DataFrame(branches)
        logging.info("Generated branch data and created DataFrame.")

        customers = generate_fake_customers_data(1000)
        customers_df = pd.DataFrame(customers)
        logging.info("Generated customer data and created DataFrame.")

        employees = generate_employees_data(100)
        employees_df = pd.DataFrame(employees)
        logging.info("Generated employee data and created DataFrame.")

        inventory_df = create_inventory_data(20, 66)
        logging.info("Created inventory data.")

        suppliers = generate_fake_supplier_data(20)
        suppliers_df = pd.DataFrame(suppliers)
        logging.info("Generated supplier data and created DataFrame.")

        products = generate_all_products_data()
        product_df = pd.DataFrame(products)
        logging.info("Generated product data and created DataFrame.")

        customer_order_data = generate_mock_orders(random.randint(500, 1500))
        customer_order_df = pd.DataFrame(customer_order_data)
        logging.info("Generated mock order data and created DataFrame.")

        supplier_order_data = generate_mock_supplier_orders(random.randint(50, 300))
        supplier_order_df = pd.DataFrame(supplier_order_data)
        logging.info("Generated mock supplier order data and created DataFrame.")

        data_extraction_end_time = time.time()
        data_extraction_total_duration = data_extraction_end_time - data_extraction_start_time
        data_extraction_minutes = int(data_extraction_total_duration // 60)
        data_extraction_seconds = int(data_extraction_total_duration % 60)
        data_extraction_milliseconds = int((data_extraction_total_duration - int(data_extraction_total_duration)) * 1000)

        print(f"Extracting data from python faker() successfully.  Time taken:{data_extraction_minutes} minutes, {data_extraction_seconds} seconds, and {data_extraction_milliseconds} milliseconds.")
        logging.info(f"Extracting data from python faker() successfully. Time taken:{data_extraction_minutes} minutes, {data_extraction_seconds} seconds, and {data_extraction_milliseconds} milliseconds.")
    except Exception as e:
        logging.error(f"An error occurred | ERROR: {e}")
        print(f"Failed to generate data| ERROR: {e}")
        send_failed_email(recipients,"Failed to generate data")
        raise

    ########### End Extract Data ###################

    ############################################## Load Raw Data ############################################

    ############# Save raw data to Local Storage #############


    ### Save Raw_data to local storage ###
    print("Saving Raw data to 'C:\\supermarket\\raw_data'...")
    logging.info("Saving Raw data to 'C:\\supermarket\\raw_data'...")
    # file location to save
    raw_file_path = r'C:\\supermarket\\raw_data'
    # End time
    raw_data_start_time = time.time()
    # List of tuples with DataFrame names and their respective filenames
    raw_to_local_df = [
        (branches_df, 'raw_branch'),
        (customers_df, 'raw_customer'),
        (employees_df, 'raw_employee'),
        (inventory_df, 'raw_inventory'),
        (suppliers_df, 'raw_supplier'),
        (customer_order_df, 'raw_customer_order'),
        (product_df, 'raw_product'),
        (supplier_order_df, 'raw_supplier_order_data')
    ]

    try:
        # Loop through each DataFrame and its corresponding filename
        for df, name in raw_to_local_df:
            file_path = f'{raw_file_path}\\{name}_{record_date}.csv'
            df.to_csv(file_path, index=False)
            print(f"{name}_{record_date} saved successfully.")
            logging.info(f"{name}_{record_date} saved successfully.")

        print(f"All raw data files have been saved to {raw_file_path} on {record_date} successfully.")
        logging.info(f"All raw data files have been saved to {raw_file_path} on {record_date} successfully.")

    except Exception as e:
        print(f"Failed to save raw data files in local storage on {record_date} ERROR: {e}")
        logging.error(f"Failed to save raw data files in local storage on {record_date} ERROR: {e}")
        send_failed_email(recipients,f"Failed to save raw data files in local storage on {record_date}.")
        raise
    print("END Saving Raw data to 'C:\\supermarket\\raw_data'...")
    logging.info("END Saving Raw data to 'C:\\supermarket\\raw_data'...")
    ##############################################  End Save raw data to Local Storage ########################

    ################################ Save Raw Data to Google Drive ##########################################
    print("Saving Raw data files to Google Drive...")
    logging.info("Saving Raw data files to Google Drive...")



    raw_branches_csv = f'{raw_file_path}\\raw_branch_{record_date}.csv'
    raw_customers_csv = f'{raw_file_path}\\raw_customer_{record_date}.csv'
    raw_employees_csv = f'{raw_file_path}\\raw_employee_{record_date}.csv'
    raw_inventory_csv = f'{raw_file_path}\\raw_inventory_{record_date}.csv'
    raw_supplier_csv = f'{raw_file_path}\\raw_supplier_{record_date}.csv'
    raw_customer_order_csv = f'{raw_file_path}\\raw_customer_order_{record_date}.csv'
    raw_product_csv = f'{raw_file_path}\\raw_product_{record_date}.csv'
    raw_supplier_order_csv = f'{raw_file_path}\\raw_supplier_order_data_{record_date}.csv'

    try:
        print("Getting Google Drive folder id... ")
        logging.info("Getting Google Drive folder id...")

        # Retrieve folder IDs and log/print the process
        main_folder_id = "1pg99tJ7dIaPyEb8vS9VvWTxgHGzk-BD3" # main_folder

        super_backup_id = get_folder_id_by_name("supermarket", main_folder_id)
        logging.info(f"Successfully retrieved 'supermarket' folder ID: {super_backup_id}")
        print(f"Successfully retrieved 'supermarket' folder ID: {super_backup_id}")

        log_backup_id = get_folder_id_by_name("log", super_backup_id)
        logging.info(f"Successfully retrieved 'log' folder ID: {log_backup_id}")
        print(f"Successfully retrieved 'log' folder ID: {log_backup_id}")

        raw_backup_id = get_folder_id_by_name("raw_data", super_backup_id)
        logging.info(f"Successfully retrieved 'raw_data' folder ID: {raw_backup_id}")
        print(f"Successfully retrieved 'raw_data' folder ID: {raw_backup_id}")

        transform_backup_id = get_folder_id_by_name("transformed_data", super_backup_id)
        logging.info(f"Successfully retrieved 'transformed_data' folder ID: {transform_backup_id}")
        print(f"Successfully retrieved 'transformed_data' folder ID: {transform_backup_id}")

        print("Successfully get the folder id in Google Drive")
        logging.info("Successfully get the folder id in Google Drive")
    except Exception as e:
        print(f"Failed to get the folder id in Google | An error occurred:{e}")
        logging.error(f"Failed to get the folder id in Google | An error occurred:{e}")
        send_failed_email(recipients,f"Failed to get the folder id in Google")
        raise
    # files to upload to google drive
    files = [
        (raw_branches_csv, 'raw_branches_csv'),
        (raw_customers_csv, 'raw_customers_csv'),
        (raw_employees_csv, 'raw_employees_csv'),
        (raw_inventory_csv, 'raw_inventory_csv'),
        (raw_supplier_csv, 'raw_supplier_csv'),
        (raw_customer_order_csv, 'raw_orders_csv'),
        (raw_product_csv, 'raw_product_csv'),
        (raw_supplier_order_csv, 'raw_supplier_order_csv')
    ]

    try:
        print("Uploading raw data files to Google Drive 'supermarket\\raw_data'...")
        logging.info("Uploading raw data files to Google Drive 'supermarket\\raw_data'...")

        # Loop through each file and upload it to Google Drive
        for file, file_name in files:
            upload_file_to_drive(file, raw_backup_id)
            message = f"Successfully uploaded {file_name} to Google Drive on {record_date}"
            print(message)
            logging.info(message)

        print(f"All raw data files on {record_date} saved to Google Drive successfully.")
        logging.info(f"All raw data files on {record_date} saved to Google Drive successfully.")

    except Exception as e:
        print(f"Failed to save raw data files to Google Drive: {e}")
        logging.error(f"Failed to save raw data files to Google Drive: {e}")
        send_failed_email(recipients,"Failed to save raw data files to Google Drive")
        raise
    # End time
    raw_data_end_time = time.time()
    raw_data_total_duration = raw_data_end_time - raw_data_start_time
    raw_data_minutes = int(raw_data_total_duration // 60)
    raw_data_seconds = int(raw_data_total_duration % 60)
    raw_data_milliseconds = int((raw_data_total_duration - int(raw_data_total_duration)) * 1000)
    print(f"END Saving Raw data. Time taken:{raw_data_minutes} minutes, {raw_data_seconds} seconds, and {raw_data_milliseconds} milliseconds.")
    logging.info(f"END Saving Raw data. Time taken:{raw_data_minutes} minutes, {raw_data_seconds} seconds, and {raw_data_milliseconds} milliseconds.")
    ################################################ END Save Raw Data to Google Drive ###################################

    ################################################ Transformed Data ########################################
    ####### Order table #########
    print("Transforming data....")
    logging.info("Transforming data....")

    # STart time
    transfomed_data_start_time = time.time()
    try:
        # Copying the original DataFrame
        main_orders_df = orders_df.copy()

        # Remove customer_id randomly
        num_nulls = int(len(main_orders_df) * round(random.uniform(0, 0.5), 4))
        indices_for_nulls = random.sample(range(len(main_orders_df)), num_nulls)
        main_orders_df.loc[indices_for_nulls, 'customer_id'] = None

        # Insert a new column for payment_id with NaN values
        main_orders_df.insert(loc=1, column='payment_id', value=np.nan)


        # Get the latest payment_id from the payments table
        max_order_id = get_latest_id('payment_id', 'payments')
        if max_order_id is None:
            max_order_id = 0

        # Fill missing payment_ids
        num_missing = main_orders_df['payment_id'].isna().sum()
        new_payment_ids = list(range(max_order_id + 1, max_order_id + 1 + num_missing))

        # Exclude empty items from the new_payment_ids before combining
        if new_payment_ids:
            main_orders_df['payment_id'] = main_orders_df['payment_id'].combine_first(pd.Series(new_payment_ids))

        # Handle order_id for orders table
        max_payment_id = get_latest_id('order_id', 'customer_order')
        if max_payment_id is None:
            max_payment_id = 0

        # Fill missing order_ids
        num_missing_order = main_orders_df['order_id'].isna().sum()
        new_order_ids = list(range(max_payment_id + 1, max_payment_id + 1 + num_missing_order))

        # Exclude empty items from new_order_ids before combining
        if new_order_ids:
            main_orders_df['order_id'] = main_orders_df['order_id'].combine_first(pd.Series(new_order_ids))

        # For supplier_orders_data_df, handle supplier_purchase_order_id similarly
        num_missing_supplier = supplier_orders_data_df['supplier_purchase_order_id'].isna().sum()
        new_sup_ids = list(range(max_order_id + 1, max_order_id + 1 + num_missing_supplier))

        # Exclude empty items from new_sup_ids before combining
        if new_sup_ids:
            supplier_orders_data_df['supplier_purchase_order_id'] = supplier_orders_data_df['supplier_purchase_order_id'].combine_first(pd.Series(new_sup_ids))

        # Split data into 3 tables as before
        ## orders table
        order_df = main_orders_df[['order_id', 'customer_id', 'payment_id', 'employee_id', 'branch_id']]

        ## product_in_customers_order table
        product_in_customers_df = main_orders_df[['order_id', 'product_id', 'order_date', 'amount', 'quantities']]

        ## payments table
        payments_df = main_orders_df[['payment_id', 'payment_method', 'transaction_id', 'billing_address', 'billing_city', 'billing_country']]

        ############ END order_table #############

        ######### Supplier order ##########
        max_supplier_id = get_latest_id('supplier_purchase_order_id' , 'product_order')
        # Set default max_payment_id if None
        if max_supplier_id is None:
            max_supplier_id = 0

        # Check for missing payment_ids in the orders DataFrame
        num_missing = supplier_orders_data_df['supplier_purchase_order_id'].isna().sum()

        # Generate new payment IDs
        new_sup_ids = range(max_supplier_id + 1, max_supplier_id + 1 + num_missing)

        # Use combine_first to fill missing values in payment_id column
        supplier_orders_data_df['supplier_purchase_order_id'] = supplier_orders_data_df['supplier_purchase_order_id'].combine_first(pd.Series(new_sup_ids))

        products_in_supplier_orders = supplier_orders_data_df[['supplier_purchase_order_id','supplier_id','product_id','order_date','arrival_date','quantity','unit_price']]
        products_orders = supplier_orders_data_df[['supplier_purchase_order_id', 'employee_id', 'branch_id']]
    except Exception as e:
        print(f"Failed to transform raw data: {e}")
        logging.error(f"Failed to transform raw data: {e}")
        send_failed_email(recipients,"Failed to transform raw data.")
        raise
    # End time
    transfomed_data_end_time = time.time()
    transfomed_data_total_duration = transfomed_data_end_time - transfomed_data_start_time
    transfomed_data_minutes = int(transfomed_data_total_duration // 60)
    transfomed_data_seconds = int(transfomed_data_total_duration % 60)
    transfomed_data_milliseconds = int((transfomed_data_total_duration - int(transfomed_data_total_duration)) * 1000)

    print(f"END transforming data. Time taken:{transfomed_data_minutes} minutes, {transfomed_data_seconds} seconds, and {transfomed_data_milliseconds} milliseconds.")
    logging.info(f"END transforming data. Time taken:{transfomed_data_minutes} minutes, {transfomed_data_seconds} seconds, and {transfomed_data_milliseconds} milliseconds.")
    ######### END Supplier order ##########
    ################################################ END transformed Data ########################################

    ############################################## LOAD transformed data #####################################################
    print("Saving Transformed data...")
    logging.info("Saving Transformed data...")

    transform_file_path = r'C:\\supermarket\\transformed_data'
    # start time
    transformed_save_2places_upload_start_time = time.time()
    try:
        print(f"Saving Transformed data to {transform_file_path}")
        logging.info(f"Saving Transformed data to {transform_file_path}")

        # Save each DataFrame as a CSV file in the specified directory
        branches_df.to_csv(f'{transform_file_path}\\transformed_branch_{record_date}.csv', index=False)
        customers_df.to_csv(f'{transform_file_path}\\transformed_customer_{record_date}.csv', index=False)
        employees_df.to_csv(f'{transform_file_path}\\transformed_employee_{record_date}.csv', index=False)
        inventory_df.to_csv(f'{transform_file_path}\\transformed_inventory_{record_date}.csv', index=False)
        suppliers_df.to_csv(f'{transform_file_path}\\transformed_supplier_{record_date}.csv', index=False)
        order_df.to_csv(f'{transform_file_path}\\transformed_order_{record_date}.csv', index=False)
        product_in_customers_df.to_csv(f'{transform_file_path}\\transformed_product_in_customer_{record_date}.csv', index=False)
        payments_df.to_csv(f'{transform_file_path}\\transformed_payment_{record_date}.csv', index=False)
        products_in_supplier_orders.to_csv(f'{transform_file_path}\\transformed_product_in_supplier_order_{record_date}.csv', index=False)
        product_df.to_csv(f'{transform_file_path}\\transformed_product_{record_date}.csv', index=False)
        products_orders.to_csv(f'{transform_file_path}\\transformed_product_order_{record_date}.csv', index=False)
        print(f"Transformed data has been saved to {transform_file_path} successfully.")
        logging.info(f"Transformed data has been saved to {transform_file_path} successfully.")
    except Exception as e:
        print(f"Failed to save data in {transform_file_path}: {e}")
        logging.error(f"Failed to save data in {transform_file_path}: {e}")
        send_failed_email(recipients,f"Failed to save data in {transform_file_path}")
        raise
    print(f"END Saving Transformed data to {transform_file_path}'")
    logging.info(f"END Saving Transformed data to {transform_file_path}")
    ########### Google Drive ############

    ### Transformed Data Upload ###
    transformed_branches_csv = f'{transform_file_path}\\transformed_branch_{record_date}.csv'
    transformed_customers_csv = f'{transform_file_path}\\transformed_customer_{record_date}.csv'
    transformed_employees_csv = f'{transform_file_path}\\transformed_employee_{record_date}.csv'
    transformed_inventory_csv = f'{transform_file_path}\\transformed_inventory_{record_date}.csv'
    transformed_supplier_csv = f'{transform_file_path}\\transformed_supplier_{record_date}.csv'
    transformed_order_csv = f'{transform_file_path}\\transformed_order_{record_date}.csv'
    transformed_product_in_customer_csv = f'{transform_file_path}\\transformed_product_in_customer_{record_date}.csv'
    transformed_payment_csv = f'{transform_file_path}\\transformed_payment_{record_date}.csv'
    transformed_products_in_supplier_order_csv = f'{transform_file_path}\\transformed_product_in_supplier_order_{record_date}.csv'
    transformed_product_csv = f'{transform_file_path}\\transformed_product_{record_date}.csv'
    transformed_products_orders_csv = f'{transform_file_path}\\transformed_product_order_{record_date}.csv'



    try:
        print("Uploading transformed data files to Google Drive 'supermarket\\transformed_data'...")
        logging.info("Uploading transformed data files to Google Drive 'supermarket\\transformed_data'...")

        transformed_files = [
            transformed_branches_csv,
            transformed_customers_csv,
            transformed_employees_csv,
            transformed_inventory_csv,
            transformed_supplier_csv,
            transformed_order_csv,
            transformed_product_in_customer_csv,
            transformed_payment_csv,
            transformed_products_in_supplier_order_csv,
            transformed_product_csv,
            transformed_products_orders_csv
        ]

        # Upload each file and log the result
        for file in transformed_files:
            upload_file_to_drive(file, transform_backup_id)
            print(f"Successfully uploaded {file} on {record_date}")
            logging.info(f"Successfully uploaded {file} on {record_date}")

        print("All transformed data files uploaded to Google Drive 'supermarket\\transformed_data' successfully.")
        logging.info("All transformed data files uploaded to Google Drive 'supermarket\\transformed_data' successfully.")
    except Exception as e:
        print(f"Failed to upload transformed data files: {e}")
        logging.error(f"Failed to upload transformed data files: {e}")
        send_failed_email(recipients,"Failed to upload transformed data files")
        raise
    # end time
    transformed_save_2places_upload_end_time = time.time()
    transformed_save_2places_upload_total_duration = transformed_save_2places_upload_end_time - transformed_save_2places_upload_start_time
    transformed_save_2places_upload_minutes = int(transformed_save_2places_upload_total_duration // 60)
    transformed_save_2places_upload_seconds = int(transformed_save_2places_upload_total_duration % 60)
    transformed_save_2places_upload_milliseconds = int((transformed_save_2places_upload_total_duration - int(transformed_save_2places_upload_total_duration)) * 1000)
    print(f"END Saving Transformed data. Time taken:{transformed_save_2places_upload_minutes} minutes, {transformed_save_2places_upload_seconds} seconds, and {transformed_save_2places_upload_milliseconds} milliseconds.")
    logging.info(f"END Saving Transformed data. Time Taken:{transformed_save_2places_upload_minutes} minutes, {transformed_save_2places_upload_seconds} seconds, and {transformed_save_2places_upload_milliseconds} milliseconds.")

    ############################################## END LOAD transformed data #####################################################

    ############################################ Load dataframes to database ######################################################
    print("Loading Transformed data to 'supermarket' database...")
    logging.info("Loading Transformed data to 'supermarket' database...")

    # start time
    append_to_db_start_time = time.time()

    try:
        dataframes_to_append = [
            (branches_df, 'branch'),
            (suppliers_df, 'supplier'),
            (customers_df, 'customer'),
            (employees_df, 'employee'),
            (payments_df, 'payment'),
            (products_df, 'product'),
            (order_df, 'order'),
            (inventory_df, 'inventory'),
            (product_in_customers_df, 'product_in_customer_order'),
            (products_orders, 'product_order'),
            (products_in_supplier_orders, 'product_in_supplier_order')
        ]
        config = get_db_config("mysql_db_acc_detail.json")
        host=config['host']
        database=config['database']
        user=config['user']
        password=config['password']

        # Loop through the list and append each DataFrame to the corresponding table
        for df, table_name in dataframes_to_append:
            append_dataframe_to_mysql(df, table_name, host, database, user, password)
            # Print and log messages without showing the DataFrame
            print(f"Successfully uploaded data to '{table_name}' table in 'supermarket' database on {record_date}.")
            logging.info(f"Successfully uploaded data to '{table_name}' table in 'supermarket' database on {record_date}.")

    except Exception as e:
        print(f"Failed to upload transformed data to 'supermarket' database on {record_date}: {e}")
        logging.error(f"Failed to upload transformed data to 'supermarket' database on {record_date}: {e}")
        send_failed_email(recipients,f"Failed to upload transformed data to 'supermarket' database on {record_date}")
        raise

    # end time
    append_to_db_end_time = time.time()
    append_to_db_total_duration = append_to_db_end_time - append_to_db_start_time
    append_to_db_minutes = int(append_to_db_total_duration // 60)
    append_to_db_seconds = int(append_to_db_total_duration % 60)
    append_to_db_milliseconds = int((append_to_db_total_duration - int(append_to_db_total_duration)) * 1000)


    print(f"END Loading Transformed data to 'supermarket' database. Time taken: {append_to_db_minutes} minutes, {append_to_db_seconds} seconds, and {append_to_db_milliseconds} milliseconds.")
    logging.info(f"END Loading Transformed data to 'supermarket' database. Time taken: {append_to_db_minutes} minutes, {append_to_db_seconds} seconds, and {append_to_db_milliseconds} milliseconds.")
    ############################################ END LOAD dataframes to database ######################################################

    etl_end_time = time.time()

    etl_total_duration = etl_end_time - etl_start_time

    # Format the duration into minutes, seconds, and milliseconds
    etl_minutes = int(etl_total_duration // 60)
    etl_seconds = int(etl_total_duration % 60)
    etl_milliseconds = int((etl_total_duration - int(etl_total_duration)) * 1000)

    ### Send email for ELT completion ###
    send_success_email(recipients,etl_minutes,etl_seconds)
    print(f"END ELT process on {record_date}. Time taken: {etl_minutes} minutes, {etl_seconds} seconds, and {etl_milliseconds} milliseconds.")
    logging.info(f"END ELT process on {record_date}. Time taken: {etl_minutes} minutes, {etl_seconds} seconds, and {etl_milliseconds} milliseconds.")

# backup eltl log every 7 days
try:
    # Get today's date
    today = datetime.datetime.today().day

    # Run backup if today is 7, 14, 21, or 28
    if today in {7, 14, 21, 28}:
        print("Updating Log file to Google Drive...")
        logging.info("Updating Log file to Google Drive...")

        etl_log_file = r'C:\supermarket\log\ELT_log.txt'
        upload_file_to_drive(etl_log_file, log_backup_id)

        print("Successfully updated backup ELT log file to Google Drive.")
        logging.info("Successfully updated backup ELT log file to Google Drive.")
    else:
        print("Backup not scheduled for today.")

except Exception as e:
    print("Failed to update backup ELT log file to Google Drive.")
    logging.error("Failed to update backup ELT log file to Google Drive.")
    send_failed_email(recipients, "Failed to update backup ELT log file to Google Drive")
    raise