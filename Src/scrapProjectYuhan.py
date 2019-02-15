from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
import pageYuhan
import errLoging
import os
import downfile

sleepTime = 1



# initial factors
DownloadPath = "D:/Windows/Desktop/download"
mainUrl = ""
linkUrl = ""
#try:
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

#mainUrl linkUrl 사용 시작
mainUrl = 'http://lms.yuhan.ac.kr'
driver.get(mainUrl)



#내강의실 페이지로 이동


driver.get('https://lms.yuhan.ac.kr/Main.do?cmd=viewMypageMain&mainMenuId=menu_00050&subMenuId=&menuType=menu')

#iframe 안으로 포함된 웹 페이지로 이동
driver.get('https://lms.yuhan.ac.kr/Study.do?cmd=viewStudyMyClassroom')


html = driver.page_source
lstLectureRoomLinks=pageYuhan.lstFindLectureRoomInViewStudyMyClassroom(html)

#파일저장 위치로 이동
os.chdir(DownloadPath)
'''
for strLectureRoomLink in lstLectureRoomLinks:
    
    #각 강의실로 이동
    driver.get(mainUrl+strLectureRoomLink)
    #bsobj 초기화
    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')
    #강의실의 이름을 변수에 저장
    strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
    print(strSubjectName)
            

    #학습자료 찾기
    hakJaRyoUrl = bsObj.find('a', text='학습자료')['href']

    #print(mainUrl+hakJaRyoUrl)
    #학습자료 테이블 페이지로 이동
    driver.get(mainUrl+hakJaRyoUrl)
    #학습자료 테이블 페이지 link들을 담을 list 선언
    lstTableLinks=list()
    #현재 학습자료 테이블 페이지 링크 추가
    lstTableLinks.append(hakJaRyoUrl)
    #추가 학습자료 테이블 페이지 링크 추가
    html = driver.page_source
    lstTableLinks += pageYuhan.lstFindOtherTableLinksInTablePage(html)
    
    
    # 학습자료 테이블 페이지 링크에서 탐색
    for link in lstTableLinks:
        #학습자료 테이블 페이지로 이동
        driver.get(mainUrl+link)
        #학습자료 테이블 페이지의 html 소스를 변수에 저장
        tablePageHtml = driver.page_source
        # 학습자료 테이블 페이지에 튜플(게시글)이 존재할경우에만 탐색
        if pageYuhan.boolIsExistTupleInTablePage(tablePageHtml) is True:
            #강의실 이름의 폴더를 만들고 그하위에 학습자료 폴더를 만듬
            if os.path.isdir(strSubjectName+'/'+'학습자료') is False:
                os.makedirs(strSubjectName+'/'+'학습자료')
            #각 학습자료 튜플 페이지를 탐색
            for tuplePage in pageYuhan.lstFindTuplePageLinks(tablePageHtml):
                # 학습자료 튜플 페이지로 이동
                driver.get(mainUrl+tuplePage)
                # 학습자료 튜플 페이지의 html 소스를 변수에 저장
                tuplePageHtml = driver.page_source
                # 파일을 다운로드할 위치지정
                strSaveDir = DownloadPath+'/'+strSubjectName + '/학습자료'
                print(strSaveDir)
                # 학습자료 튜플 페이지에서 다운로드 링크들을 찾음
                for dictFile in pageYuhan.lstFindFileInHakJaRyoTuplePage(tuplePageHtml):
                    # saveDir 위치에 파일 다운
                    downfile.downFile(dictFile['name'],mainUrl+dictFile['url'],strSaveDir)

'''

# 과제 다운


