#!/usr/bin/env python3
import aminofix as a
from time import sleep
from os import _exit
c=a.Client()

print("paste all ndc urls here when you finish type : @end to finish")
lines = []
while True:
    line = input()
    if line!="@end":
        lines.append(line)
    else:
        break
try:
    for d in lines:
        d=d.strip()
        if d!="" and d!="\n": 
            cc=c.get_from_id(d[d.find("e/")+2:],0,d[d.find("x")+1:d.find("/u")])
            print(cc.shortUrl)
            sleep(1)
except Exception as e:
    print(e)
    _exit(1)
_exit(0)