
# import urllib.request


# urllib.request.urlretrieve("https://imdb-video.media-imdb.com/vi4172269849/1434659529640-260ouz-1731422693951.mp4?Expires=1735319777\u0026Signature=LpLNVjBZB0Cb0f4KvwDaWwVmcZBZBBbe1eYTr8PrsRueL7kF36gFPFr9P0BsLxFLctiXV-kf4C8ybq-HhaTVfLhvBmEoGYtkHpxX~0HmB7ZqZyVbM~JQnhws1bHJmAALxCnMu7gLuKF6eX4lSvRZVlKjP34Kt~lNihcjeQFtKMgUaF50qUfFSOsbo9xZNqUzoN8aQ5YGNnAD9~SB1MFLC1vxqkLCy7NFuV~AcEXY9egUt0qCtrbIeQ8IACi3w84d1R0K6wIBWnHT~WesKSftMPlfTzNdvwP9DZ0HDlRDme2VW5XSrfC68VndSLf-Cf-vmW5WoVlIYb4dc2hx1cL42Q__\u0026Key-Pair-Id=APKAIFLZBVQZ24NQH3KA", 
# "5.mp4")


import json
from minio import Minio
import urllib.request
import os
import datetime

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


url = client.get_presigned_url("GET", bucket_name, "5.mp4", expires=datetime.timedelta(hours=2))
print("View URL for image.jpg:", url)