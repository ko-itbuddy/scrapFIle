import urllib.request
import logging
import inspect
import re
import os


# create logger
logging.basicConfig(filename='scrapProject.log',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(inspect.getfile(inspect.currentframe()))
logger.setLevel(logging.DEBUG)




def downHtml(strName, html, strPath):
        
        strName = strName.replace('\\','_')
        strName = strName.replace('/','_')
        strName = strName.replace(':','_')
        strName = strName.replace('*','_')
        strName = strName.replace('?','_')
        strName = strName.replace('\"','_')
        strName = strName.replace('<','_')
        strName = strName.replace('>','_')
        strName = strName.replace('|"','_')

        
    
        #if os.path.isdir(strPath) is False:
                #os.makedirs(strPath)
        #completeName = strPath+'/'+strName
        #print(strPath+'/'+strName)
        completeName = strPath+strName
        print(strPath+strName)
        with open(completeName, "w" ,encoding='utf-8') as file:
                file.write(html)
    




def downFile(strName, strUrl, strPath):
    #print(strPath+'/'+strName)
    #if os.path.isdir(strPath) is False:
        #os.makedirs(strPath)
    #print(strPath+'/'+strName)
    #urllib.request.urlretrieve(strUrl, strPath+'/'+strName)
    print(strPath+strName)
    urllib.request.urlretrieve(strUrl, strPath+strName)
    