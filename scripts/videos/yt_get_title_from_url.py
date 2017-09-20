import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = False
        self.index = 0
        self.result = None
    def handle_starttag(self, tag, attrs):
        if tag == 'h1' and attrs == [('class','watch-title-container')]:
            self.title = True
    def handle_endtag(self, tag):
        if tag == 'h1':
            self.title = False
    def handle_data(self, data):
        if self.title:
            if self.index == 1:
                self.result = data.replace('\n','')[4::]
            self.index +=1

def get_title(url):
    parser = MyHTMLParser()
    u = urllib.request.urlopen(url)
    data = u.read().decode('utf8')
    parser.feed(data)
    return parser.result
