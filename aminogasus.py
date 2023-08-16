#!/usr/bin/env python3
import aminofix as a #amino.fix 2.3.6.1
import asyncio,aiohttp
from os import _exit,listdir
import signal
import platform
from time import sleep


try:
    if str(platform.system()).lower()=="windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except:
    pass


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()



c=None
async def getinfo(userId: str,comId:str,session: aiohttp.ClientSession):
    global c
    async with session.get(f"{c.api}/x{comId}/s/user-profile/{userId}", headers=c.parse_headers()) as response:
        try: 
            return await response.json()
        except:
            return await response.text()



def interaption_handler(signum,func):
    print("program terminated")
    _exit(1)

signal.signal(signal.SIGINT,interaption_handler)



threwo=0
for dir_elm in listdir("comIds"):
    if threwo % 3==0:
        print("")
        threwo =1
    if dir_elm.find(".txt")!=-1 and dir_elm.find("requirements.txt")==-1:
        print(dir_elm+"   ",end="")
        threwo +=1
print("\n")    
print("""
comIds file exemple : result_en_490.txt
""")
f=input("give me file name of comIds : ")
comIds=[]
try:
    lines=open(f.strip(),"r").readlines()
    for l in lines:
        com=l.strip()
        if com!="":
            comIds.append(com)
except:
    try:
        lines=open("comIds/"+f.strip(),"r").readlines()
        for l in lines:
            com=l.strip()
            if com!="":
                comIds.append(com) 
    except Exception as e:
        print("error in file ",e)
        _exit(1)

#url="https://aminoapps.com/p/fucvk"
cond=False
url=""
userId=""
c=a.Client()
api=c.api
print("""
url exemple : http://aminoapps.com/p/vh7bif
""")
while cond==False:
    url=input("give me url of target : ").strip()
    infoo=c.get_from_code(url)
    userId=infoo.objectId
    if str(infoo.objectType)=="0":
        
        cond=True
    else:
        print("please give me url of profile")





def gasas(comIds):
    all_comIds=[]
    counts=len(comIds)
    if counts>=100:
        j=0
        for i in range(100,counts,100):
            j=i
            all_comIds.append(comIds[i-100:i])

        all_comIds.append(comIds[j:counts])

    elif counts<100:
        all_comIds.append(comIds)

    return all_comIds

exists=[]
not_exits_now=[]
error_comIds=[]

async def maino(userId,comIds,show=False):
    global error_comIds
    global exists
    global not_exits_now
    indexo=0
    connector=aiohttp.TCPConnector(limit=2)
    async with aiohttp.ClientSession(connector=connector) as session:
        printProgressBar(0, len(comIds), prefix = 'Progress:', suffix = 'Complete', length = 20)
        for comId in comIds:
            try:
                info= await getinfo(userId,comId,session)
                if info["api:statuscode"] == 0:
                    if info["userProfile"]["status"]==0:
                        exists.append(comId)
                        
                        print("avaliable comID existing now",comId," "*20)
                    #elif info["userProfile"]["status"]==3 or info["userProfile"]["status"]==9:
                    else:
                        not_exits_now.append(comId)
                        
                        print("avaliable comID exists, but He has leave the community",comId," "*10)
            except:
                if show==True:
                    print(info)
                    print("""
                    #######################
                    """)
                try:
                    if info["api:statuscode"] != 225:
                        error_comIds.append(comId)
                except:
                    
                    error_comIds.append(comId)
            
            printProgressBar(indexo + 1, len(comIds), prefix = 'Progress:', suffix = 'Complete', length = 20)
            indexo+=1

async def mainer():

    global comIds
    global error_comIds
    all_comIds=gasas(comIds)
    conter=len(all_comIds)
    indexer=1
    for comIds0 in all_comIds:
        print(f"{indexer}/{conter}")
        await maino(userId,comIds0)
        sleep(3)
        indexer+=1
    while len(error_comIds)>0:
        print("we have ",len(error_comIds)," errors in comIds ,need to fix him")
        print(error_comIds)
        print("\n\nimportant hint :\n\nIt would be better to wait 1 min to 3 minutes before choosing : Yes",
        "\nso that you have to unblock while waiting\n")
        fix=input("you need to fix him ? y/n : ").lower()

        if fix=="y" or fix=="":
            indexer=1
            all_comIds=gasas(error_comIds)
            conter=len(all_comIds)
            error_comIds=[]
            for comIds0 in all_comIds:
                print(f"{indexer}/{conter}")
                await maino(userId,comIds0,show=True)
                sleep(3)
                indexer+=1   
        else:
            error_comIds=[]  

loop=asyncio.get_event_loop()
loop.run_until_complete(mainer())
loop.close()

print("""

#####################################################
               exist now
""")

for e in exists:
    print(f"ndc://x{e}/user-profile/{userId}")
print("""

#####################################################
              not exist now
""")

for e in not_exits_now:
    print(f"ndc://x{e}/user-profile/{userId}")


#info["api:statuscode"] = 225 # not exists

#info["api:statuscode"] = 0 #  exists userProfile status 0
#info["api:statuscode"] = 0 #  exists banned userProfile status 9
#info["api:statuscode"] = 0 #  exists leave userProfile status 3

# narviiapp://x03235/user-profile/dffdsfgdsdsgsddssh

_exit(0)
