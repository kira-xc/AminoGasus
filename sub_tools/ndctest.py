#!/usr/bin/env python3
import aminofix as a
c=a.Client()
cc=c.get_from_id("a72384e2-53c8-486e-8459-50a8fdd48f48",0,"3")
print(cc.shortUrl)