import datetime
now = datetime.datetime.now()

nowDate = now.strftime('%Y%m%d')
nowTime = now.strftime('%H-%M-%S-%f')
def writeLog(errMsg):
    strFileName = nowDate+".log"
    with open(strFileName,'a',encoding='utf-8') as f:
        strLogLine = nowTime+' : ' +str(errMsg)+'\n'
        f.write(strLogLine)


