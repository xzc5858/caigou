# from pyquery import PyQuery as pq
# from bs4 import BeautifulSoup
import os
import sys
import requests
from bs4 import BeautifulSoup
import socket

scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
f = open(scriptPath + '/list.txt', 'a+', encoding="utf-8")

headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = "http://www.ccgp-shanxi.gov.cn/view.php?ntype=fnotice&nodeid=154"
data = {"title": "网络安全", "type": "全部", "local": "", "dqx": ""}
r = requests.post(url, data=data)
soup = BeautifulSoup(r.text, "html5lib")
print(soup.title.getText())
# print(soup.find_all("tr", class_="odd"));
for item in soup.find_all("tr", class_="odd"):
    # print(item)
    f.writelines(item.text + '\n')
    # socket.mysocket.url(item.)
    # ls=BeautifulSoup(item.text,"html5lib")
    a = item.a
    href = "http://www.ccgp-shanxi.gov.cn/" + a["href"]
    dz = requests.get(href)
    desoup = BeautifulSoup(dz.text, "html5lib")
    print(desoup.find_all("p",align="left"))
for item in soup.find_all("tr", class_="even"):
    # print(item)
    f.writelines(item.text + '\n')
f.close()
