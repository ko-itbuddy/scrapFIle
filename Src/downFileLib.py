import urllib.request
import os



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
                        completeName = strPath+'_'+strName
                with open(completeName, "w" ,encoding='utf-8') as file:
                        file.write(html)
                        print('저장 완료된 파일 : '+completeName)
        




        def downFile(self, strName, strUrl, strPath):
                if self.boolMkSubDirs is True:
                        if os.path.isdir(strPath) is False:
                                os.makedirs(strPath)
                                print('폴더 생성 : ' + strPath)
                        completeName = strPath+'/'+strName
                        
        #urllib.request.urlretrieve(strUrl, strPath+'/'+strName)
                else:
                        completeName = strPath+'_'+strName

                urllib.request.urlretrieve(strUrl, completeName)
                print('저장 완료된 파일 : '+completeName)
        