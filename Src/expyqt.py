import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogForm import Ui_Dialog_scrap
import os

class AppWindow(Ui_Dialog_scrap):
    def initAll(self):
        self.initLineEdit_selectedDir()
        self.actionOntoolButton_selectDir()
        
        




    def initLineEdit_selectedDir(self):
        print(os.getcwd())
        dirName = os.getcwd()
        self.lineEdit_selectedDir.setText(dirName)
        
        
    def actionOntoolButton_selectDir(self):
        self.toolButton_selectDir.clicked.connect(self.showDirDialog)

    def showDirDialog(self):
        #dirName = QtWidgets.QFileDialog.getExistingDirectory(self, '다운로드 경로 지정', './')
        dirName = QtWidgets.QFileDialog.getExistingDirectory(None, '다운로드 경로 지정', './')
        self.lineEdit_selectedDir.setText(dirName)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = AppWindow()
    ui.setupUi(Dialog_scrap)
    ui.initAll()
    Dialog_scrap.show()
    sys.exit(app.exec_())