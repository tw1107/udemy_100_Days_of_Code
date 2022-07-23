import requests
from datetime import datetime, timedelta
import time
from os import listdir
from os.path import isfile, join
import os
import shutil


# Create one file list by the latest created date, then copy the file to a working folder for the files to validate
# After upload completed, delete the files in working folder
def create_validate_file_list():
    path = "/Users/a.b.wang/Desktop/CDC_API_Key/security/validate_files"
    validate_filenames = [f for f in listdir(f"{path}") if isfile(join(f"{path}", f))]
    return validate_filenames


def create_insert_file_list():
    path = "/Users/a.b.wang/Desktop/CDC_API_Key/security/upload_files"
    add_filenames = [f for f in listdir(f"{path}") if isfile(join(f"{path}", f))]
    return add_filenames



def generate_token_validation():
    headers = {
        'accept': 'application/json',
    }
    cert = {'cdph_california_cert.pem', 'cdph_california_key_decrypted.pem'}
    json_data = {
        'clientID': 'CAA-VALIDATE',
        'clientSecret': 'o%2bz3k3tVWESp7sCTZ4QSZA%3d%3d',
        'scopes': [
            'UPLOAD',
        ],
    }
    response = requests.post('https://covdch-api-stg.cdc.gov/v0/token/gen', headers=headers, json=json_data, cert=cert)
    json_data = response.json()
    token_validate = json_data['token']
    return token_validate

def generate_token_insert():
    headers = {
        'accept': 'application/json',
    }
    cert = ('cdph_california_cert.pem', 'cdph_california_key_decrypted.pem')
    json_data = {
        'clientID': 'CAA-INTERNAL',
        'clientSecret': 'o%2bz3k3tVWESp7sCTZ4QSZA%3d%3d',
        'scopes': [
            'UPLOAD',
        ],
    }
    response = requests.post('https://covdch-api-stg.cdc.gov/v0/token/gen', headers=headers, json=json_data, cert=cert)
    json_data = response.json()
    token_insert = json_data['token']
    return token_insert



def validata_file():
    token = generate_token_validation()
    token_creation_time = time.time()
    validate_folder_path = "/Users/a.b.wang/Desktop/CDC_API_Key/security/validate_files"
    upload_folder_path = "/Users/a.b.wang/Desktop/CDC_API_Key/security/upload_files"
    headers = {
        'accept': 'application/json',
        'Authorization': f"{token}",
        'Content-Type': 'text/plain',
    }
    cert = ('cdph_california_cert.pem', 'cdph_california_key_decrypted.pem')

    # Validate each file
    for filenames in create_validate_file_list():
        with open(f"/Users/a.b.wang/Desktop/CDC_API_Key/security/validate_files/{filenames}", 'rb') as f:
            data = f.read()
        response = requests.post('https://covdch-api-stg.cdc.gov/v0/upload/cvrs/batch', headers=headers, data=data, cert=cert)

        # If processed successfully, move the files to upload folder
        if response.status_code == 200:

            shutil.move(f"{validate_folder_path}/" + filenames, upload_folder_path)
            print(f"Filename: {filenames} validation succeed, moved to the upload folder.")
        else:
            print(f"Filename: {filenames} validation failed. Response Status <{response.status_code}>. Please check the logs folder for details.")

        # Create log response
        with open(f"/Users/a.b.wang/Desktop/CDC_API_Key/security/logs/{filenames}_log_response.txt", 'wb') as f:
            f.write(response.content)

    return token_creation_time


def insert_file():
    token = generate_token_insert()
    insert_token_st = time.time()
    headers = {
        'accept': 'application/json',
        'Authorization': f"{token}",
        'Content-Type': 'text/plain',
    }
    cert = ('cdph_california_cert.pem', 'cdph_california_key_decrypted.pem')

    for filenames in create_insert_file_list():
        with open(f"/Users/a.b.wang/Desktop/CDC_API_Key/security/upload_files/{filenames}", 'rb') as f:
            data = f.read()
        response = requests.post('https://covdch-api-stg.cdc.gov/v0/upload/cvrs/batch', headers=headers, data=data, cert=cert)

        # Create log response
        with open(f"/Users/a.b.wang/Desktop/CDC_API_Key/security/logs/upload/{filenames}_log_response.txt", 'wb') as f:
            f.write(response.content)

    return insert_token_st



validation_continue = True
insert_continue = True

while validation_continue:
    validation_token_st = validata_file()
    et = time.time()
    elapsed_time = et - validation_token_st
    print('Validation Completed. Execution time:', elapsed_time, 'seconds')

    if elapsed_time >= 600:
         validation_continue = True
    else:
        validation_continue = False


while insert_continue:
    insert_token_st = insert_file()
    et = time.time()
    elapsed_time = et - insert_token_st
    print('Insert Completed. Execution time:', elapsed_time, 'seconds')

    if elapsed_time >= 600:
        insert_continue = True
    else:
        insert_continue = False



