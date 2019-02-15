import time
from bs4 import BeautifulSoup
import re
import errLoging



sleepTime = 1



def lstFindLectureRoomInViewStudyMyClassroom(html):
    #return Lecture Room links as list
    lstResult = list()
    #bsObj 초기화
    bsObj = BeautifulSoup(html,'html.parser')

    for element in bsObj.findAll('a',{'title':'강의실입장'}):
    #각 과목의 사이버 강의실의 웹페이지의 주소를 출력
        lstResult.append(element['href'])
        
    return lstResult

def strFindSubjectNameInLectureRoom(html):
    #return HakJaryo links as string
    strResult = str()
    #bsObj 초기화
    bsObj = BeautifulSoup(html,'html.parser')
    #텍스트가 '학습자료'인 a태그 찾기
    strResult= bsObj.find('a', text='학습자료')['href']


def lstFindOtherTableLinksInTablePage(html):
    lstResult = list()
    bsObj = BeautifulSoup(html,'html.parser')
    #class=page-num 이 존재하면 페이지가 더있음
    for element in bsObj.findAll('span',{'class':'page-num'}):
            lstResult.append('/'+element.a['href'])
    return lstResult

def boolIsExistTupleInHakJaRyoTablePage(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # "검색 된 글이 없습니다." 라는 문구가 존재하지 않으면 그페이지에는 파일이 존재하는 것이다.
    if bsObj.find('td', text=re.compile('검색 된 글이 없습니다.')) is None:
        return True
    else:
        return False

def lstFindTuplePageLinks(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    lstResult = list()
    
    strTmpFileName = str()
    strTmpFileLink = str()
    strTmpFileDate = str()
    #튜플 페이지 링크는 다음 태그에 존재
    #<td class="list" nowrap="true" align="left" colspan="1">
    #<a href="Board.do?cmd=viewBoardContents&amp;boardInfoDTO.boardInfoId=2018103070105323-PDS&amp;boardContentsDTO.boardContentsId=BOAD_180611152447668f0a49&amp;boardContentsDTO.contentsNo=6&amp;boardContentsDTO.gongjiYn=N&amp;gubun=V&amp;curPage=1">
    # 퀴즈자료
    # </a>
    # </td>

    #/html/body/div/form/table/tbody/tr[1]/td[1]
    #/html/body/div/form/table/tbody/tr/td[2]
    #/html/body/div/form/table/tbody/tr[1]/td[5] 날짜

    for link in bsObj.findAll('td',{'class':'list','nowrap':'true','align':'left','colspan':'1'}):
        dictTemp = dict()
        dictTemp['no'] = link.previous_sibling.previous_sibling.get_text()
        dictTemp['url'] = '/'+link.a['href']
        lstResult.append(dictTemp)
    return lstResult

def __decodeFileDownLink(string):
    #strList = re.split(';| |,|\'\'|\'|\(| |',string)
    strResult = str()
    strList = string.split('\'')
    rfileName = str(strList[1])
    sfileName = str(strList[3])
    filePath = str(strList[5])
    
    strResult = 'fileDownServlet?rFileName='+rfileName+'&sFileName='+sfileName+'&filePath='+filePath

    return strResult

def lstFindFileInHakJaRyoTuplePage(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    lstResult = list()
    dictTemp = dict()
    strTmpFileName = str()
    strTmpFileLink = str()
    bsObj.find()
    for element in bsObj.findAll('div',{'class':'file'}):
        dictTemp['name'] = element.div.get_text()
        dictTemp['url'] = '/'+__decodeFileDownLink(element.div['onclick'])
        lstResult.append(dictTemp)
    return lstResult

def boolIsExistTupleInKuaJeaTablePage(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # "검색 된 글이 없습니다." 라는 문구가 존재하지 않으면 그페이지에는 파일이 존재하는 것이다.
    if bsObj.find('td', text=re.compile('등록된 과제가 없습니다.')) is None:
        return True
    else:
        return False

def boolIsSumittedKuaJea(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # "제출정보보기" 라는 문구가 존재하지 않으면 미제출된 과제의 페이지이다
    
    
    if bsObj.find('span', text=re.compile('제출정보보기')) is None:
        
        return False
    else:
        return True
        

def boolIsExistFile(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # 파일의 title은 Download~로 시작한다
    if bsObj.find('td', {'title',re.compile('Download')}) is None:
        return True
    else:
        return False

def lstFindFileinKuaJeaInSubmitInfo(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # 기본정보는 파일을 포함한 링크와 함께 해당 테이블 태그에 속해 있다.
    tmpBsObj = bsObj.find('th', text='과제명').parent.parent
    #print(tmpBsObj)
    
    lstResult = list()
    dictProfTemp = dict()
    dictStdTemp = dict()
    strTmpFileName = str()
    strTmpFileLink = str()

    for element in tmpBsObj.findAll('div',{'onclick':re.compile('fileDownload')}):
        #print(element)
        dictProfTemp['nameProf'] = element.get_text()
        dictProfTemp['urlProf'] = '/'+__decodeFileDownLink(element['onclick'])
        lstResult.append(dictProfTemp)

    
    tmpBsObj = bsObj.find('th', text='과제설명').parent.parent
    #print(tmpBsObj)

    for element in tmpBsObj.findAll('div',{'onclick':re.compile('fileDownload')}):
        #print(element)
        dictStdTemp['nameStd'] = element.get_text()
        dictStdTemp['urlStd'] = '/'+__decodeFileDownLink(element['onclick'])
        lstResult.append(dictStdTemp)
    #print(lstResult)
    return lstResult
    
#lstFindFileInUnsubmittedKuaJeaPage same as
def lstFindFileInUnsubmittedKuaJeaPage(html):
    return lstFindFileInHakJaRyoTuplePage(html)
    

#object type is str or list
def changeFileNameForAll(obj,no):
    lstTemp = str()
    lstReusult = list()
    strResult = str()
    # 앞에 0을 대입 하여 2자리로 만듬 ex 2 -> 02
    no = no.zfill(2)
    


    if isinstance(obj, list) is True:
        for dictInLst in obj:
            if 'name' in dictInLst :
                lstTemp = dictInLst['name'].split('.')
                dictInLst['name'] = no + '_' + lstTemp[0] + '.' + lstTemp[1]
                lstReusult.append(dictInLst)
            elif 'nameStd' in dictInLst:
                lstTemp = dictInLst['nameStd'].split('.')
                dictInLst['nameStd'] = no + '_' + lstTemp[0] + '-Student.' + lstTemp[1]
                lstReusult.append(dictInLst)
            elif 'nameProf' in dictInLst:
                lstTemp = dictInLst['nameProf'].split('.')
                dictInLst['nameProf'] = no + '_' + lstTemp[0] + '-Professor.' + lstTemp[1]
                lstReusult.append(dictInLst)
        return lstReusult
    elif isinstance(obj, str) is True:
        lstTemp = obj.split('.')
        return  no + '_' + lstTemp[0] + '.' + lstTemp[1]
    


exLstFileOne = [{'name':'abc.hwp'}, {'nameProf':'def.hwp'},{'nameStd':'ghi.hwp'}]
exLstFileTwo = [{'nameProf':'def.hwp'},{'nameStd':'ghi.hwp'}]
exLstFileThree = [{'nameStd':'ghi.hwp'}]

