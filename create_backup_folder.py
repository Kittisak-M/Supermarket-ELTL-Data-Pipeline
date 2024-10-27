from __future__ import print_function
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path
import logging

###### Create local PC folders ######
folder_path = Path(r'C:\supermarket')
folder_path.mkdir(parents=True, exist_ok=True)
print(f"Folder 'supermarket' created at {folder_path}")

# Subfolders
subfolder_paths = {
    'raw_data': Path(r'C:\supermarket\raw_data'),
    'transformed_data': Path(r'C:\supermarket\transformed_data'),
    'db_backup': Path(r'C:\supermarket\db_backup'),
    'log': Path(r'C:\supermarket\log')
}

for name, path in subfolder_paths.items():
    path.mkdir(parents=True, exist_ok=True)
    print(f"Folder created at {path}")

###### Create backup folders in Google Drive ######
CREDENTIALS_FILE = os.path.join(os.getcwd(), 'google_drive_api_credential.json')
SCOPES = ['https://www.googleapis.com/auth/drive.file']
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# Function to create a folder in Google Drive
def create_folder(folder_name, parent_folder_id=None):
    file_metadata = {'name': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]
    
    folder = service.files().create(body=file_metadata, fields='id').execute()
    print(f'Folder "{folder_name}" created with ID: {folder.get("id")}')
    return folder.get("id")

# Function to get folder ID in Google Drive
def get_folder_id(folder_name, parent_folder_id=None):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    if parent_folder_id:
        query += f" and '{parent_folder_id}' in parents"
    
    try:
        results = service.files().list(q=query, fields="files(id)").execute()
        items = results.get('files', [])
        if items:
            return items[0]['id']
        else:
            print(f'No folder found with the name "{folder_name}".')
            return None
    except Exception as error:
        print(f'An error occurred: {error}')
        return None

# Configure logging
log_directory = subfolder_paths['log']
log_file_path = log_directory / 'activity_log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Log function
def log_message(message):
    logging.info(message)
    print(message)

log_message("Creating local backup folders...")
for name, path in subfolder_paths.items():
    log_message(f"Folder created at {path}")

try:
    # Check if 'supermarket' folder exists in Google Drive
    supermarket_folder_id = get_folder_id('supermarket', parent_folder_id='1pg99tJ7dIaPyEb8vS9VvWTxgHGzk-BD3')
    
    if supermarket_folder_id:
        log_message(f"Folder 'supermarket' already exists in Google Drive with ID: {supermarket_folder_id}")
    else:
        # Create 'supermarket' folder if it doesn't exist
        supermarket_folder_id = create_folder('supermarket', parent_folder_id='1pg99tJ7dIaPyEb8vS9VvWTxgHGzk-BD3')
        log_message(f"Created folder 'supermarket' in Google Drive with ID: {supermarket_folder_id}")
    
    # Get 'supermarket' folder ID
    parent_folder_id = get_folder_id('supermarket')

    # Create subfolders inside 'supermarket' in Google Drive
    if parent_folder_id:
        for name in subfolder_paths.keys():
            subfolder_id = get_folder_id(name, parent_folder_id=parent_folder_id)
            if subfolder_id:
                log_message(f"Folder '{name}' already exists inside 'supermarket' with ID: {subfolder_id}")
            else:
                subfolder_id = create_folder(name, parent_folder_id=parent_folder_id)
                log_message(f"Created folder '{name}' in Google Drive inside 'supermarket' with ID: {subfolder_id}")

    log_message("Backup folders checked/created in Google Drive successfully.")

except Exception as e:
    log_message(f"An error occurred while creating folders: {e}")

# Function to check if a file exists in Google Drive
def get_file_id(file_name, parent_folder_id):
    query = f"name='{file_name}' and '{parent_folder_id}' in parents"
    try:
        results = service.files().list(q=query, fields="files(id)").execute()
        items = results.get('files', [])
        if items:
            return items[0]['id']
        else:
            log_message(f'No file found with the name "{file_name}".')
            return None
    except Exception as error:
        log_message(f'An error occurred: {error}')
        return None

# Upload the log file to Google Drive (create new or update existing)
def upload_log_to_drive(local_log_file_path, parent_folder_id):
    try:
        file_id = get_file_id(local_log_file_path.name, parent_folder_id)
        
        if file_id:
            # If file exists, update it with new content
            media = MediaFileUpload(str(local_log_file_path), mimetype='text/plain')
            updated_file = service.files().update(fileId=file_id, media_body=media).execute()
            log_message(f'Log file "{local_log_file_path.name}" updated on Google Drive with ID: {updated_file.get("id")}')
        else:
            # If file doesn't exist, upload a new one
            file_metadata = {'name': local_log_file_path.name, 'parents': [parent_folder_id]}
            media = MediaFileUpload(str(local_log_file_path), mimetype='text/plain')
            new_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            log_message(f'Log file "{local_log_file_path.name}" uploaded to Google Drive with ID: {new_file.get("id")}')
    except Exception as e:
        log_message(f"An error occurred while uploading the log file to Google Drive: {e}")

# Get the parent folder ID for the "log" subfolder in Google Drive
log_parent_folder_id = get_folder_id('log', parent_folder_id=parent_folder_id)

# Upload the log file if the 'log' folder exists
if log_parent_folder_id:
    upload_log_to_drive(log_file_path, log_parent_folder_id)
else:
    log_message("Failed to retrieve the 'log' folder ID for uploading the log file.")

