#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level0.php'
mydata = {'id': 1802, 'holdthedoor': 'submit'}

for i in range(1024):
    x = requests.post(url, data = mydata)
    print(x)
