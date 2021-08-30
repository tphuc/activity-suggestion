import requests
import csv
import json
import time

url = "http://www.boredapi.com/api/activity?"

def collectData(amount=5000, interval=1,):
    f = csv.writer(open("test.csv", "a+"))
    for i in range(amount):
        time.sleep(interval)
        response = requests.get(url)
        res = response.json()
        print(i)
        f.writerow([res['key'], res["activity"], res["accessibility"], res["type"], res["participants"], res['price'], res['link']]) 


collectData()