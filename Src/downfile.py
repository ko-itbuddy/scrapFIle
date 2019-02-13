import urllib.request
import errLoging







def downFile(strName, strUrl, strPath):
    try:
        print(strPath+'/'+strName)
        urllib.request.urlretrieve(strUrl, strPath+'/'+strName)
    except FileExistsError as errMsg:
        errLoging.writeLog('*************** [in downfile.downFile]***************')
        errLoging.writeLog('errMsg')