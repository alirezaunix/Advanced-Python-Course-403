import requests
from bs4 import BeautifulSoup
url="https://www.python.org/"
resp=requests.get(url).text
bs=BeautifulSoup(resp,"html.parser")
results=bs.find_all("a")
for result in results:
    if 'downloads/release' in str(result):
        print(result)