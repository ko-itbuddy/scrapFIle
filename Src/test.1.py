import re
string = "fileDownload('*ED*95*99*EC*82*AC*EA*B4*80*EB*A6*AC_15*EC*A3*BC_2018_*EB*AC*B8*EC*A0*9C.ppt','FILE_181211113257dbdc3113.ppt','/business/report/2018203070148723/')"

#strList = re.split(';| |,|\'\'|\'|\(| |',string)
strList = string.split('\'')
#print(strList)
for i in strList:
    print(i)

returnList = list()
returnList.append(strList[1])
returnList.append(strList[3])
returnList.append(strList[5])

print(returnList)

'''
text = 'The quick brown\nfox jumps*over the lazy dog.'
print(re.split('; |, |\*|\n',text))
'''