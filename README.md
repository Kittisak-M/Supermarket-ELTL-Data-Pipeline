# Supermarket ELTL pipeline
### Data Pipeline Architecture
![supermarket_pipeline_architecture](https://github.com/user-attachments/assets/1c07deff-1a9d-4ad1-90d7-da5eda1d20b8)

## Overview

This project automates the data pipeline for a supermarket database created using Python, enabling data storage, backup, logging, and notifications. The pipeline utilizes MySQL, Python, and Google Drive, which serves as a data lake, storing data both locally and in the cloud for redundancy. ELTL (Extract, Load, Transform, and Log) processes and SQL database backups are scheduled via Windows Task Scheduler.

## Deployment
Windows Task Scheduler is used to automate the ELTL processes and database backups for the supermarket database.

## Project Contents

### Supermarket Database Schema
![supermarket_db_diagram](https://github.com/user-attachments/assets/9586407e-83af-4f2d-9552-ce491626b42c)

### 1. Data Generation and Storage
- **Local Storage**: Data is stored locally at `C:\supermarket`.
- **Cloud Storage**: Data is also stored on Google Drive, which serves as a data lake.

### 2. Database Schema Creation
- Uses Dbdiagram.io to design the database schema using dimensional modeling technique.

### 3. ELTL Process
- **Extract**: Generates mock data using Python.
- **Load Raw Data**: Saves raw data to `C:\supermarket\raw_data` and Google Drive.
- **Transform data**: Processes and saves transformed data to `C:\supermarket\transformed_data` and Google Drive.
- **Load transform data**: Load transform data to Local MySQL database.
  
Click [here](https://github.com/Kittisak-M/Supermarket_ELTL/blob/main/ELTL_script.py) to see the full ELTL code.
### 4. Database Backup
- **Local Backup**: Stores backup database by replace the old one with the new one at `C:\supermarket\backup`.
- **Google Drive Backup**: Upload the local database file located at `C:\supermarket\backup to Google Drive`.

### 5. Logging
- Logs all activities locally in `C:\supermarket\log`. The log file is uploaed for backup to Google Drive weekly.

### 6. Email Notification
- Sends daily email notifications to relevant team members on the status of the ELTL process, including success, failure, error tracking, and runtime performance metrics.

## Prerequisites

Ensure the following software is installed:

- **MySQL**
- **Python** 
- **VS Code**
- **Google Drive**

**Deployment**: Windows Task Scheduler is used to automate ELTL processes and database backup.

## MySQL Setup

1. Install MySQL.
2. Change the details in a JSON file named `mysql_db_acc_detail.json` in the folder to store the database access details in the following format:

   ```json
   {
      "host": "your_host",
      "user": "your_user",
      "password": "your_password",
      "database": "supermarket_db"
   }
## Creating an App Password for Sending Emails

To create an app password for sending emails using Gmail, follow these steps:

### Enable 2-Step Verification

1. Go to your Google Account.
2. Select **Security**.
3. Under "Signing in to Google," select **2-Step Verification** and follow the instructions to enable it.

### Create an App Password for sending E

1. Once 2-Step Verification is enabled, go back to the **Security** section.
2. Under "Signing in to Google," select **App Passwords**.
3. You may need to sign in again.
4. Under "Select app," choose **Mail**.
5. Under "Select device," choose the device you are using or select **Other (Custom name)** to name it.
6. Click **Generate**.
7. Copy the generated app password (16-character code) for use in your application.

## Setting Up Google Drive API for backup database, store log files and store raw and tranformed data

To set up the Google Drive API, follow these steps:

### Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on **Select a project** and then **New Project**.
3. Enter a project name and click **Create**.

### Enable Google Drive API
![Enable google_drive_api](https://github.com/user-attachments/assets/ef0d834a-d03c-4910-b490-8430bf6be349)
1. In the dashboard, click on **Library**.
2. Search for "Google Drive API" and select it.
3. Click on the **Enable** button.

### Create Credentials
![Get_google_drive_credential](https://github.com/user-attachments/assets/f05d1833-9132-4cd0-89b5-345643134547)
1. Go to the **Credentials** tab on the left.
2. Click on **Create Credentials** and select **OAuth client ID**.
3. Configure the consent screen as required.
4. Choose **Desktop app** as the application type and click **Create**.
5. Download the credentials file (`credentials.json`) and place it in your project folder.

