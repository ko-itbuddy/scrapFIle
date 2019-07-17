import sys
from PyQt5 import QtWidgets,QtCore, QtWidgets

class Ui_Dialog_scrap(object):
    def setupUi(self, Dialog_scrap):
        
        Dialog_scrap.setObjectName("Dialog_scrap")
        Dialog_scrap.resize(291, 455)
        self.initUI()

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.output.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        self.process.start('ping',['127.0.0.1'])

    def initUI(self):
        # Layout are better for placing widgets
        layout = QtWidgets.QHBoxLayout()
        self.runButton = QtWidgets.QPushButton('Run')
        self.runButton.clicked.connect(self.callProgram)

        self.output = QtWidgets.QTextEdit()

        layout.addWidget(self.output)
        layout.addWidget(self.runButton)

        

        # QProcess object for external app
        self.process = QtCore.QProcess()
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.runButton.setEnabled(False))
        self.process.finished.connect(lambda: self.runButton.setEnabled(True))


#Function Main Start

#Function Main END

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_scrap = QtWidgets.QDialog()
    ui = Ui_Dialog_scrap()
    ui.setupUi(Dialog_scrap)
    Dialog_scrap.show()
    sys.exit(app.exec_())