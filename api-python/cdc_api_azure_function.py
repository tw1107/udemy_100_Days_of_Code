import logging
import requests
import azure.functions as func
import os
from datetime import datetime, timedelta
from azure.storage.blob import BlobClient, BlobServiceClient, ContainerClient
from azurebatchload import Utils

def create_validate_file_list():
    connect_str = os.getenv('BLOB_CONNECTION_STRING') 
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name=os.getenv('BLOB_CONTAINER_NAME')
    container_client=blob_service_client.get_container_client(container_name)
    
    blob_list = container_client.list_blobs()
    logging.info(f"This is blob_list: {container_client.list_blobs()}")
    for blob in blob_list:
        blobs_name = "\t" + blob.name
        logging.info(f"This is blob.name: {blobs_name}")
        blob_filename=blobs_name

    return blobs_name    

def generate_token_validation():
    headers = {
        'accept': 'application/json',
    }
    cert = ('cdph_california_cert.pem', 'cdph_california_key_decrypted.pem')
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
    logging.info(f"Token generated")
    #logging.info(f"Token: {token_validate}")
    return token_validate


def validate_file():
    token = generate_token_validation()
    headers = {
        'accept': 'application/json',
        'Authorization': f"{token}",
        'Content-Type': 'text/plain',
    }
    cert = ('cdph_california_cert.pem', 'cdph_california_key_decrypted.pem')

    logging.info(f"starting the file validation loop")
    filename=create_validate_file_list()
    for files in filename:
        logging.info(files)
        with open(f"{files}", 'rb') as f:
            data = f.read()
            logging.info(f"Read data: {data}")
            response = requests.post('https://covdch-api-stg.cdc.gov/v0/upload/cvrs/batch', headers=headers, data=data, cert=cert)
            logging.info(f"Response: {response}")
            logging.info(f"Response content: {response.content}")

    # Create log response
    # with open(f"/Users/a.b.wang/Desktop/CDC_API_Key/security/logs/{filenames}_log_response.txt", 'wb') as f:
    #     f.write(response.content)


def main(myblob: func.InputStream):

    # Blob Container Connection Details:
    conn_str     =  os.getenv('BLOB_CONNECTION_STRING') 
    container_name  =  os.getenv('BLOB_CONTAINER_NAME')
    logging.info(f"Reading connection string: {conn_str}")
    logging.info(f"Reading container name: {container_name}")

    # Establish connection to Azure Blob container:
    logging.info('Connecting to Blob container...')

    blob = BlobClient.from_connection_string(conn_str=conn_str, container_name=container_name, blob_name=myblob.name)
    logging.info('Connected to Blob container successfully!')

    # List files for validation
    #logging.info(f"List files for validation from container name: {container_name}")
    #create_validate_file_list()
    #logging.info('Finished listing.')
    

    ## Validate the files in Filelist
    logging.info('Validating files...')
    #validate_file()
    create_validate_file_list()
    logging.info('Finished validating files.')


    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    
    

