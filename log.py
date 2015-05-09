#!/usr/bin/env python3
#coding=utf8
import re
import os
def parse(bot,chan,t,u):
    pwd="/tmp/messages"
    ip_count={}
    user_count={}
    for line in open(pwd):
        if "authentication error" not in line:  continue
#...PAM: authentication error for root from 1.93.37.230
        if "illegal user" not in line:
            col=line.split() 
            ip,user=col[-1].strip(),col[-3]
        else:
            fetch=re.search("illegal user (.*) from (.*)",line)
            user=fetch.group(1)
            ip=fetch.group(2)
        if ip not in ip_count:   ip_count[ip]=1
        elif ip in ip_count:     ip_count[ip]=ip_count[ip]+1
        if user not in user_count:   user_count[user]=1
        elif user in user_count:     user_count[user]=user_count[user]+1
    if u==True:
        for key in sorted(user_count,key=user_count.get,reverse=True):
            t=t-1
            if t<0: return
            bot.send('PRIVMSG {} :{:15} {} times\r\n'.format(chan,key,user_count[key]).encode())
    else:
        for key in sorted(ip_count,key=ip_count.get,reverse=True):
            t=t-1
            if t<0: return
            bot.send('PRIVMSG {} :{:15} {} times\r\n'.format(chan,key,ip_count[key]).encode())
