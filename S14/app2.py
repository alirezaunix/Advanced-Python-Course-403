import requests
from lxml import etree
import time
url="https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1"
while True:
    resp=requests.get(url).text
    tree=etree.HTML(resp)
    result=tree.xpath('/html/body/main/div/div[3]/div[1]/div/div/div[1]/table/tbody/tr[1]')
    dollar=etree.tostring(result[0], encoding='unicode', method='text').splitlines()[2].replace("\t","")
    print(dollar)
    time.sleep(10)
