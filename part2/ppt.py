import requests
from bs4 import BeautifulSoup

url = "http://www.ppt.com/gossip/index.html'
re=requests.get(url)

soup=BeautifulSoup(re.text.encode('utf-8'), "html.parser")

for line in soup.select('.r-ent'):
    print ('日期:', line.select('.date')[0].text)
    print ('作者:', line.select('.author')[0].text)
    print ('標題:', line.select('.title')[0].text)
    print ('看板名稱:', 'Gossip')
    print()
