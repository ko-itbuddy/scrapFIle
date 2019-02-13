import urllib.request







def downFile(strName, strUrl, strPath):
    print(strPath+'/'+strName)
    urllib.request.urlretrieve(strUrl, strPath+'/'+strName)