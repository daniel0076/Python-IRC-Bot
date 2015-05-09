#!/usr/bin/env python3.3
#coding=utf-8
import re
import subprocess as sp
def rup(para):
    if para == "":
        return 'Usage: @rup host [host ...]'
    cmd=list(("rup",para))
    rup=sp.Popen(
        cmd,
        stdin=sp.PIPE,
        stdout=sp.PIPE,
        stderr=sp.PIPE
    )
    out=rup.communicate()[0].decode()
    print(out)
    res=re.search("([\d]+) *days?, *([\d]+:[\d]+),.*load average: (.*)",out)
    if res == None :
        return 'unknown host "{}"'.format(para) 
    day=res.group(1)
    u_time=res.group(2)
    load=res.group(3)
    if re.search("^[\d]:[\d][\d]",u_time) != None:
        u_time="0{}".format(u_time)
    para="[{}]".format(para)
    final="{:10} uptime: {}d {}  load: {}".format(para,day,u_time,load)
    return final
