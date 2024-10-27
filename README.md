# Supermarket Data Pipeline Automation

## Overview

This project automates the data pipeline for a supermarket database, data created using python, enabling data storage, backup, logging, and notifications. The pipeline utilizes MySQL, Python, and Google Drive, used as data lake, storing data both locally and on the cloud for redundancy. ELTL (Extract, Load, Transform, and Log) processes and SQL database backups are scheduled via Windows Task Scheduler.

## Deployment
   Windows task scheduler is used to automate the Extract, Load, Transform, and Load (ELTL) processes and database backup for supermarket database

## Project Contents

### 1. Data Pipeline Architecture
![Data Pipeline Architecture](./data_pipeline_architecture.png) <!-- Replace with your relative image path -->

1. **Data Generation and Storage**:
   - **Local Storage**: Data is stored locally at `C:\supermarket`.
   - **Cloud Storage**: Data is also stored on Google Drive, which serves as a data lake.

2. **Create Supermarket Database Schema**
   - use dbigram to create database
2. **ELTL Process**
   - Extract Data from mock data using python. 
   - Load Raw data to `C:\supermarket\raw_data` and Google Drive.
   - Transform Data and save to `C:\supermarket\transformed_data` and Google Drive.""
   - load
2. **Data Backup**:
   - **Local Backup**: Backups for both raw and transformed data are stored at `C:\supermarket\backup`.
   - **Google Drive Backup**: An additional layer of redundancy for both raw and transformed data backups.

3. **Logging**:
   - All activities are logged locally in `C:\supermarket\log` and on cloud using Google Drive.

4. **Database Backup**:
   - Daily MySQL database backups are saved in:
     - `C:\supermarket\backup`
     -  Google Drive
   - Only the latest version of backups is retained by deleting older backups.

5. **Email Notification**:
   - Sends a daily email notification to relevant team members with the ELTL process status, error tracking, and runtime performance metrics.


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

## Setting Up Google Drive API

To set up the Google Drive API, follow these steps:

### Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on **Select a project** and then **New Project**.
3. Enter a project name and click **Create**.

### Enable Google Drive API

1. In the dashboard, click on **Library**.
2. Search for "Google Drive API" and select it.
3. Click on the **Enable** button.

### Create Credentials

1. Go to the **Credentials** tab on the left.
2. Click on **Create Credentials** and select **OAuth client ID**.
3. Configure the consent screen as required.
4. Choose **Desktop app** as the application type and click **Create**.
5. Download the credentials file (`credentials.json`) and place it in your project folder.

