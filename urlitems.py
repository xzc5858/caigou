class urlitems(object):

    def __init__(self):
        self.new_Urls = set()
        self.old_Urls = set()

    def save_new_item(self, url):
        if url is not None:
            if url not in self.new_Urls and url not in self.old_Urls:
                print(url)
                self.new_Urls.add(url)
