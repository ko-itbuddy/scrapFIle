###################################
# UI part
import sys, subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogForm import Ui_Dialog_scrap
from scrapEngine import ScrapEngneForYuhan
import threading

##################################
# scrapEngine

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




class AppWindow(Ui_Dialog_scrap):
    def initAll(self):
        #init
        self.init()
        #actions
        self.actions()
       #self.actionOntoolButton_selectDir()
#init
    def init(self):
        #lineEdit_selectedDir
        self.lineEdit_selectedDir.setText(os.getcwd())
        #lineEdit_id
        #lineEdit_pwd
        #groupBox_downType
        #radioButton_mkHakKuaDirs
        #radioButton_justName
        #label_selectedDir
        #label_id
        #label_pwd
        #pushButton_start
        #pushButton_selectDir
        #lineEdit_subDirName
        self.lineEdit_subDirName.setText("portfolio")
        #label_subDirName
        #textEdit_log
        #pushButton_saveLog
        
#action connector      
    def actions(self):
        
        #lineEdit_selectedDir
        #lineEdit_id
        #lineEdit_pwd
        #groupBox_downType
        #radioButton_mkHakKuaDirs
        #radioButton_justName
        #label_selectedDir
        #label_id
        #label_pwd
        #pushButton_start
        self.pushButton_start.clicked.connect(self.pushButton_start_clicked)
        #pushButton_selectDir
        self.pushButton_selectDir.clicked.connect(self.showDirExprolerDialog)
        #lineEdit_subDirName
        #label_subDirName
        #textEdit_log
        #pushButton_saveLog
        self.pushButton_saveLog.clicked.connect(self.pushButton_saveLog_clicked)
        
        
   
