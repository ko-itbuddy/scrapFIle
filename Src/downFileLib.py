import urllib.request
import logging
import inspect
import re
import os


# create logger
logging.basicConfig(filename='scrapProject.log',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(inspect.getfile(inspect.currentframe()))
logger.setLevel(logging.DEBUG)


class DownFile:
        def __init__(self, boolMKSUBDIRS):
                self.boolMkSubDirs = boolMKSUBDIRS
        def downHtml(self, strName, html, strPath):
                
                strName = strName.replace('\\','_')
                strName = strName.replace('/','_')
                strName = strName.replace(':','_')
                strName = strName.replace('*','_')
                strName = strName.replace('?','_')
                strName = strName.replace('\"','_')
                strName = strName.replace('<','_')
                strName = strName.replace('>','_')
                strName = strName.replace('|"','_')

                
                if self.boolMkSubDirs is True:
                        if os.path.isdir(strPath) is False:
                                os.makedirs(strPath)
                                print('폴더 생성 : ' + strPath)
                        completeName = strPath+'/'+strName
                        
                else:
                        completeName = strPath+strName
                with open(completeName, "w" ,encoding='utf-8') as file:
                        file.write(html)
        




        def downFile(self, strName, strUrl, strPath):
                if self.boolMkSubDirs is True:
                        if os.path.isdir(strPath) is False:
                                os.makedirs(strPath)
                                print('폴더 생성 : ' + strPath)
                        completeName = strPath+'/'+strName
                        
        #urllib.request.urlretrieve(strUrl, strPath+'/'+strName)
                else:
                        completeName = strPath+strName

                urllib.request.urlretrieve(strUrl, completeName)
        