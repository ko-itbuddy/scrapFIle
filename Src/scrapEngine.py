

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import selenium.common.exceptions
from bs4 import BeautifulSoup
import time
import re
import scrapEngineLib
import os
from downFileLib import DownFile as downfile
import sys
import traceback




class ScrapEngneForYuhan:
    def __init__(self, strUSERID, strUSERPWD, strDOWNLOADPATH, boolMKSUBDIRS, intSLEEPTIME,strTOPDIRNAME):
        
        # initial ststic factors
        self.ERROR = '[ERROR]:'
        self.RIGHT = '[RIGHT]:'

        # initial factors
        self.SLEEPTIME = intSLEEPTIME
        self.DOWNLOADPATH = strDOWNLOADPATH + '/'+strTOPDIRNAME
        self.USERID = strUSERID
        self.USERPWD = strUSERPWD
        self.progress = 0.0
        
        #downFileLib initial
        self.downfile = downfile(boolMKSUBDIRS)
        
    def increasePregress(self, flt):
        if self.progress < 100.0 :
            self.progress += flt
        else:
            pass
        

        
    def run(self):


        # Chrome의 드라이버 위치를 입력
        
        driver = webdriver.Chrome('.\chromedriver.exe')
        print('selenium Chrome Driver Loaded')
        #암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
        print('waiting 3 seconds....')
        driver.implicitly_wait(3)
        #웹페이지에 접근
        
        driver.get('https://portal.yuhan.ac.kr/user/login.face')
        time.sleep(self.SLEEPTIME)
        #textEdit_log.insertPlainText('현재 URL : '+driver.)

        
            
        print('로그인중...')
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').click()
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').clear()
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').send_keys(self.USERID)
        #time.sleep(2)
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').click()
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').clear()
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').send_keys(self.USERPWD)
        #time.sleep(2)
        print('로그인 완료!')
        #로그인 버튼 클릭
        driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/a').click()
        
            
            
            #alert = driver.switch_to.alert
            #alert.accept()
            #print(alert.text())
        

        #사이버 강의실로 이동
        try:
            #mainUrl linkUrl 사용 시작
            mainUrl = 'http://lms.yuhan.ac.kr'
            driver.get(mainUrl)
            time.sleep(self.SLEEPTIME)
            #print('현재 페이지 : '+driver.current_url)



            #내강의실 페이지로 이동


            driver.get('https://lms.yuhan.ac.kr/Main.do?cmd=viewMypageMain&mainMenuId=menu_00050&subMenuId=&menuType=menu')
            time.sleep(self.SLEEPTIME)
            #iframe 안으로 포함된 웹 페이지로 이동
            driver.get('https://lms.yuhan.ac.kr/Study.do?cmd=viewStudyMyClassroom')
            time.sleep(self.SLEEPTIME)


            html = driver.page_source
            lstLectureRoomLinks=scrapEngineLib.lstFindLectureRoomInViewStudyMyClassroom(html)
            totalCntLectureRoom = len(lstLectureRoomLinks)
            print('전체 강의실의 수 : {}' .format(totalCntLectureRoom))
            # 지정 다운로드 위치에 폴더가 존재하지 않으면 생성
            if os.path.isdir(self.DOWNLOADPATH) is False:
                os.makedirs(self.DOWNLOADPATH)
            #파일저장 위치로 이동
            os.chdir(self.DOWNLOADPATH)
            #####################################
            # 학습자료 다운로드
            print('###학습자료 다운로드')
            for strLectureRoomLink in lstLectureRoomLinks:
                
                #각 강의실로 이동
                driver.get(mainUrl+strLectureRoomLink)
                time.sleep(self.SLEEPTIME)
                #print('현재 페이지 : '+driver.current_url)
                #bsobj 초기화
                html = driver.page_source
                bsObj = BeautifulSoup(html, 'html.parser')
                #강의실의 이름을 변수에 저장
                strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
                #print(strSubjectName)
                print('현재 강의실은 : '+strSubjectName)

                #학습자료 찾기
                hakJaRyoUrl = bsObj.find('a', text='학습자료')['href']

                #print(mainUrl+hakJaRyoUrl)
                #학습자료 테이블 페이지로 이동
                driver.get(mainUrl+hakJaRyoUrl)
                time.sleep(self.SLEEPTIME)
                #print('현재 페이지 : '+driver.current_url)
                #학습자료 테이블 페이지 link들을 담을 list 선언
                lstTableLinks=list()
                #현재 학습자료 테이블 페이지 링크 추가
                lstTableLinks.append(hakJaRyoUrl)
                #추가 학습자료 테이블 페이지 링크 추가
                html = driver.page_source
                lstTableLinks += scrapEngineLib.lstFindOtherTableLinksInTablePage(html)
                                
                
                # 학습자료 테이블 페이지 링크에서 탐색
                for link in lstTableLinks:
                    #학습자료 테이블 페이지로 이동
                    driver.get(mainUrl+link)
                    time.sleep(self.SLEEPTIME)
                    #학습자료 테이블 페이지의 html 소스를 변수에 저장
                    tablePageHtml = driver.page_source
                    # 학습자료 테이블 페이지에 튜플(게시글)이 존재할경우에만 탐색
                    if scrapEngineLib.boolIsExistTupleInHakJaRyoTablePage(tablePageHtml) is True:
                        #강의실 이름의 폴더를 만들고 그하위에 학습자료 폴더를 만듬
                        #if os.path.isdir(strSubjectName+'/'+'학습자료') is False:
                            #os.makedirs(strSubjectName+'/'+'학습자료')
                        if os.path.isdir(strSubjectName) is False:
                            os.makedirs(strSubjectName)
                        #각 학습자료 튜플 페이지를 탐색
                        tuplePages = scrapEngineLib.lstFindTuplePageLinks(tablePageHtml)
                        totalCntTuplePages = len(tuplePages)
                        print('#검색된 글의 총 갯수 : {}' .format(totalCntTuplePages))
                        for tuplePage in tuplePages:
                            # 학습자료 튜플 페이지로 이동
                            driver.get(mainUrl+tuplePage['url'])
                            time.sleep(self.SLEEPTIME)
                            # 학습자료 튜플 페이지의 html 소스를 변수에 저장
                            tuplePageHtml = driver.page_source
                            # 파일을 다운로드할 위치지정
                            strSaveDir = self.DOWNLOADPATH+'/'+strSubjectName + '/학습자료'
                            #strSaveDir = self.DOWNLOADPATH+'/'+strSubjectNam
                            #페이지 html을 저장
                            htmlName = scrapEngineLib.changeFileNameForAll('_'+ tuplePage['name']+'.html',tuplePage['no'])
                            self.downfile.downHtml(htmlName,tuplePageHtml,strSaveDir)
                            #print(strSaveDir)
                            # 학습자료 튜플 페이지에서 다운로드 링크들을 찾음
                            for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileInHakJaRyoTuplePage(tuplePageHtml), tuplePage['no']):
                                # saveDir 위치에 파일 다운
                                self.downfile.downFile(dictFile['name'],mainUrl+dictFile['url'],strSaveDir)
                                time.sleep(self.SLEEPTIME)
                            self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                            print('##progress : '+'{:04.2f}%' .format(self.progress))
                    else :
                        print('#검색 된 글이 없습니다.')
                        self.increasePregress(47/totalCntLectureRoom)
                        print('##progress : '+'{:04.2f}%' .format(self.progress))
            self.progress = 50.0
            print('##progress : '+'{:04.2f}%' .format(self.progress))
            ########################################################
            #  과제 다운

            print('###과제 다운로드')
            for strLectureRoomLink in lstLectureRoomLinks:
                
                #각 강의실로 이동
                driver.get(mainUrl+strLectureRoomLink)
                #print('현재 페이지 : '+driver.current_url)
                time.sleep(self.SLEEPTIME)
                #bsobj 초기화
                html = driver.page_source
                bsObj = BeautifulSoup(html, 'html.parser')
                #강의실의 이름을 변수에 저장
                strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
                print('#현재 강의실은 : '+strSubjectName)
                        

                #과 제 찾기
                KuaJeaUrl = bsObj.find('a', text='과 제')['href']

                #print(mainUrl+KuaJeaUrl)
                #과제 테이블 페이지로 이동
                driver.get(mainUrl+KuaJeaUrl)
                #print('현재 페이지 : '+driver.current_url)
                time.sleep(self.SLEEPTIME)
                #과제 테이블 페이지 link들을 담을 list 선언
                lstTableLinks=list()
                #현재 과제 테이블 페이지 링크 추가
                lstTableLinks.append(KuaJeaUrl)
                #추가 과제 테이블 페이지 링크 추가
                html = driver.page_source
                lstTableLinks += scrapEngineLib.lstFindOtherTableLinksInTablePage(html)
                totalCntLectureRoom = len(lstLectureRoomLinks)
                
                # 과제 테이블 페이지 링크에서 탐색
                
                for link in lstTableLinks:
                    #과제 테이블 페이지로 이동
                    driver.get(mainUrl+link)
                    #print('현재 페이지 : '+driver.current_url)
                    time.sleep(self.SLEEPTIME)
                    #print('현재 URL : '+ mainUrl+link)
                    #과제 테이블 페이지의 html 소스를 변수에 저장
                    tablePageHtml = driver.page_source
                    # 과제 테이블 페이지에 튜플(게시글)이 존재할경우에만 탐색
                    if scrapEngineLib.boolIsExistTupleInKuaJeaTablePage(tablePageHtml) is True:
                        

                        if os.path.isdir(strSubjectName) is False:
                            os.makedirs(strSubjectName)
                        #각 과제 튜플 페이지를 탐색
                        tuplePages = scrapEngineLib.lstFindTuplePageLinks(tablePageHtml)
                        totalCntTuplePages = len(tuplePages)
                        print('#검색된 과제의 총 갯수 : {}'.format(totalCntTuplePages))
                        for tuplePage in tuplePages:
                            # 과제 튜플 페이지로 이동
                            driver.get(mainUrl + tuplePage['url'])
                            #time.sleep(self.SLEEPTIME)
                            # 과제 튜플 페이지의 html 소스를 변수에 저장
                            tuplePageHtml = driver.page_source
                            
                            
                            # 제출된 과제인지 확인
                            
                            if scrapEngineLib.boolIsSumittedKuaJea(tuplePageHtml) is True:
                                print('#제출한 과제입니다.')
                                tuplePageBsObj = BeautifulSoup(tuplePageHtml, 'html.parser')
                                
                                submitInfoPageUrl = '/'+ tuplePageBsObj.find('span',text='제출정보보기').parent.parent['href']
                                
                                #제출 정보보기 사이트로 이동
                                driver.get(mainUrl + submitInfoPageUrl)
                                time.sleep(self.SLEEPTIME)

                                submitInfoPageHtml = driver.page_source


                                # 파일을 다운로드할 위치지정
                                strSaveDir = self.DOWNLOADPATH+'/'+strSubjectName + '/과제'
                                
                                #페이지 html을 저장
                                htmlName = scrapEngineLib.changeFileNameForAll('_'+tuplePage['name']+'.html',tuplePage['no'])
                                self.downfile.downHtml(htmlName,submitInfoPageHtml,strSaveDir)

                                #파일이 존재하는지 확인 
                                if scrapEngineLib.boolIsExistFile(submitInfoPageHtml) is True:
                                    print('현재 페이지에는 파일이 존재합니다.')
                                    
                                    
                                    # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                                    for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileinKuaJeaInSubmitInfo(submitInfoPageHtml), tuplePage['no']):
                                        # saveDir 위치에 파일 다운
                                        
                                        if 'nameProf' in dictFile:
                                            self.downfile.downFile(dictFile['nameProf'],mainUrl+dictFile['urlProf'],strSaveDir)
                                            #print('저장 파일명 : '+ dictFile['nameProf'])
                                            #print('저장 파일의 URL : '+ dictFile['urlProf'])
                                        if 'nameStd' in dictFile:    
                                            self.downfile.downFile(dictFile['nameStd'],mainUrl+dictFile['urlStd'],strSaveDir)
                                            #print('저장 파일명 : '+ dictFile['nameStd'])
                                            #print('저장 파일의 URL : '+ dictFile['urlStd'])
                                        time.sleep(self.SLEEPTIME)
                                        #self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                                        #print('##progress : '+'{:04.2f}%' .format(self.progress))
                                else:
                                    print('현재 페이지에는 파일이 존재하지 않습니다.') 
                                    #self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                                    #print('##progress : '+'{:04.2f}%' .format(self.progress))
                                
                                    
                                        
                            else :
                                # 미제출된 과제의 경우 처리
                                print('#미제출한 과제입니다.')

                                # 파일을 다운로드할 위치지정
                                strSaveDir = self.DOWNLOADPATH+'/'+strSubjectName + '/과제'
                                
                                #페이지 html을 저장
                                htmlName = scrapEngineLib.changeFileNameForAll('_'+ tuplePage['name']+'.html',tuplePage['no'])
                                self.downfile.downHtml(htmlName,tuplePageHtml,strSaveDir)
                                #####################
                                

                                if scrapEngineLib.boolIsExistFile(tuplePageHtml) is True:
                                    print('현재 페이지에는 파일이 존재합니다.')
                                    
                                    #print('파일 저장 위치 : '+strSaveDir)
                                    # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                                    
                                    for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileInUnsubmittedKuaJeaPage(tuplePageHtml), tuplePage['no']):
                                        # saveDir 위치에 파일 다운
                                        if 'name' in dictFile:
                                            self.downfile.downFile(dictFile['name'],mainUrl+dictFile['url'],strSaveDir)
                                           
                                        time.sleep(self.SLEEPTIME)
                                else:
                                    print('현재 페이지에는 파일이 존재하지 않습니다.')
                            self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                            print('##progress : '+'{:04.2f}%' .format(self.progress))
                    else:
                        print('#등록된 과제가 없습니다.')
                        self.increasePregress(47/totalCntLectureRoom)
                        print('##progress : '+'{:04.2f}%' .format(self.progress))
            self.progress=100.0
            print('##progress : '+'{:04.2f}%' .format(self.progress))
            print('완료!')
        except Exception:
            traceback.print_exc()
        
        
        #driver.quit()
    

