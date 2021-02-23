import plug
from detail import detail
import myos
import re

isGet = False
headers = {
    "User-Agent": "Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url = "http://www.ccgp-shanxi.gov.cn/view.php?ntype=fnotice&nodeid=154"
data = {"title": "大同", "type": "全部", "local": "", "dqx": ""}
soup = plug.request_soup(url, isGet, data)


def turn_page(thissoup):
    items = thissoup.find('div', class_="pager").find_all('a')
    for item in items:
        st = re.match('^后一页.*', item.text.strip())
        # print(st)
        if st != None:
            url = "http://www.ccgp-shanxi.gov.cn/" + item['href']
            soup = plug.request_soup(url, True, None)
    return soup


def get_page(thissoup):
    items = thissoup.find('div', class_="pager").find_all('a')
    items = items[1]['href'].split('page=')
    # print(items[1])
    return items[1]


def do(soup):
    for item in soup.find_all("tr", class_="odd"):
        myos.ls.writelines(item.text + '\n')

        a = item.a
        href = "http://www.ccgp-shanxi.gov.cn/" + a["href"]
        mode = item.text
        de = detail(href, mode)
        de.show()
        de.save()

    for item in soup.find_all("tr", class_="even"):
        myos.ls.writelines(item.text + '\n')

        a = item.a
        href = "http://www.ccgp-shanxi.gov.cn/" + a["href"]
        mode = item.text
        de = detail(href, mode)
        de.show()
        de.save()


do(soup)
counts = int(get_page(soup))
print('start:')
for i in range(counts):
    soup = turn_page(soup)
    print('-----------------------------------------')
    print(soup)
    do(soup)