#actions 
    def showDirExprolerDialog(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory(None, '다운로드 경로 지정', './')
        self.lineEdit_selectedDir.setText(dirName)
    
    
    def pushButton_saveLog_clicked(self):
        fUrl = QtWidgets.QFileDialog.getSaveFileName(None, "로그 파일 저장위치", 'scrapLog.txt', "Images (*.txt)")
        
        with open(fUrl[0],'w', encoding='UTF-8') as f:
            f.write = self.textEdit_log.toPlainText()
    #ScrapEngneForYuhan(self, strUSERID, strUSERPWD, strDOWNLOADPATH,boolMKSUBDIRS, intSLEEPTIME)
    def pushButton_start_clicked(self):
        #define engine From scrapEngine.ScrapEngine FOr Yuhan
        self.textEdit_log.append(self.lineEdit_id.text())
        self.textEdit_log.append(self.lineEdit_pwd.text())
        self.textEdit_log.append(self.lineEdit_selectedDir.text())
        strUSERID = self.lineEdit_id.text()
        strUSERPWD = self.lineEdit_pwd.text()
        strDOWNLOADPATH = self.lineEdit_selectedDir.text()
        boolMKSUBDIRS = False
        intSLEEPTIME = 2
        strTOPDIRNAME = self.lineEdit_subDirName.text()

        
        self.initRun(strUSERID, strUSERPWD, strDOWNLOADPATH,boolMKSUBDIRS, intSLEEPTIME, strTOPDIRNAME)
        self.run()


########################e
#engine part
    def increasePregress(self, flt):
        if self.progress < 100.0 :
            self.progress += flt
        else:
            pass



    def initRun(self, strUSERID, strUSERPWD, strDOWNLOADPATH, boolMKSUBDIRS, intSLEEPTIME,strTOPDIRNAME):
        
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
        
        
    
        

        
    def run(self):


        # Chrome의 드라이버 위치를 입력
        driver = webdriver.Chrome('Ext/chromedriver')
        self.textEdit_log.append('selenium Chrome Driver Loaded')
        #암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
        self.textEdit_log.append('waiting 3 seconds....')
        driver.implicitly_wait(3)
        #웹페이지에 접근
        
        driver.get('https://portal.yuhan.ac.kr/user/login.face')
        time.sleep(self.SLEEPTIME)
        #textEdit_log.insertPlainText('현재 URL : '+driver.)

        try:
            #로그인 정보 입력
            
            self.textEdit_log.append('로그인중...')
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').click()
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').clear()
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[1]/input').send_keys(self.USERID)
            #time.sleep(2)
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').click()
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').clear()
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/p[2]/input').send_keys(self.USERPWD)
            #time.sleep(2)
            self.textEdit_log.append('로그인 완료!')
            #로그인 버튼 클릭
            driver.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/a').click()
        except Exception as e:
            traceback.print_exc()
            #alert = driver.switch_to.alert
            #alert.accept()
            #self.textEdit_log.append(alert.text())
        

        #사이버 강의실로 이동
        try:
            #mainUrl linkUrl 사용 시작
            mainUrl = 'http://lms.yuhan.ac.kr'
            driver.get(mainUrl)
            time.sleep(self.SLEEPTIME)
            #self.textEdit_log.append('현재 페이지 : '+driver.current_url)



            #내강의실 페이지로 이동


            driver.get('https://lms.yuhan.ac.kr/Main.do?cmd=viewMypageMain&mainMenuId=menu_00050&subMenuId=&menuType=menu')
            time.sleep(self.SLEEPTIME)
            #iframe 안으로 포함된 웹 페이지로 이동
            driver.get('https://lms.yuhan.ac.kr/Study.do?cmd=viewStudyMyClassroom')
            time.sleep(self.SLEEPTIME)


            html = driver.page_source
            lstLectureRoomLinks=scrapEngineLib.lstFindLectureRoomInViewStudyMyClassroom(html)
            totalCntLectureRoom = len(lstLectureRoomLinks)
            self.textEdit_log.append('전체 강의실의 수 : {}' .format(totalCntLectureRoom))
            # 지정 다운로드 위치에 폴더가 존재하지 않으면 생성
            if os.path.isdir(self.DOWNLOADPATH) is False:
                os.makedirs(self.DOWNLOADPATH)
            #파일저장 위치로 이동
            os.chdir(self.DOWNLOADPATH)
            #####################################
            # 학습자료 다운로드
            self.textEdit_log.append('###학습자료 다운로드')
            for strLectureRoomLink in lstLectureRoomLinks:
                
                #각 강의실로 이동
                driver.get(mainUrl+strLectureRoomLink)
                time.sleep(self.SLEEPTIME)
                #self.textEdit_log.append('현재 페이지 : '+driver.current_url)
                #bsobj 초기화
                html = driver.page_source
                bsObj = BeautifulSoup(html, 'html.parser')
                #강의실의 이름을 변수에 저장
                strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
                #self.textEdit_log.append(strSubjectName)
                self.textEdit_log.append('현재 강의실은 : '+strSubjectName)

                #학습자료 찾기
                hakJaRyoUrl = bsObj.find('a', text='학습자료')['href']

                #self.textEdit_log.append(mainUrl+hakJaRyoUrl)
                #학습자료 테이블 페이지로 이동
                driver.get(mainUrl+hakJaRyoUrl)
                time.sleep(self.SLEEPTIME)
                #self.textEdit_log.append('현재 페이지 : '+driver.current_url)
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
                        self.textEdit_log.append('#검색된 글의 총 갯수 : {}' .format(totalCntTuplePages))
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
                            #self.textEdit_log.append(strSaveDir)
                            # 학습자료 튜플 페이지에서 다운로드 링크들을 찾음
                            for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileInHakJaRyoTuplePage(tuplePageHtml), tuplePage['no']):
                                # saveDir 위치에 파일 다운
                                self.downfile.downFile(dictFile['name'],mainUrl+dictFile['url'],strSaveDir)
                                time.sleep(self.SLEEPTIME)
                            self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                            self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
                    else :
                        self.textEdit_log.append('#검색 된 글이 없습니다.')
                        self.increasePregress(47/totalCntLectureRoom)
                        self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
            self.progress = 50.0
            self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
            ########################################################
            #  과제 다운

            self.textEdit_log.append('###과제 다운로드')
            for strLectureRoomLink in lstLectureRoomLinks:
                
                #각 강의실로 이동
                driver.get(mainUrl+strLectureRoomLink)
                #self.textEdit_log.append('현재 페이지 : '+driver.current_url)
                time.sleep(self.SLEEPTIME)
                #bsobj 초기화
                html = driver.page_source
                bsObj = BeautifulSoup(html, 'html.parser')
                #강의실의 이름을 변수에 저장
                strSubjectName = bsObj.find('p',{'class','subject-list'}).get_text()
                self.textEdit_log.append('#현재 강의실은 : '+strSubjectName)
                        

                #과 제 찾기
                KuaJeaUrl = bsObj.find('a', text='과 제')['href']

                #self.textEdit_log.append(mainUrl+KuaJeaUrl)
                #과제 테이블 페이지로 이동
                driver.get(mainUrl+KuaJeaUrl)
                #self.textEdit_log.append('현재 페이지 : '+driver.current_url)
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
                    #self.textEdit_log.append('현재 페이지 : '+driver.current_url)
                    time.sleep(self.SLEEPTIME)
                    #self.textEdit_log.append('현재 URL : '+ mainUrl+link)
                    #과제 테이블 페이지의 html 소스를 변수에 저장
                    tablePageHtml = driver.page_source
                    # 과제 테이블 페이지에 튜플(게시글)이 존재할경우에만 탐색
                    if scrapEngineLib.boolIsExistTupleInKuaJeaTablePage(tablePageHtml) is True:
                        

                        if os.path.isdir(strSubjectName) is False:
                            os.makedirs(strSubjectName)
                        #각 과제 튜플 페이지를 탐색
                        tuplePages = scrapEngineLib.lstFindTuplePageLinks(tablePageHtml)
                        totalCntTuplePages = len(tuplePages)
                        self.textEdit_log.append('#검색된 과제의 총 갯수 : {}'.format(totalCntTuplePages))
                        for tuplePage in tuplePages:
                            # 과제 튜플 페이지로 이동
                            driver.get(mainUrl + tuplePage['url'])
                            #time.sleep(self.SLEEPTIME)
                            # 과제 튜플 페이지의 html 소스를 변수에 저장
                            tuplePageHtml = driver.page_source
                            
                            
                            # 제출된 과제인지 확인
                            
                            if scrapEngineLib.boolIsSumittedKuaJea(tuplePageHtml) is True:
                                self.textEdit_log.append('#제출한 과제입니다.')
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
                                    self.textEdit_log.append('현재 페이지에는 파일이 존재합니다.')
                                    
                                    
                                    # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                                    for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileinKuaJeaInSubmitInfo(submitInfoPageHtml), tuplePage['no']):
                                        # saveDir 위치에 파일 다운
                                        
                                        if 'nameProf' in dictFile:
                                            self.downfile.downFile(dictFile['nameProf'],mainUrl+dictFile['urlProf'],strSaveDir)
                                            #self.textEdit_log.append('저장 파일명 : '+ dictFile['nameProf'])
                                            #self.textEdit_log.append('저장 파일의 URL : '+ dictFile['urlProf'])
                                        if 'nameStd' in dictFile:    
                                            self.downfile.downFile(dictFile['nameStd'],mainUrl+dictFile['urlStd'],strSaveDir)
                                            #self.textEdit_log.append('저장 파일명 : '+ dictFile['nameStd'])
                                            #self.textEdit_log.append('저장 파일의 URL : '+ dictFile['urlStd'])
                                        time.sleep(self.SLEEPTIME)
                                        self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                                        self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
                                else:
                                    self.textEdit_log.append('현재 페이지에는 파일이 존재하지 않습니다.') 
                                    self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                                    self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
                                
                                    
                                        
                            else :
                                # 미제출된 과제의 경우 처리
                                self.textEdit_log.append('#미제출한 과제입니다.')

                                # 파일을 다운로드할 위치지정
                                strSaveDir = self.DOWNLOADPATH+'/'+strSubjectName + '/과제'
                                
                                #페이지 html을 저장
                                htmlName = scrapEngineLib.changeFileNameForAll('_'+ tuplePage['name']+'.html',tuplePage['no'])
                                self.downfile.downHtml(htmlName,tuplePageHtml,strSaveDir)
                                #####################
                                

                                if scrapEngineLib.boolIsExistFile(tuplePageHtml) is True:
                                    self.textEdit_log.append('현재 페이지에는 파일이 존재합니다.')
                                    
                                    #self.textEdit_log.append('파일 저장 위치 : '+strSaveDir)
                                    # 과제 튜플 페이지에서 다운로드 링크들을 찾음
                                    
                                    for dictFile in scrapEngineLib.changeFileNameForAll(scrapEngineLib.lstFindFileInUnsubmittedKuaJeaPage(tuplePageHtml), tuplePage['no']):
                                        # saveDir 위치에 파일 다운
                                        if 'name' in dictFile:
                                            self.downfile.downFile(dictFile['name'],mainUrl+dictFile['url'],strSaveDir)
                                           
                                        time.sleep(self.SLEEPTIME)
                                else:
                                    self.textEdit_log.append('현재 페이지에는 파일이 존재하지 않습니다.')
                            self.increasePregress(47/totalCntLectureRoom/totalCntTuplePages)
                            self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
                    else:
                        self.textEdit_log.append('#등록된 과제가 없습니다.')
                        self.increasePregress(47/totalCntLectureRoom)
                        self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
            self.progress=100.0
            self.textEdit_log.append('##progress : '+'{:04.2f}%' .format(self.progress))
            self.textEdit_log.append('완료!')
        except Exception:
            traceback.print_exc()
        
        
        #driver.quit()
    

if __name__ == '__main__':
        #initial UI
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = AppWindow()
    ui.setupUi(Dialog_scrap)
    ui.initAll()
    Dialog_scrap.show()
    sys.exit(app.exec_())





