import json
from minio import Minio
import urllib.request
import os

directory = 'films'

with open('credentials.json') as file:
    data = json.load(file)

url = data['url']
# accessKey = data['accessKey']
# secretKey = data['secretKey']

accessKey = "minioadmin"
secretKey = "minioadmin"

client = Minio(url, access_key=accessKey, secret_key=secretKey, secure=False)

# source_file = './test.txt'

bucket_name = "python-test-bucket"
source_file = ''

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        source_file = f
        print(f)
    destination_file = filename

    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    client.fput_object(
        bucket_name, destination_file, source_file,
    )

