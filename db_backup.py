

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
    subject = f"Supermarket Database Completion Report - {current_date}"
    body = f"""
    Hello Team,

    Supermarket Database was successfully completed today, {current_date}.
    The time taken for the database backup was {minute} minutes and {second} seconds.

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
    subject = f"Supermarket Database Failure Report - {current_date}!"
    body = f"""
    Hello Team,

    A failure was encountered while attempting to back up the Supermarket database on {current_date}.
    Error details: {error_message[:100]}.
    For immediate assistance, please contact [Name] at 097-xxxxxxx or via email at example@gmail.com.

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

# Set up logging
log_directory = r'C:\supermarket\log'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file = os.path.join(log_directory, 'backup_log.log')
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.file']


def load_db_credentials(json_path):
    """
    Load database credentials from a JSON file.
    :param json_path: The path to the JSON file containing the DB credentials.
    :return: A dictionary with the DB credentials.
    """
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise  # Raise the exception
    except json.JSONDecodeError:
        raise  # Raise the exception
    except Exception as e:
        raise  # Raise the exception
        raise  # Raise the exception after logging it

def backup_sql_database(credentials, backup_file_path):
    """
    Backup the SQL database to a file using credentials.
    :param credentials: A dictionary containing the DB credentials.
    :param backup_file_path: The relative path to store the backup file.
    """
    try:
        dump_command = f"mysqldump -h {credentials['host']} -u {credentials['user']} -p{credentials['password']} {credentials['database']} > {backup_file_path}"
        subprocess.run(dump_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        raise  # Raise the exception
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

def delete_all_files_in_directory(directory_path):
    """
    Delete all files in the specified directory.
    :param directory_path: The path to the directory from which files will be deleted.
    """
    # Get a list of all files in the directory
    files_in_directory = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Check if the directory has any files
    if not files_in_directory:
        print(f'No files in {directory_path} to be deleted.')
        logging.info(f'No files in {directory_path} to be deleted.')
    else:
        # Delete all files in the directory
        for filename in files_in_directory:
            file_path = os.path.join(directory_path, filename)
            os.remove(file_path)  # Delete the file
            logging.info(f'Deleted: {file_path}')
            print(f'Deleted: {file_path}')  #



def delete_all_files_in_folder(folder_id):
    """
    Delete all files in a Google Drive folder without deleting the folder itself.
    :param folder_id: The Google Drive folder ID.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Build the Google Drive API service
    try:
        drive_service = build('drive', 'v3', credentials=creds)
    except Exception as e:
        return

    # List all files in the specified folder
    query = f"'{folder_id}' in parents"
    try:
        results = drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])

        if not files:
            return

        # Delete each file
        for file in files:
            file_id = file['id']
            drive_service.files().delete(fileId=file_id).execute()

    except Exception as e:
        return

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
    subject = f"Supermarket Database Completion Report - {current_date}"
    body = f"""
    Hello Team,

    Supermarket Database was successfully completed today, {current_date}.
    The time taken for the database backup was {minute} minutes and {second} seconds.

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
    subject = f"Supermarket Database Failure Report - {current_date}!"
    body = f"""
    Hello Team,

    A failure was encountered while attempting to back up the Supermarket database on {current_date}.
    Error details: {error_message[:100]}.
    For immediate assistance, please contact [Name] at 097-xxxxxxx or via email at example@gmail.com.

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

if __name__ == '__main__':
    import time

    ## Time measure
    db_backup_start_time = time.time()

    # Set up logging
    logging.basicConfig(filename=r'C:\supermarket\log\backup_log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    ###### E-mail Config #####
    recipient = ["kittisak.maungmanee@gmail.com"]
    ##########################

    main_folder_id = "1pg99tJ7dIaPyEb8vS9VvWTxgHGzk-BD3"
    super_backup_id = get_folder_id_by_name("supermarket", main_folder_id)
    log_backup_id = get_folder_id_by_name("log", super_backup_id)
    raw_backup_id = get_folder_id_by_name("raw_data", super_backup_id)
    dbbackup_backup_id = get_folder_id_by_name("db_backup", super_backup_id)
    transform_backup_id = get_folder_id_by_name("transformed_data", super_backup_id)

    # Load the database credentials from the JSON file
    db_credentials_path = './mysql_db_acc_detail.json'
    credentials = load_db_credentials(db_credentials_path)

    # Create the backup file name with the desired format
    timestamp = datetime.now().strftime("%H.%M_%d-%m-%Y")  # Include seconds for uniqueness
    backup_file_name = f'supermarket_backup_{timestamp}.sql'
    db_backup_directory = r'C:\supermarket\db_backup'
    # Specify the backup file path
    local_backup = os.path.join(db_backup_directory, backup_file_name)

    # Check if dbbackup_backup_id was found
    if not dbbackup_backup_id:
        logging.error("The 'db_backup' folder was not found. Exiting the script.")
        print("Error: The 'db_backup' folder was not found. Exiting the script.")
        exit(1)

    ## Backup ##
    print(f'Back up supermarket Database on {datetime.today().strftime("%d-%m-%Y")}...')
    logging.info(f'Back up supermarket Database on {datetime.today().strftime("%d-%m-%Y")}...')

    #### Local Storage ####
    print(f"Backing up supermarket database to local storage '{db_backup_directory}'")
    logging.info(f"Backing up supermarket database to local storage '{db_backup_directory}'")

    # Delete old latest in 'C:\supermarket\db_backup'
    print(f"Deleting latest supermarket database in '{db_backup_directory}'")
    logging.info(f"Deleting latest supermarket database in '{db_backup_directory}'")

    try:
        delete_all_files_in_directory(db_backup_directory)
        print(f"Successfully delete the latest supermarket database backup file in '{db_backup_directory}'")
        logging.info(f"Successfully delete the latest supermarket database backup file in '{db_backup_directory}'")
    except Exception as e:
        print(f'Fail to delete the latest supermarket database backup file in {db_backup_directory}| ERROR: {e}')
        logging.error(f'Fail to delete the latest supermarket database backup file in {db_backup_directory}| ERROR: {e}')
        send_failed_email(recipient, f"f'Fail to delete the latest supermarket database backup file in {db_backup_directory} / Error: {e}" )
        raise

    # Backup
    try:
        backup_sql_database(credentials, local_backup)
        print(f"Successfully save supermarket database on {datetime.today().strftime("%d-%m-%Y")} in '{db_backup_directory}'")
        logging.info(f"Successfully save supermarket database on {datetime.today().strftime('%d-%m-%Y')} in '{db_backup_directory}'")
    except Exception as e:
        print(f'Fail to save file in {db_backup_directory}| ERROR: {e}')
        logging.error(f'Fail to save file in {db_backup_directory}| ERROR: {e}')
        send_failed_email(recipient, f"f'Fail to save file in {db_backup_directory} / Error: {e}" )
        raise


    #### Google Drive ####
    print('Backing up supermarket database to Google Drive...')
    logging.info('Backing up supermarket database to Google Drive...')

    # Delete file in Google Drive
    print(f'Deleting latest supermarket database in Google Drive / folder_id={dbbackup_backup_id}')
    logging.info(f'Deleting latest supermarket database in Google Drive / folder_id={dbbackup_backup_id}')

    try:
        delete_all_files_in_folder(dbbackup_backup_id)
        print(f'Successfully delete the latest supermarket database in Google Drive folder id = {dbbackup_backup_id}')
        logging.info(f'Successfully delete the latest supermarket database in Google Drive folder id = {dbbackup_backup_id}')
    except Exception as e:
        print(f"Failed to delete files in Google Drive / folder id = {dbbackup_backup_id} / error: {e}")
        logging.error(f"Failed to delete files in Google Drive / folder id = {dbbackup_backup_id} / error: {e}")
        send_failed_email(recipient, f"Failed to delete files in Google Drive / folder id = {dbbackup_backup_id} / error: {e}" )
        raise


    # Upload supermarket backup file
    try:
        upload_file_to_drive(local_backup, dbbackup_backup_id)
    except Exception as e:
        print(f"Failed to upload in Google Drive database on {datetime.today().strftime("%d-%m-%Y")} / folder id = {dbbackup_backup_id} / error: {e}")
        logging.error(f"Failed to upload in Google Drive database on {datetime.today().strftime('%d-%m-%Y')} / folder id = {dbbackup_backup_id} / error: {e}")
        send_failed_email(recipient, f"Failed to upload in Google Drive database on {datetime.today().strftime('%d-%m-%Y')} / folder id = {dbbackup_backup_id} / error: {e}" )
        raise

    print(f'Back up on {datetime.today().strftime("%d-%m-%Y")} is already done.')
    logging.info(f'Back up on {datetime.today().strftime("%d-%m-%Y")} is already done.')



    ### UPLOAD log file from local storage 'C:\supermarket\log' to Google Drive ###
    log_file_path = r'C:\supermarket\log\backup_log.log'
    if os.path.exists(log_file_path):
        upload_file_to_drive(log_file_path, log_backup_id)
        print('Successfully upload log file to Google Drive')
        logging.info('Successfully upload log file to Google Drive')
    else:
        print("Failed to upload log file to Google Drive: ", log_file_path)
        logging.error("Failed to upload log file to Google Drive: ", log_file_path)
        send_failed_email(recipient, f"Failed to upload log file to Google Drive: {log_file_path}" )
        raise

    db_backup_end_time = time.time()
    db_backup_total_duration = db_backup_end_time - db_backup_start_time
    db_backup_minutes = int(db_backup_total_duration // 60)
    db_backup_seconds = int(db_backup_total_duration % 60)
    db_backup_milliseconds = int((db_backup_total_duration - int(db_backup_total_duration)) * 1000)

    send_success_email(recipient, db_backup_minutes, db_backup_seconds)
    print("Supermarket database is already backup in google drive and local storage successfully.")
    logging.info("Supermarket database is already backup in google drive and local storage successfully.")

