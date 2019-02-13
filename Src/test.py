import os
import time
os.getcwd()
now = time.gmtime(time.time())

print(now)

lst_dirName = ['a','b','c','d']
try:
        
    for dirName in lst_dirName:
        os.mkdir(dirName)
except OSError as e:
    strFileName = str(now.tm_year)+str(now.tm_mon)+str(now.tm_mday)+".log"
    with open(strFileName,'a',encoding='utf-8') as f:
        strLogLine = str(now.tm_hour)+str(now.tm_min)+str(now.tm_sec) +' : ' +str(e)+'\n'
        f.write(strLogLine)
    