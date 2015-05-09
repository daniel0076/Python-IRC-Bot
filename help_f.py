#!/usr/bin/env python3
import re
import socket
def tip(chan,bot):
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"Usage: @weather //weather information.").encode())
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"Usage: @cal expression //calculator.").encode())
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"Usage: URL //shorten URL.").encode())
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"Usage: @rup [host] //remote status").encode())
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"Usage: @log [-n num] [-u] //log parser").encode())
    bot.send('PRIVMSG {} :{}\r\n'.format(chan,"some keyword will do magic!").encode())
    return
