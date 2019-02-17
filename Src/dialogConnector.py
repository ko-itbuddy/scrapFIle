###################################
# UI part
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogForm import Ui_Dialog_scrap



class AppWindow(Ui_Dialog_scrap):
    def initAll(self):
        #init
        self.init()
        #actions
        self.actions()

        #self.actionOntoolButton_selectDir()
#init
    def init(self):
        #progressBar
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
        #groupBox_mkSubDir
        #radioButton_mkSubDir
        #radioButton_notMkSubdir
        #lineEdit_subDirName
        self.lineEdit_subDirName.setText("portfolio")
        #label_subDirName
        #textEdit_log
        #pushButton_saveLog
        
#action connector      
    def actions(self):
        
        #progressBar
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
        #   pushButton_start.clicked
        self.pushButton_start.clicked.connect(self)
        #pushButton_selectDir
        #   pushButton_selectDir.clicked
        self.pushButton_selectDir.clicked.connect(self.showDirExprolerDialog)
        #groupBox_mkSubDir
        #radioButton_mkSubDir
        #   radioButton_mkSubDir
        self.radioButton_mkSubDir.released.connect(self.radioButton_mkSubDir_released)
        #radioButton_notMkSubdir
        #   radioButton_notMkSubdir
        self.radioButton_notMkSubdir.released.connect(self.radioButton_notMkSubdir_released)
        #lineEdit_subDirName
        #label_subDirName
        #textEdit_log
        #pushButton_saveLog
        self.pushButton_saveLog.clicked.connect(self.pushButton_saveLog_clicked)
    
   
#actions 
    def showDirExprolerDialog(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory(None, '다운로드 경로 지정', './')
        self.lineEdit_selectedDir.setText(dirName)
    
    def radioButton_notMkSubdir_released(self):
        self.lineEdit_subDirName.setReadOnly(True)
    
    def radioButton_mkSubDir_released(self):
        self.lineEdit_subDirName.setReadOnly(False)
    
    def pushButton_saveLog_clicked(self):
        fUrl = QtWidgets.QFileDialog.getSaveFileName(None, "로그 파일 저장위치", 'scrapLog.txt', "Images (*.txt)")
        
        with open(fUrl[0],'w', encoding='UTF-8') as f:
            f.write = self.textEdit_log.toPlainText()

    

#handler
    def get_textEdit_log(self):
        return self.textEdit_log

        

if __name__ == '__main__':
    #initial UI
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = AppWindow()
    ui.setupUi(Dialog_scrap)
    ui.initAll()
    Dialog_scrap.show()
    sys.exit(app.exec_())