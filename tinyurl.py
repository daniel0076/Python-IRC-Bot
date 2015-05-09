#!/usr/bin/env python3.3
# -*- coding=utf-8 -*-
import re
from urllib.request  import urlopen
def create(url):
    des='http://tinyurl.com/create.php?url='
    get = urlopen(des+url).read().decode()
    patt='<blockquote><b>(http://tinyurl.com/.*)</b>'
    tiny=re.search(patt,get)
    return tiny.group(1)
