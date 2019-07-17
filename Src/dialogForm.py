# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Src\scrapFileUi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_scrap(object):
    def setupUi(self, Dialog_scrap):
        Dialog_scrap.setObjectName("Dialog_scrap")
        Dialog_scrap.resize(291, 360)
        #lineEdit_selectedDir
        self.lineEdit_selectedDir = QtWidgets.QLineEdit(Dialog_scrap)
        self.lineEdit_selectedDir.setGeometry(QtCore.QRect(80, 12, 141, 20))
        self.lineEdit_selectedDir.setReadOnly(True)
        self.lineEdit_selectedDir.setObjectName("lineEdit_selectedDir")
        self.lineEdit_id = QtWidgets.QLineEdit(Dialog_scrap)
        self.lineEdit_id.setGeometry(QtCore.QRect(90, 162, 141, 20))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_pwd = QtWidgets.QLineEdit(Dialog_scrap)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(90, 192, 141, 20))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setDragEnabled(False)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.groupBox_downType = QtWidgets.QGroupBox(Dialog_scrap)
        self.groupBox_downType.setGeometry(QtCore.QRect(20, 82, 251, 71))
        self.groupBox_downType.setObjectName("groupBox_downType")
        self.radioButton_mkHakKuaDirs = QtWidgets.QRadioButton(self.groupBox_downType)
        self.radioButton_mkHakKuaDirs.setGeometry(QtCore.QRect(30, 40, 191, 16))
        self.radioButton_mkHakKuaDirs.setObjectName("radioButton_mkHakKuaDirs")
        self.radioButton_justName = QtWidgets.QRadioButton(self.groupBox_downType)
        self.radioButton_justName.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.radioButton_justName.setAutoFillBackground(False)
        self.radioButton_justName.setChecked(True)
        self.radioButton_justName.setObjectName("radioButton_justName")
        self.label_selectedDir = QtWidgets.QLabel(Dialog_scrap)
        self.label_selectedDir.setGeometry(QtCore.QRect(10, 12, 56, 16))
        self.label_selectedDir.setObjectName("label_selectedDir")
        self.label_id = QtWidgets.QLabel(Dialog_scrap)
        self.label_id.setGeometry(QtCore.QRect(30, 162, 41, 16))
        self.label_id.setObjectName("label_id")
        self.label_pwd = QtWidgets.QLabel(Dialog_scrap)
        self.label_pwd.setGeometry(QtCore.QRect(20, 192, 51, 16))
        self.label_pwd.setObjectName("label_pwd")
        self.pushButton_start = QtWidgets.QPushButton(Dialog_scrap)
        self.pushButton_start.setGeometry(QtCore.QRect(60, 320, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_selectDir = QtWidgets.QPushButton(Dialog_scrap)
        self.pushButton_selectDir.setGeometry(QtCore.QRect(240, 12, 31, 23))
        self.pushButton_selectDir.setObjectName("pushButton_selectDir")
        self.textEdit_log = QtWidgets.QTextEdit(Dialog_scrap)
        self.textEdit_log.setGeometry(QtCore.QRect(20, 220, 251, 91))
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.pushButton_saveLog = QtWidgets.QPushButton(Dialog_scrap)
        self.pushButton_saveLog.setGeometry(QtCore.QRect(157, 320, 75, 23))
        self.pushButton_saveLog.setObjectName("pushButton_saveLog")
        self.lineEdit_subDirName = QtWidgets.QLineEdit(Dialog_scrap)
        self.lineEdit_subDirName.setGeometry(QtCore.QRect(100, 50, 121, 20))
        self.lineEdit_subDirName.setObjectName("lineEdit_subDirName")
        self.label_subDirName = QtWidgets.QLabel(Dialog_scrap)
        self.label_subDirName.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_subDirName.setObjectName("label_subDirName")

        self.retranslateUi(Dialog_scrap)
        QtCore.QMetaObject.connectSlotsByName(Dialog_scrap)
        Dialog_scrap.setTabOrder(self.lineEdit_selectedDir, self.pushButton_selectDir)
        Dialog_scrap.setTabOrder(self.pushButton_selectDir, self.lineEdit_subDirName)
        Dialog_scrap.setTabOrder(self.lineEdit_subDirName, self.radioButton_justName)
        Dialog_scrap.setTabOrder(self.radioButton_justName, self.radioButton_mkHakKuaDirs)
        Dialog_scrap.setTabOrder(self.radioButton_mkHakKuaDirs, self.lineEdit_id)
        Dialog_scrap.setTabOrder(self.lineEdit_id, self.lineEdit_pwd)
        Dialog_scrap.setTabOrder(self.lineEdit_pwd, self.textEdit_log)
        Dialog_scrap.setTabOrder(self.textEdit_log, self.pushButton_start)
        Dialog_scrap.setTabOrder(self.pushButton_start, self.pushButton_saveLog)

    def retranslateUi(self, Dialog_scrap):
        _translate = QtCore.QCoreApplication.translate
        Dialog_scrap.setWindowTitle(_translate("Dialog_scrap", "사이버 강의실 파일 다운"))
        self.groupBox_downType.setTitle(_translate("Dialog_scrap", "저장 방식 설정"))
        self.radioButton_mkHakKuaDirs.setText(_translate("Dialog_scrap", "학습자료/과제 디렉토리 생성"))
        self.radioButton_justName.setText(_translate("Dialog_scrap", "파일이름에 과제/학습노트 추가"))
        self.label_selectedDir.setText(_translate("Dialog_scrap", "저장 위치"))
        self.label_id.setText(_translate("Dialog_scrap", "아이디"))
        self.label_pwd.setText(_translate("Dialog_scrap", "비밀번호"))
        self.pushButton_start.setText(_translate("Dialog_scrap", "Start"))
        self.pushButton_selectDir.setText(_translate("Dialog_scrap", "..."))
        self.pushButton_saveLog.setText(_translate("Dialog_scrap", "Save Log"))
        self.label_subDirName.setText(_translate("Dialog_scrap", "하위 폴더 이름"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = Ui_Dialog_scrap()
    ui.setupUi(Dialog_scrap)
    Dialog_scrap.show()
    sys.exit(app.exec_())

