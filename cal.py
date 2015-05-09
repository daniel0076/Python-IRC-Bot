#!/usr/bin/env python3.3
#-*- coding=utf8 -*-
import re
def cal(exp):
    if re.search("[^0-9\+\-\*/\.\(\)\^]",exp) == 1:
        return "Usage: @cal <expression>"
    try:
        if exp.find("^") != -1:
            exp=exp.replace("^","**")
        eval(exp)
    except SyntaxError:
        return "Usage: @cal <expression>"
    except NameError:
        return "Usage: @cal <expression>"
    except EOFError:
        return "Usage: @cal <expression>"
    except TypeError:
        return "Usage: @cal <expression>"
    except ZeroDivisionError:
        return "Error!!Divided by zero"
    else:
        return eval(exp)

   

