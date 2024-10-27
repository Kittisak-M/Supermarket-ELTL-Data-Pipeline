#!/bin/bash

## 1. Create Database
## 2. Create backup folder
## 3. ELTL process
#### CREATE DATABASE ####
script_dir=$(dirname "$0")
echo "Creating database in MySQL..."
python "$script_dir/database_creation_script.py"


if [ $? -eq 0 ]; then
    echo "Database creation successful."
else
    echo "Database creation failed."
    exit 1  #
fi
#########################

###### CREATE BACKUP FOLDER ######
echo "Creating Backup folder in 'drive C:' and Google Drive"
python "$script_dir/back_up_folder_generation.py"

if [ $? -eq 0 ]; then
    echo "Backup folder created successfully."
else
    echo "Failed to create backup folder."
    exit 1  
fi
#########################


####### ETLT process ############
echo "Running ETLT for mock data..."
python "$script_dir/ETLT_script.py"
if [ $? -eq 0 ]; then
    echo "ETLT for mock data completed successfully."
else
    echo "ETLT for mock data failed."
    exit 1 
fi
#########################

# Final message indicating all scripts have been executed
echo "All scripts have been executed successfully."
