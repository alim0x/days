# -*- coding: utf-8 -*-

import requests
import HTMLParser
import re
import os
import shutil

class MyHTMLParser(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.addressList = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            if attrs[1][1] == 'img-responsive js-fluid-image js-packery-image':
                self.addressList.append(attrs[0][1])

    def processAddress(self, addrs):
        preUrl = 'https://download.unsplash.com/'
        if not re.search('reserve/', addrs):
            return preUrl + re.search('(?<=net/).*(?=\?)', addrs).group(0)
        else:
            return preUrl + re.search('reserve.*\.jpg', addrs, re.I).group(0)


class CheckStatus(object):
    pass



class DownloadImg(object):

    def __init__(self):
        self.fileSize = 0

    def downloadImg(self, url):
        print 'Getting and saving photo...'
        imgResponse = requests.get(url, stream=True)

        if imgResponse.status_code == 200:
            self.fileSize = int(imgResponse.headers['content-length'])
            with open(os.path.abspath('.') + '\\img.jpg', 'wb') as f:
                imgResponse.raw.decode_content = True
                shutil.copyfileobj(imgResponse.raw, f)

        if self.verifyImgSize():
            print 'Things all done!'
        else:
            self.downloadImg(url)

    def verifyImgSize(self):
        if os.path.getsize(os.path.abspath('.') + '\\img.jpg') == self.fileSize:
            return True
        else:
            print 'Downloaded photo\'s size is wrong, retrying...'
            return False



if __name__ == '__main__':
    index = requests.get('http://unsplash.com/')

    my = MyHTMLParser()
    my.feed(index.text)
    my.close()
    for i in range(10):
        my.addressList[i] = my.processAddress(my.addressList[i])
    down = DownloadImg()
    want = raw_input("Which pic do you want?(1~10)\n")
    want = int(want) % 10 - 1
    down.downloadImg(my.addressList[want])
