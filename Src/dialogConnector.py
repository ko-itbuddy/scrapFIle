###################################
# UI part
import sys, subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogForm import Ui_Dialog_scrap
from scrapEngine import ScrapEngneForYuhan
import threading






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
        print(self.lineEdit_id.text())
        print(self.lineEdit_pwd.text())
        print(self.lineEdit_selectedDir.text())
        strUSERID = self.lineEdit_id.text()
        strUSERPWD = self.lineEdit_pwd.text()
        strDOWNLOADPATH = self.lineEdit_selectedDir.text()
        boolMKSUBDIRS = False
        intSLEEPTIME = 2
        strTOPDIRNAME = self.lineEdit_subDirName.text()


        engine = ScrapEngneForYuhan(strUSERID, strUSERPWD, strDOWNLOADPATH,boolMKSUBDIRS, intSLEEPTIME, strTOPDIRNAME)
        #stream
        #process
        process = QtCore.QProcess()
        process.readyReadStandardError.connect( lambda: self.textEdit_log.append() )
        process.readyReadStandardOutput.connect( lambda: self.textEdit_log.append() )
        #self.process.setArguments('dir')
        process.start(engine.run())
        while True:
            self.textEdit_log.append(self.process.readStdout())
            if self.process.isRunning()==False:
                break
        
        
        '''
        while p.poll() != None:
            out = self.process
            if out == '':
                break
            if out != '':
                str(out,'utf-8'))
        self.textEdit_log.append(self.process.readChannel())
        '''
        #while p.poll() != None:
        #    out = p.stderr.read(1)
        #    if out == '':
        ##        break
        #    if out != '':
        #        str(out,'utf-8'))
                
        #self.process = QtCore.QProcess()
        #self.process(engine.run())

        



 
        

if __name__ == '__main__':
    #initial UI
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = AppWindow()
    ui.setupUi(Dialog_scrap)
    ui.initAll()
    Dialog_scrap.show()
    sys.exit(app.exec_())