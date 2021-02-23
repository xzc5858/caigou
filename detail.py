import myos
import sys
import requests
from bs4 import BeautifulSoup
import plug
import re


class detail:

    def __init__(self, url, mode):
        self.Url = url
        self.Soup = None
        self.Type = mode

    def show(self):
        r = plug.request_get(self.Url)
        self.Soup = BeautifulSoup(r.text, "html5lib")
        # print(self.Soup)
        return self.Soup

    def save(self):
        tb = self.Soup.find('table').find(class_='bk5').find('table')
        if tb is not None:
            self.zbz(tb)
        else:
            print('n')

    def zbz(self, soup):
        res = None
        myos.detail.writelines('----------------------------------------------\n')
        # print('---------------------------------------------------------------')
        # print(soup)
        for item in soup.find_all('p'):

            # myos.detail.writelines(item.text.strip()+'\n')
            # s = "联系方式"
            # ss = s.encode('UTF-8', 'strict')
            # print(item)
            res = re.match('^.*名称.*', item.text.strip())
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')
            res = re.match('^.*采购人.*', item.text.strip())
            # print(type(res))
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')
            res = re.match('^.*地址.*', item.text.strip())
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')
            res = re.match('^.*联系方式.*', item.text.strip())
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')
            res = re.match('^.*项目联系人(.+?)', item.text.strip())
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')
            res = re.match('^.*电话(.+?)', item.text.strip())
            if res != None:
                # print(item)
                myos.detail.writelines(item.text.strip() + '\n')


