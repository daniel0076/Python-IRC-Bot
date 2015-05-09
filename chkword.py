#!/usr/bin/env python3.3
# -*- coding=utf8 -*-
import re
import socket
def check(bot,chan,user,cont):
    if re.search(".*傲嬌.*",cont) != None:
        msg = "人... 人家才不是傲嬌呢 >////<"
        bot.send('PRIVMSG {} :{}\r\n'.format(chan,msg).encode())
    if re.search(".*[惹$]",cont) !=None:
        msg = "你國文沒學好嗎？"
        bot.send('PRIVMSG {} :{}: {}\r\n'.format(chan,user,msg).encode())
    if re.search(".*[ㄅㄎㄇㄉ$]",cont) != None:
        msg = "請重念小學吧！"
        bot.send('PRIVMSG {} :{}: {}\r\n'.format(chan,user,msg).encode())
    if re.search(".*[Qq][Bb].*",cont) !=None:
        msg =  "QB 必需死"
        bot.send('PRIVMSG {} :{}\r\n'.format(chan,msg).encode())
    if re.search(">/+<",cont) != None:
        msg =  cont.replace('/','\\')
        bot.send('PRIVMSG {} :{}\r\n'.format(chan,msg).encode())
    return
