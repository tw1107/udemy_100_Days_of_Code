
#################### Requirements #################### 
# 1. This script is to submit data to the COVID-19 Data Clearinghouse (DCH) 
#    through the DCH Application Programming Interface (API) using cURL.
#
# 2. This script will refresh every 10 mins to regenerate a new token 
#     as the token will be valid for 15 mins.
#
# 3. If the script fails inbetween this script will restart from the failed point. 
#    It will only process the remaining files.
#
# 4. Logs from each file process is stored under log folder. 
#    Optional: Script execution log is also stored under the log folder.
#
# 5. The script need three arguments Client id, Scope and <email list>
#    Client_id will be CAA_INTERNAL or CAA_VALIDATE
#    Scope will be UPLOAD 
#    Example for calling the script: <script name> CAA-VALIDATE UPLOAD ops
#
# Important Note : 
# 1. This script needs security certificate and secrect key so don't upload it to git or any sort of versioning tools.
# 2. Data file: for 'UPLOAD', each data file should be within 200K including header.
#
#########################################################

# 1. generate token


# give us error status
token.raise_for_status()
print(token)

# 3. Create the file list from the source data folder.
#    If the prior job failed in between then it will process the remaining files

# 4. Processing each files for validation/insert

# 5. Check if the files has been process successfully or not. If not stop the process

# 6. print response 

# 7. Regenerate the token every 10 mins 
while True:
    time.sleep(600)



curl --cert cdph_california_cert.pem --key cdph_california_key_decrypted.pem -X POST "https://covdch-api.cdc.gov/v0/token/gen" -H "accept:application/json" -H "Content-Type:application/json" -d"{\"clientID\":\"CAA-VALIDATE\",\"clientSecret\":\"o%2bz3k3tVWESp7sCTZ4QSZA%3d%3d\",\"scopes\":[\"UPLOAD\"]}"


curl --cert ${CLIENT_CERT} --key ${CLIENT_KEY} -X ${REQUEST_TYPE} "${PROCESS_URL}" -H "accept: application/json" -H "Authorization: ${TOKEN_RESP} " -H"Content-Type: text/plain" --data-binary @"${SOURCE_DIR}/${FILE_NAME}" -o ${LOG_DIR}/${CLIENT_ID}/${SCOPE}'_'${FILE_NAME}'.log'

curl --cert cdph_california_cert.pem --key cdph_california_key_decrypted.pem -X POST "https://covdch-api.cdc.gov/v0/upload/cvrs/batch" -H "accept: application/json" -H "Authorization: ${TOKEN_RESP}" -H "Content-Type: text/plain" --data-binary @"/Users/a.b.wang/Desktop/CDC_API_Key/security/CDC_CAA_TEST.txt" -o "/Users/a.b.wang/Desktop/CDC_API_Key/security/logs/log_response.txt"


curl --cert cdph_california_cert.pem --key cdph_california_key_decrypted.pem -X POST "https://covdch-api-stg.cdc.gov/v0/token/gen" -H "accept:application/json" -H "Content-Type:application/json" -d"{\"clientID\":\"CAA-VALIDATE\",\"clientSecret\":\"o%2bz3k3tVWESp7sCTZ4QSZA%3d%3d\",\"scopes\":[\"UPLOAD\"]}"





