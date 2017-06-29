import requests
from bs4 import BeautifulSoup
import sys

board = input('Input the board name:> ')
url = "https://www.ptt.cc/bbs/{}/index.html".format(board)
re = requests.get(url)

soup = BeautifulSoup(re.text.encode('utf-8'), "html.parser")

for line in soup.select('.r-ent'):
    print ("日期:", line.select('.date')[0].text)
    print ("作者:", line.select('.author')[0].text)
    print ("標題:", line.select('.title')[0].text)
    print ("看板名稱:", board)
    r = requests.get("https://www.ptt.cc"+line.a['href'])
    soupcontennt = BeautifulSoup(r.text.encode('utf-8'), "html.parser")
    text = soupcontennt.select('#main-container')[0].get_text()
    text = text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    text = text.split("\n--\n")[0]
    print ("內文:",text)
    print()