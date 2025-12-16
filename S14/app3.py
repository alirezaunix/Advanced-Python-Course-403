import requests
from lxml import etree
import time
url='https://www.tgju.org/profile/crypto-bitcoin'
while True:
    resp=requests.get(url).text
    tree=etree.HTML(resp)
    result=tree.xpath('/html/body/main/div[1]/div[1]/div[1]/div/div[2]/div/h3[1]/span[2]/span[1]')
    dollar=etree.tostring(result[0], encoding='unicode', method='text')
    print(dollar)
    
