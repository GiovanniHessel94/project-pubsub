import requests
import time

for i in range(0, 3):
    time.sleep(0.5)
    response = requests.get('http://127.0.0.1:5000')
    print(response.status_code)
