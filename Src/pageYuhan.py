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
            lstResult.append(element.a['href'])
    return lstResult

def boolIsExistTupleInTablePage(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    # 검색 된 글이 없습니다. 라는 문구가 존재하면 그페이지에는 파일이 없는 것이다.
    if bsObj.find('td', text=re.compile('검색 된 글이 없습니다.')) is None:
        return True
    else:
        return False

def lstFindTuplePageLinks(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    lstResult = list()
    dictTemp = dict()
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
        
        lstResult.append('/'+link.a['href'])
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

def LstFindFileInHakJaRyoTuplePage(html):
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



        










#첫번째 정보
#selector
# mypage-content > div.cen > div.infobox > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3) > a:nth-child(5)
#xpath
# //*[@id="mypage-content"]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[3]/a[5]

#두번째 정보
#selector
# #mypage-content > div.cen > div.infobox > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(3) > a:nth-child(5)
#xpath
# //*[@id="mypage-content"]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[3]/a[5]

#세번째 정보
#selector
# #mypage-content > div.cen > div.infobox > div:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(3) > a:nth-child(5)
#xpath
# //*[@id="mypage-content"]/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[3]/a[5]

#print(bsObj.find("div",{"style":"margin-left:15px;"}))
# print(bsObj.select('div.infobox > div:nth-child(2) > table > tbody > tr'))
# 위코드는 출력되다가 끊긴다

#td에서 추출된 각 항목의 페이지 
def subjectMenuItem(link):
    #전체 주소를 생성
    url = 'https://lms.yuhan.ac.kr/'+ link
    print('과제 링크')
    print(url)
    driver.get(url)
    #time.sleep(10)
    html = driver.page_source
    #print(html)
    bsObj = BeautifulSoup(html,'html.parser')
    #교수님이 올리신 파일
    #교수님이 올리신 파일이 없을경우엔?
    try:
        
        #print(bsObj.find('div',{'title':re.compile('Download:')})['onclick'])
        profFileDownScript = bsObj.find('div',{'title':re.compile('Download:')})['onclick']
        fileDownloadLink = 'https://lms.yuhan.ac.kr/'+ fileDownloadHalfLink(profFileDownScript)
        print('교수님이 올린파일 다운로드 링크')
        #다운로드 링크 생성 -> 해당링크로 이동시 파일다운로드 진행됨
        print(fileDownloadLink)
    except TypeError:
        print('')
    except AttributeError:
        print('')

    #제출정보보기 페이지 링크
    try:
        print('제출정보 보기 링크')
        #찾은 element의 부모의 부모의 href를 가져옴
        print(bsObj.find('span', text='제출정보보기').parent.parent['href'])
    except TypeError:
        print('')
    except AttributeError:
        print('Attribute error')

    #fileDownloadLink = 'https://lms.yuhan.ac.kr/'+ fileDownloadHalfLink(bsObj.find('div',{'title':re.compile('Download:')})['onclick'])
    #print(fileDownloadLink)

#제출정보보기 페이지
def subjectMenuItemSubInfo(link):
    #전체 주소를 생성
    url = 'https://lms.yuhan.ac.kr/'+ link
    print(url)
    driver.get(url)
    #time.sleep(10)
    html = driver.page_source
    #print(html)
    bsObj = BeautifulSoup(html,'html.parser')
    #학생이 올린 파일
    #학생이 올린 파일이 없을경우엔?
    try:
        #print(bsObj.find('div',{'title':re.compile('Download:')})['onclick'])
        fileDownloadLink = 'https://lms.yuhan.ac.kr/'+ fileDownloadHalfLink()
        print(fileDownloadLink)
    except AttributeError:
        print('')

    #fileDownloadLink = 'https://lms.yuhan.ac.kr/'+ fileDownloadHalfLink(bsObj.find('div',{'title':re.compile('Download:')})['onclick'])
    #print(fileDownloadLink)
    



def extractFileDownLink(string):
    #strList = re.split(';| |,|\'\'|\'|\(| |',string)
    strList = string.split('\'')
    rfileName = str(strList[1])
    sfileName = str(strList[3])
    filePath = str(strList[5])
    
    loc = 'fileDownServlet?rFileName='+rfileName+'&sFileName='+sfileName+'&filePath='+filePath

    return loc



def m_mkdir(url):
    classRoomUrl='https://lms.yuhan.ac.kr'+url
    driver.get(classRoomUrl)
    html = driver.page_source

    bsObj = BeautifulSoup(html,'html.parser')
    #태그를 찾고 테그의 텍스트를 가져오기
    print('지금 강의실은 '+bsObj.find('p',{'class','subject-list'}).get_text()+'입니다')

    #학습자료 메뉴 정보
    #<a href="/Board.do?cmd=viewBoardContentsList&amp;boardInfoDTO.boardInfoId=2018203070148723-PDS" target="bodyFrame" onclick="Show_Menu_Board('2018203070148723-PDS',
	#'2018203070148723-PDS',
	#'/Board.do?cmd=viewBoardContentsList&amp;boardInfoDTO.boardInfoId=2018203070148723-PDS'); return false;">학습자료</a>
    # #menuBoardList > div:nth-child(1) > a
    #//*[@id="menuBoardList"]/div[1]/a
    
    #과 제 메뉴 정보
    #<a href="/AuthGroupMenu.do?cmd=goMenu&amp;mcd=menu_00088" target="bodyFrame" onclick="Show_Menu_Page('menu_00088',
	#'menu_00088',
	#'/Report.do?cmd=viewReportListLearner&amp;reportInfoDTO.reportType=course'); return false;">과 제</a>
    # #classBody > div.content > div.left > div:nth-child(5) > a
    # //*[@id="classBody"]/div[2]/div[1]/div[4]/a



    
    #학습자료 테이블
    #텍스트를 이용하여 링크를 크롤링
    curlPageUrl = 'https://lms.yuhan.ac.kr'+bsObj.find('a', text='학습자료')['href']
    driver.get(curlPageUrl)

    curlPageHtml = driver.page_source
    curlPageBsObj = BeautifulSoup(curlPageHtml,'html.parser')
    # pages로 리스트를 만들어서 주소들을 저장한다
    pages = list()
    pages.append(curlPageUrl)



    '''
    try:
        for page in curlPageBsObj.findAll('span',{'class':'page-num'}):
            pages.append('https://lms.yuhan.ac.kr/'+page.a['href'])
        
    except AttributeError:
        print('')

    print('#####################\nin 학습노트 pages')
    for page in pages:
        driver.get(page)
        tmpCurlPageHtml = driver.page_source
        tmpCurlPageBsObj = BeautifulSoup(tmpCurlPageHtml,'html.parser')
        tmpCurlPageBsObjList = tmpCurlPageBsObj.findAll('td',{'class':'list','nowrap':'true','align':'left','colspan':'1'})
        for tmp in tmpCurlPageBsObjList:
            downTableFile(tmp)
        
    
    time.sleep(sleepTime)
    '''

    #과 제 테이블
    

    curlPageUrl = 'https://lms.yuhan.ac.kr'+bsObj.find('a', text='과 제')['href']
    driver.get(curlPageUrl)
    curlPageHtml = driver.page_source

    curlPageBsObj = BeautifulSoup(curlPageHtml,'html.parser')
    pages = list()
    pages.append(curlPageUrl)
    
    try:
        for page in curlPageBsObj.findAll('span',{'class':'page-num'}):
            pages.append('https://lms.yuhan.ac.kr/'+page.a['href'])
    except AttributeError:
        print('')

    print('#####################\nin 과제 pages')
    #아까 수집해둔 테이블 페이지 링크들
    for page in pages:
        #print('*********'+page)
        driver.get(page)
        tmpCurlPageHtml = driver.page_source
        tmpCurlPageBsObj = BeautifulSoup(tmpCurlPageHtml,'html.parser')
        
        #테이블의 TD element중에 다운로드페이지로 가는 링크를 가진 요소들을 합한다.
        
        
        try:
            tmpCurlPageBsObjList = tmpCurlPageBsObj.findAll('td',{'class':'list','nowrap':'true','align':'left','colspan':'1'})
        except AttributeError:
            print('')

        for tmp in tmpCurlPageBsObjList:
            # tmp에서 파일 다운로드 링크를 가져오려면 다음 표현을 써야한다
            #tmp.a['href']
            #print(tmp.a['href'])
            downProfessorFile(tmp.a['href'])


    
    
