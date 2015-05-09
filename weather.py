#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen
def getw():
    global whea,temp,content
    url='http://www.cwb.gov.tw/pda/observe/real/46757.htm'
    whea='天氣現象.*\n.*>(.*)</span></li>'
    temp='溫度.*\n<span class="headerText">([\d.]+)</span></li>'
    content = urlopen(url).read().decode()
def wea():
    global whea
    global content
    getw()
    wh = re.search(whea, content)
    res="天氣現象: {}".format(wh.group(1))
    return res
def tem():
    global temp
    global content
    getw()
    t=re.search(temp,content)
    res="溫度: {} ℃".format(t.group(1))
    return res
