import requests
import os

proxies = {
"http": os.environ['QUOTAGUARDSHIELD_URL'],
"https": os.environ['QUOTAGUARDSHIELD_URL']
}

res = requests.get("https://www.google.com/", proxies=proxies)
print(res.text)
