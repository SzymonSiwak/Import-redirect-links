import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class UiMainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.debugTextBrowser.setGeometry(QtCore.QRect(80, 480, 641, 61))     #80, 460, 641, 81
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 31, 631, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 411, 31))
        self.lineEdit.setObjectName("lineEdit")

        #Frame for user name, password, host name, database name labels and textboxes
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(90, 341, 641, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        #User name label, textbox
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit2.setGeometry(QtCore.QRect(140, 20, 151, 21))
        self.lineEdit2.setObjectName("textEdit2")
        
        #User password label, textbox
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit3.setGeometry(QtCore.QRect(140, 60, 151, 20))
        self.lineEdit3.setObjectName("lineEdit3")
        
        #Host name label, textbox
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(320, 20, 71, 21))
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit4.setGeometry(QtCore.QRect(420, 20, 151, 20))
        self.lineEdit4.setObjectName("lineEdit4")
        
        #Database name label, textbox
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 101, 21))
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit5.setGeometry(QtCore.QRect(420, 60, 151, 20))
        self.lineEdit5.setObjectName("lineEdit5")

        #Tabel name label, textbox
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(320, 100, 91, 16))
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit6.setGeometry(QtCore.QRect(420, 100, 151, 20))
        self.lineEdit6.setObjectName("lineEdit6")

        #File name label, textbox
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 121, 20))
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit7.setGeometry(QtCore.QRect(140, 100, 151, 20))
        self.lineEdit7.setObjectName("lineEdit7")
         

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(530, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(100, 50, 411, 211))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 270, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 270, 81, 31))   
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 270, 81, 31))   
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.browseSlot)           
        self.pushButton_2.clicked.connect(self.writeDocSlot)         
        self.pushButton_3.clicked.connect(self.sendSlot)
        self.pushButton_4.clicked.connect(self.saveSlot) 
        self.lineEdit.returnPressed.connect(self.returnPressedSlot)  
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nazwa pliku"))
        self.label_2.setText(_translate("MainWindow", "Nazwa użytkownika"))
        self.label_3.setText(_translate("MainWindow", "Hasło"))
        self.label_4.setText(_translate("MainWindow", "Host"))
        self.label_5.setText(_translate("MainWindow", "Nazwa bazy"))
        self.label_6.setText(_translate("MainWindow", "Nazwa tabeli"))
        self.label_7.setText(_translate("MainWindow", "Nazwa pliku do zapisu"))
        self.pushButton.setText(_translate("MainWindow", "Przeglądaj"))
        self.pushButton_2.setText(_translate("MainWindow", "Pokaż"))
        self.pushButton_3.setText(_translate("MainWindow", "Wyślij"))
        self.pushButton_4.setText(_translate("MainWindow", "Zapisz"))
        
        
    @pyqtSlot( )
    def returnPressedSlot( self ):
        pass

    @pyqtSlot( )
    def writeDocSlot( self ):
        pass

    @pyqtSlot( )
    def browseSlot( self ):
        pass

    @pyqtSlot( )
    def sendSlot( self ):
        pass

    @pyqtSlot( )
    def saveSlot( self ):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
