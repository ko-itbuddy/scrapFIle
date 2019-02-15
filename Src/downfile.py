import urllib.request
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(inspect.getfile(inspect.currentframe()))



def downHtml(strName, html, strPath):
    completeName = strPath+'/'+strName
    with open(completeName, "w" ,encoding='utf-8') as file:
        file.write(html)
    




def downFile(strName, strUrl, strPath):
    try:
        print(strPath+'/'+strName)
        urllib.request.urlretrieve(strUrl, strPath+'/'+strName)
    except FileExistsError as errMsg:
        errLoging.writeLog('*************** [in downfile.downFile]***************')
        errLoging.writeLog('errMsg')