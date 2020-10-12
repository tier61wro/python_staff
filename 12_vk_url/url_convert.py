#!/usr/bin/env python3
'''
converts url like:
https://pp.userapi.com/c4993/u70018585/104486024/x_459bf9c1.jpg
to strings like
https://vk.com/u8758236
'''
import re
import sys

def url_convert(url):
    m = re.search(r"\/c\d+\/u(\d+)", url)
    if m :
        id = m.group(1)
        print ("found id = ", id)
        return 'https://vk.com/id'+str(id)
    else:
        print ("url seems to be old")
        sys.exit(0)

url_in  = 'https://pp.userapi.com/c4993/u70018585/104486024/x_459bf9c1.jpg'
url_out = url_convert(url_in)
print (url_out)