for strLectureRoomLink in lstLectureRoomLinks:
    
    #각 강의실로 이동
    driver.get(mainUrl+strLectureRoomLink)
    #bsobj 초기화
    html = driver.page_source
    bsObj = BeautifulSoup(html, 'html.parser')
    #강의실의 이름을 변수에 저장
    strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
    print(strSubjectName)
            

    #과 제 찾기
    KuaJeaUrl = bsObj.find('a', text='과 제')['href']

    #print(mainUrl+KuaJeaUrl)
    #과제 테이블 페이지로 이동
    driver.get(mainUrl+KuaJeaUrl)
    #과제 테이블 페이지 link들을 담을 list 선언
    lstTableLinks=list()
    #현재 과제 테이블 페이지 링크 추가
    lstTableLinks.append(KuaJeaUrl)
    #추가 과제 테이블 페이지 링크 추가
    html = driver.page_source
    lstTableLinks += pageYuhan.lstFindOtherTableLinksInTablePage(html)
    
    
    # 과제 테이블 페이지 링크에서 탐색
    
    for link in lstTableLinks:
        #과제 테이블 페이지로 이동
        driver.get(mainUrl+link)
        print('현재 URL : '+ mainUrl+link)
        #과제 테이블 페이지의 html 소스를 변수에 저장
        tablePageHtml = driver.page_source
        # 과제 테이블 페이지에 튜플(게시글)이 존재할경우에만 탐색
        if pageYuhan.boolIsExistTupleInTablePage(tablePageHtml) is True:
            #강의실 이름의 폴더를 만들고 그하위에 과제 폴더를 만듬
            if os.path.isdir(strSubjectName+'/'+'과제') is False:
                os.makedirs(strSubjectName+'/'+'과제')
                print('디렉토리 생성 : '+ strSubjectName+'/'+'과제')
            #각 과제 튜플 페이지를 탐색
            for tuplePage in pageYuhan.lstFindTuplePageLinks(tablePageHtml):
                # 과제 튜플 페이지로 이동
                driver.get(mainUrl+tuplePage)
                print('현재 URL : '+ mainUrl+tuplePage)
                #####################
                time.sleep(sleepTime)
                # 과제 튜플 페이지의 html 소스를 변수에 저장
                tuplePageHtml = driver.page_source
                
                
                # 제출된 과제인지 확인
                if pageYuhan.boolIsSumittedKuaJea(tuplePageHtml) is True:
                    print('제출한 과제입니다.')
                    tuplePageBsObj = BeautifulSoup(tuplePageHtml, 'html.parser')
                    
                    submitInfoPageUrl = '/'+ tuplePageBsObj.find('span',text='제출정보보기').parent.parent['href']
                    #print(mainUrl + submitInfoPageUrl)
                    #제출 정보보기 사이트로 이동
                    driver.get(mainUrl + submitInfoPageUrl)
                    print('현재 URL : '+ mainUrl + submitInfoPageUrl)
                    #####################
                    time.sleep(sleepTime)
                    submitInfoPageHtml = driver.page_source
                    #파일이 존재하는지 확인 
                    if pageYuhan.boolIsExistFile(submitInfoPageHtml) is True:
                        print('현재 페이지에는 파일이 존재합니다.')
                        # 파일을 다운로드할 위치지정
                        strSaveDir = DownloadPath+'/'+strSubjectName + '/과제'
                        print('파일 저장 위치 : '+strSaveDir)
                        # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                        
                        for dictFile in pageYuhan.lstFindFileinKuaJeaInSubmitInfo(submitInfoPageHtml):
                            # saveDir 위치에 파일 다운
                            if 'nameProf' in dictFile:
                                downfile.downFile(dictFile['nameProf'],mainUrl+dictFile['urlProf'],strSaveDir)
                                print('저장 파일명 : '+ dictFile['nameProf'])
                                print('저장 파일의 URL : '+ dictFile['urlProf'])
                            if 'nameStd' in dictFile:    
                                downfile.downFile(dictFile['nameStd'],mainUrl+dictFile['urlStd'],strSaveDir)
                                print('저장 파일명 : '+ dictFile['nameStd'])
                                print('저장 파일의 URL : '+ dictFile['urlStd'])
                            
                            
                else :
                    # 미제출된 과제의 경우 처리
                    print('미제출한 과제입니다.')
                    if pageYuhan.boolIsExistFile(submitInfoPageHtml) is True:
                        # 파일을 다운로드할 위치지정
                        strSaveDir = DownloadPath+'/'+strSubjectName + '/과제'
                        print(strSaveDir)
                        # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                        for dictFile in pageYuhan.lstFindFileinKuaJeaInSubmitInfo(submitInfoPageHtml):
                            # saveDir 위치에 파일 다운
                            if 'nameProf' in dictFile:
                                downfile.downFile(dictFile['nameProf'],mainUrl+dictFile['urlProf'],strSaveDir)
                                print(dictFile['nameProf']+'\n'+dictFile['urlProf'])
                            #downfile.downFile(dictFile['nameStd'],mainUrl+dictFile['urlStd'],strSaveDir)


        
        #time.sleep(5)
        #kuaJeaUrl = bsObj.find('a', text='과 제')['href']
        #print(mainUrl+kuaJeaUrl)


#except Exception as errMsg:
#    print(errMsg)
#   errLoging.writeLog(errMsg)


