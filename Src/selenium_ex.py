from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

sleepTime = 1

# Chrome의 드라이버 위치를 입력
driver = webdriver.Chrome('Ext/chromedriver')

#암묵적으로 웁 자원 로드를 위해 3초까지 기다료 준다.
driver.implicitly_wait(3)

#웹페이지에 접근
driver.get('https://portal.yuhan.ac.kr/user/login.face')

#로그인 정보 입력
login = driver.find_element_by_css_selector('#userId')

driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').click()
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').clear()
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').send_keys('skvudrms54')
#time.sleep(2)
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').click()
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').clear()
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').send_keys('hcnask2211PT!!')
#time.sleep(2)

#로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/a').click()

#사이버 강의실로 이동
driver.get('https://lms.yuhan.ac.kr/sso_index.jsp')

driver.get('http://lms.yuhan.ac.kr/')


#내강의실 페이지로 이동
driver.get('https://lms.yuhan.ac.kr/Main.do?cmd=viewMypageMain&mainMenuId=menu_00050&subMenuId=&menuType=menu')

#iframe 안으로 포함된 웹 페이지로 이동
driver.get('https://lms.yuhan.ac.kr/Study.do?cmd=viewStudyMyClassroom')

time.sleep(sleepTime)
html = driver.page_source
#print(html)
bsObj = BeautifulSoup(html, 'html.parser')


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


    
    
    
    time.sleep(sleepTime)


    print('-------------------------------------------------')
    
    #https://lms.yuhan.ac.kr/Main.do?cmd=viewCourseMain&mainDTO.courseId=2018204650189219&gubun=study_course
    #https://lms.yuhan.ac.kr/Report.do?cmd=viewReportListLearner&reportInfoDTO.reportType=course
    #https://lms.yuhan.ac.kr/Board.do?cmd=viewBoardContentsList&boardInfoDTO.boardInfoId=2018204650189219-PDS


    #학습자료, 과 제 페이지 table의 tr
    #/html/body/div/form/table/tbody/tr[1]
    #등록된 자료가 없을때 다음 element가 존재
    #<td colspan="5" align="center"> 등록된 과제가 없습니다.	</td>
    #time.sleep(2)

    



    



for element in bsObj.findAll('a',{'title':'강의실입장'}):
    #각 과목의 사이버 강의실의 웹페이지의 주소를 출력
    print(element['href'])
    m_mkdir(element['href'])
    
    




'''
for i in bsObj.select('div.infobox > div:nth-child(2) > table > tbody > tr'):
    print(i)

for child in bsObj.find("div",{"class":"infobox"}).children:
    print(child)



'''