if __name__ == '__main__':
    #def __init__(self, strUSERID, strUSERPWD, strDOWNLOADPATH, boolMKSUBDIRS, intSLEEPTIME)
    strUSERID = ''
    strUSERPWD = ''
    strTOPDIRNAME = 'portfolio'
    strDOWNLOADPATH = os.getcwd().replace('\\\\','/')
    boolMKSUBDIRS = False
    intSLEEPTIME = 2
    


    #app = ScrapEngneForYuhan(strUSERID, strUSERPWD, strDOWNLOADPATH, boolMKSUBDIRS, intSLEEPTIME)
    #app.run()


    args = sys.argv[1:]
    
        
    for arg in args:        
        if re.compile('--path=').search(arg):
            rst = arg.split('=')
            strTemp = str(rst[1])
            strTemp = strTemp.replace('\\\\','/')
            strTemp = strTemp.replace('\\','/')
            if str(strTemp[-1]) == '/':
                strTemp= strTemp[0:-1]
            strDOWNLOADPATH = strTemp
            #print('--path='+strDOWNLOADPATH)
        elif re.compile('--topdirname=').search(arg):
            rst = arg.split('=')            
            strTOPDIRNAME = rst[1]
            #print('--topdirname='+rst[1])
        elif re.compile('--id=').search(arg):
            rst = arg.split('=')
            strUSERID = rst[1]
            #print('--id='+rst[1])
        elif re.compile('--pwd=').search(arg):
            rst = arg.split('=')
            strUSERPWD= rst[1]
            #print('--pwd='+rst[1])
        elif re.compile('--sleeptime=').search(arg):
            rst = arg.split('=')
            intSLEEPTIME= int(rst[1])
            print(intSLEEPTIME)
            #print('--sleeptime='+rst[1])
        elif re.compile('--mksubdirs=').search(arg):
            rst = arg.split('=')
            if rst[1] == 'True' or rst[1] == 'true':
                boolMKSUBDIRS = True
            #print('--mksubdirs='+rst[1])
        #elif re.compile('--help').search(arg) or re.compile('-h').search(arg) or re.compile('-H').search(arg):
        elif re.compile('--help').search(arg) \
            or re.compile('-h').search(arg) or \
            re.compile('-H').search(arg):
            print("########################################################################")
            print("설명 : 유한대 (구)사이버교육시스템의 각 강의실의 학습자료/과제를 모두 다운받습니다.\n")
            print('*주의* 본 프로그램은 다운로드 경로에 같은 파일이 존재할경우 자동으로 덮어씁니다.')
            print("사용법")
            print("--path=[STRING] : 학습자료/과제를 다운받을 경로를 지정합니다. 기본값 : [./] 현재폴더")
            print("                 ex > --path=C:/Users/HAPPY/scrapPortfolio/")
            print("                     --path=C:/Users/HAPPY/scrapPortfolio)")
            print("--topdirname=[STRING] : 다운로드 경로에 생성할 최상위 폴더의 이름을 입력합니다.")
            print("                 (기본값 : portfolio)\n")
            print("--id=[STRING] : (*필수) 유한대학교 포털사이트의 로그인 아이디를 입력합니다.\n")
            print("--pwd=[STRING] : (* 필수) 유한대학교 포털사이트의 로그인 비밀번호를 입력합니다.\n")
            print('--sleeptime=[INTEGER] : 페이지 이동과 파일 다운로드시 지연시간을 입력합니다.')
            print('                 단위 초 (기본값 : 2 학교 서버의 과부화로 인한 오류 발생을 막기 위함)\n') 
            print('--mksubdirs=[True|False] : 파일 저장시 각 강의실마다 학습자료/과제')
            print('                  폴더를 생성할지 설정합니다. (기본값 : False)\n')
            print('--help, -h, -H : 도움말을 보여줍니다.')
        else:
            rst = arg.split('=')
            strTemp = str(rst[0])
            sys.exit(strTemp + ' 는 사용이 불가능한 옵션입니다.\n도움말을 보려면 --help, -h, -H 옵션을 입력하십시오.')
            
    if os.path.exists('./chromedriver.exe') is False:
        print('chromedriver.exe 파일이 존재 하지 않습니다!')
        print('chromedriver.exe 파일을 실행 파일과 같은 폴더에 위치 시켜주세요!')
        print('다운로드 페이지 : https://sites.google.com/a/chromium.org/chromedriver/')
    elif len(args) == 0:
        print("잘못된 사용방법 입니다. 도움말을 보려면 --help, -h, -H 옵션을 입력하십시오.")
    elif strUSERID != '' and strUSERPWD != '':
        app = ScrapEngneForYuhan(strUSERID, strUSERPWD, strDOWNLOADPATH, boolMKSUBDIRS, intSLEEPTIME, strTOPDIRNAME)
        app.run()
    elif strUSERID == '':
        print('* 필수 값 --id=[STRING] 의 값이 없습니다! 도움말을 보려면 --help, -h, -H를 입력하십시오.')
    elif strUSERPWD == '':
        print('* 필수 값 --pwd=[STRING] 의 값이 없습니다! 도움말을 보려면 --help, -h, -H를 입력하십시오.')
        #print('* 필수 값 --pwd=[STRING]와 --id=[STRING] 의 값이 없습니다! \n도움말을 보려면 --help, -h, -H를 입력하십시오.')