curl --cert cdph_california_cert.pem --key cdph_california_key_decrypted.pem -X POST "https://covdch-api.cdc.gov/v0/upload/cvrs/batch" -H "accept: application/json" -H "Authorization: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDQUEtVkFMSURBVEUiLCJpYXQiOjE2NTU3NTQ0NTcsImV4cCI6MTY1NTc1NTM1NywiY29uZmlnIjp7InNvdXJjZSI6IkNBQS1WQUxJREFURSIsImV2ZW50IjoidmFjY2FkbWluIiwianVyaXNkaWN0aW9uIjoiQ0FBIiwic2NvcGVzIjpbIlVQTE9BRCJdLCJwdWJsaWNLZXkiOiItLS0tLUJFR0lOIENFUlRJRklDQVRFLS0tLS1cclxuTUlJRnJUQ0NCSldnQXdJQkFnSVFCSjlOa0FsbVlWVTBYWFNlczl4S3F6QU5CZ2txaGtpRzl3MEJBUXNGQURCbFxyXG5NUXN3Q1FZRFZRUUdFd0pWVXpFVk1CTUdBMVVFQ2hNTVJHbG5hVU5sY25RZ1NXNWpNUmt3RndZRFZRUUxFeEIzXHJcbmQzY3VaR2xuYVdObGNuUXVZMjl0TVNRd0lnWURWUVFERXh0RWFXZHBRMlZ5ZENCVFNFRXlJRUZ6YzNWeVpXUWdcclxuU1VRZ1EwRXdIaGNOTWpFeE1qQXpNREF3TURBd1doY05NalF4TWpBeU1qTTFPVFU1V2pDQnl6RUxNQWtHQTFVRVxyXG5CaE1DVlZNeEZ6QVZCZ05WQkFnVERrNXZjblJvSUVOaGNtOXNhVzVoTVE4d0RRWURWUVFIRXdaRWRYSm9ZVzB4XHJcbk16QXhCZ05WQkFvVEtrTmxiblJsY25NZ1ptOXlJRVJwYzJWaGMyVWdRMjl1ZEhKdmJDQmhibVFnVUhKbGRtVnVcclxuZEdsdmJqRVlNQllHQTFVRUN4TVBSRVJKUkM5T1EwbFNSQ2hXVkVZcE1SZ3dGZ1lEVlFRREV3OURSRkJJSUVOaFxyXG5iR2xtYjNKdWFXRXhLVEFuQmdrcWhraUc5dzBCQ1FFV0drMXBZMmhoWld3dVVHOTNaV3hzUUdOa2NHZ3VZMkV1XHJcbloyOTJNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTJkTVQxZlE2UEZNTWlHWXlcclxuaXJVeEJzTEl2N2xIVEpsMktRSndqTHRrQ0NJUEFreHY0UW5mbWRlVTByckRBYWc4UElOaUVWS1RjQ29wQ3hhd1xyXG5PVEFFR0RwQy9qWlZzY3VUVmRMcDNQS04xWkxJRU9DSEZrcWw4SDJhT2hjYkxkTjJSbzN0UjU3NVpsckxwOHN0XHJcbndpT3JzSElRU1NGcGliZDFPMDNqckVnbVhDSHlGZGlTbG02cnVVLy9XbzE5YlFFYXkxbWhCODErbkFlYTFsU1dcclxuMkpiN0FzQUtwdXdwY2ZVRjAvajg4cXhGMXdTYlVxZURHWjRsd25lOUNUS2xmcDhhWmtBUUVpcFQzT2hCY2piSVxyXG5VR1JVNjhFUm10Sk91NE5wQkFuRkR5eFphTDdhOFdlWGlEcTJaVWZOMGg3NG51eGx2bGs0T3EzZUlrY2VMcUtyXHJcbkVaS2NsUUlEQVFBQm80SUI4RENDQWV3d0h3WURWUjBqQkJnd0ZvQVU1d0lqZ0FCUDJOZThsQXZaUDNRNVNUSThcclxuaW5rd0hRWURWUjBPQkJZRUZKWlIvTUlPZ3I0Zm5CNHJjK2QvbjRGcWxuMGlNQXdHQTFVZEV3RUIvd1FDTUFBd1xyXG5KUVlEVlIwUkJCNHdISUVhVFdsamFHRmxiQzVRYjNkbGJHeEFZMlJ3YUM1allTNW5iM1l3RGdZRFZSMFBBUUgvXHJcbkJBUURBZ1dnTUIwR0ExVWRKUVFXTUJRR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREJEQkRCZ05WSFNBRVBEQTZcclxuTURnR0NtQ0dTQUdHL1d3RUFRSXdLakFvQmdnckJnRUZCUWNDQVJZY2FIUjBjSE02THk5M2QzY3VaR2xuYVdObFxyXG5jblF1WTI5dEwwTlFVekNCaFFZRFZSMGZCSDR3ZkRBOG9EcWdPSVkyYUhSMGNEb3ZMMk55YkRNdVpHbG5hV05sXHJcbmNuUXVZMjl0TDBScFoybERaWEowVTBoQk1rRnpjM1Z5WldSSlJFTkJMVEV1WTNKc01EeWdPcUE0aGpab2RIUndcclxuT2k4dlkzSnNOQzVrYVdkcFkyVnlkQzVqYjIwdlJHbG5hVU5sY25SVFNFRXlRWE56ZFhKbFpFbEVRMEV0TVM1alxyXG5jbXd3ZVFZSUt3WUJCUVVIQVFFRWJUQnJNQ1FHQ0NzR0FRVUZCekFCaGhob2RIUndPaTh2YjJOemNDNWthV2RwXHJcblkyVnlkQzVqYjIwd1F3WUlLd1lCQlFVSE1BS0dOMmgwZEhBNkx5OWpZV05sY25SekxtUnBaMmxqWlhKMExtTnZcclxuYlM5RWFXZHBRMlZ5ZEZOSVFUSkJjM04xY21Wa1NVUkRRUzVqY25Rd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQlxyXG5BSTRKUzZTeGhVQlgxNlMwa2Q2VFE5NG1NNjd1ZGdRNzl5Tk90emp3ZlpyOGxHS2pSbjE4UGNBL3lNWkZJUmRmXHJcbk1icUtFa0RDb2c5NVBlRDhYM1JqZ1l2OW1vSW93ZGVBRnNHUStwaEhCTE5LZWlPSzc5YkE4aWFLN0l4Vkx0YkZcclxuM01JM2tnOXFTOUtrbHBGS3NqUmN3RTNhSlY5cjNRNGlOdWJsRHp1a1VtcmNJQWxWTHVhcXZ2bGR4c2U2RVBqYlxyXG4vbmN1VXhDN3FZTG5RY3JwdVZGNjlobndiV2QzR1pQV3BaVlh2a0JWR2JPV1EweVQ0cHkrLy9DdmRDSTd3NXgzXHJcbmM0OVVza0xDUEViK3lmVDF4QVR0YTgrazdKdExWRW9qOTZWMXpYWVl0Y25KbGFPUlJLdHFLTTZnbE8rUWpXb1RcclxuYWVZWWYwNGpyZWg3R1ZVZStjTDFHbTg9XHJcbi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS1cclxuIiwicmVxdWVzdGluZ0NsaWVudElkIjpudWxsLCJ3cml0ZU9iamVjdFN0b3JhZ2UiOmZhbHNlLCJ3cml0ZVJlZGFjdGVkRGF0YSI6ZmFsc2UsIndyaXRlTm9uUmVkYWN0ZWREYXRhIjpmYWxzZSwidmFsaWRhdGVPbmx5Ijp0cnVlfX0.UDjwVs3ov9SpHcaTjud_mftvFrd7Ehn7lQqyGn75EnfQXY8CxyTvBjjNSc0xD_-peU2trz3j4kzhBYuPW1dRFQ" -H "Content-Type: text/plain" --data-binary @"/Users/a.b.wang/Desktop/CDC_API_Key/security/CDC_CAA_TEST.txt" -o "/Users/a.b.wang/Desktop/CDC_API_Key/security/logs/log_response.txt"