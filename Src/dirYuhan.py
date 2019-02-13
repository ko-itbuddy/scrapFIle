import os
import time
import errLoging
os.getcwd()
now = time.gmtime(time.time())

print(now)



def makeDir(strName):
    try:
        os.mkdir(strName)
    except OSError as e:
        errLoging

def move
