Python IRC Bot
===

## Network Administration NCTU 2014 Spring

A simple IRC Bot by Python, NA project1

---

### Files & Modules

+ main
+ config
+ help_f.py
+ log.py
+ rup.py
+ cal.py
+ weather.py
+ tinyurl.py
+ chkword.py

---

+ configuration
    + set up parameters in `config`
+ main
    + the main file
    + parse the input and call functions
+ help_f.py
    + help generate help message
+ log.py
    + log parser
    + parse `/var/log/messages`
    + find out attempts to login by illegal users or wrong passwords
+ rup.py
    + run `rup` on the server
    + return the result to the IRC
+ cal.py
    + calculator
+ weather.py
    + get weather information from CWB website
+ tinyurl.py
    + make tinyurl for you
+ chkword.py
    + check specific patterns and response

### Usage

First run main on your server

+ Get weather : `@weather`
+ Use calculator : `@cal expression`
+ Make tinyurl : `URL`
+ Parse the log : `@log [-n num] [-u]`
+ Remote status : `@rup [host]`
+ Some keyword will do magic : Just see the code
