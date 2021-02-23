from base.spider import spider
import plug

class ccpgsx_spider(spider):


    def __init__(self):

        self.name = "sxccpg"
        self.url = "http://www.ccgp-shanxi.gov.cn/view.php?ntype=fnotice&nodeid=154"
        self.data = {"title": "网络安全", "type": "全部", "local": "", "dqx": ""}
        self.soup=plug.request_soup(self.url,False,self.data)

    def show_list(self):

        for item in self.soup.find_all("tr", class_="odd"):
           print(item.text+'\n')

        for item in soup.find_all("tr", class_="even"):
            print(item.text+'\n')



    def show_detail(self):
        r = plug.request_get(self.Url)
        self.Soup = BeautifulSoup(r.text, "html5lib")
        # print(self.Soup)
        return self.Soup

    def save_last(self):
        do(soup)
        counts = int(get_page(soup))
        print('start:')
        for i in range(counts):
            soup = turn_page(soup)
            print('-----------------------------------------')
            print(soup)
            do(soup)

    def save_detail(self):
        tb = self.Soup.find('table').find(class_='bk5').find('table')
        if tb is not None:
            self.zbz(tb)
        else:
            print('n')

    def turn_page(self):
        items = thissoup.find('div', class_="pager").find_all('a')
        for item in items:
            st = re.match('^后一页.*', item.text.strip())
            # print(st)
            if st != None:
                url = "http://www.ccgp-shanxi.gov.cn/" + item['href']
                soup = plug.request_soup(url, True, None)
        return soup

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
