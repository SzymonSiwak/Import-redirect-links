
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from bazaPt1 import UiMainWindow
import sys
from bazaModel import Model
import mysql.connector
import pandas as pd
from pathlib import Path
import os

class MainWindowUIClass( UiMainWindow ):
    def __init__( self ):
        super().__init__()
        self.model = Model()
        
    def setupUi( self, MW ):
        #Setup the UI of the super class, and add here code that relates to the way we want our UI to operate.
        super().setupUi( MW )


    def debugPrint( self, msg ):
        #Print the message in the text edit at the bottom of the horizontal splitter.
        self.debugTextBrowser.append( msg )

    def refreshAll( self ):
        #Updates the widgets whenever an interaction happens.
        self.lineEdit.setText( self.model.getFileName() )
        self.textEdit.setText( self.model.getFileContents() )
    
    
    def returnPressedSlot( self ):
        #Called when the user enters a string in the line edit and presses the ENTER key.
        fileName =  self.lineEdit.text()
        if self.model.isValid( fileName ):
            self.model.setFileName( self.lineEdit.text() )
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText( "" )
            self.refreshAll()
            self.debugPrint( "Invalid file specified: " + fileName  )

    
    def writeDocSlot( self ):
        #Called when the user presses the Write-Doc button.
        self.model.writeDoc( self.textEdit.toPlainText() )
        self.debugPrint( "WriteDoc button pressed!" )
        
    
    def browseSlot( self ):
        #Called when the user presses the Browse button
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "Text Files (*.txt)",
                        #"Text Files (*.txt);;Excel Files (*.xlsx)",
                        options=options)
        if fileName:
            self.debugPrint( "setting file name: " + fileName )
            self.model.setFileName( fileName )
            self.refreshAll()
        
    
    
    def saveSlot(self):
        self.question1 ="INSERT INTO " 
        self.question2 = "(enabled, redirect_from, redirect_from_type, redirect_to, redirect_to_type, redirect_type) VALUES(1, " 
        self.question3 = ", 'Page', 'https://prawowroclaw.edu.pl', 'Page', 301);" 
        self.f = self.textEdit.toPlainText()
        self.tabel = self.lineEdit6.text()
        self.fileName = self.lineEdit7.text()
        if self.fileName=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę pliku do zapisu.")
            display = msg.exec_()
        elif self.tabel=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę tabeli.")
            display = msg.exec_()
        elif self.f=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Wczytaj plik.")
            display = msg.exec_()
        else:
            count=0
            self.f = self.f.replace('https', '\nhttps').split("\n")
            desktop = os.path.expanduser("~\Desktop")  #getting user path to desktop directory
            self.txtFile = open(desktop+"\ "+self.fileName+".txt", "w") 
            for i in self.f:
                if i=="":
                    continue
                else:
                    self.txtFile.writelines(self.question1+"'"+self.tabel+"'"+self.question2+"'"+i+"'"+self.question3+"\n") 
                    count+=1
                    continue
            self.txtFile.close()
            msg = QMessageBox()
            msg.setWindowTitle("Potwierdzenie")
            msg.setText("Pomyślnie zapisano "+str(count)+" rekordy. Plik został zapisany na pulpicie.")
            display = msg.exec_()

        

    
    def sendSlot(self):
        self.question1 ="INSERT INTO " 
        self.question2 = "(enabled, redirect_from, redirect_from_type, redirect_to, redirect_to_type, redirect_type) VALUES(1, " 
        self.question3 = ", 'Page', 'https://prawowroclaw.edu.pl', 'Page', 301);" 
        self.user = self.lineEdit2.text()
        self.password = self.lineEdit3.text()
        self.host = self.lineEdit4.text()
        self.database = self.lineEdit5.text()
        self.tabel = self.lineEdit6.text()
        self.f = self.textEdit.toPlainText()
        if self.user=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę użytkownika.")
            display = msg.exec_()
        elif self.host=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę hosta.")
            display = msg.exec_()
        elif self.password=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj hasło.")
            display = msg.exec_()
        elif self.database=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę bazy.")
            display = msg.exec_()
        elif self.tabel=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Podaj nazwę tabeli.")
            display = msg.exec_()
        elif self.f=="":
            msg = QMessageBox()
            msg.setWindowTitle("Ostrzeżenie")
            msg.setText("Wczytaj plik.")
            display = msg.exec_()
        else:
            self.connection = mysql.connector.connect(host=self.host,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password) 
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)
                self.f = self.textEdit.toPlainText()
                count=0
                self.f = self.f.replace('https', ',https').split(",")    
                for i in self.f:
                    if i=="":
                        continue
                    else:
                        self.cursor.execute(self.question1+self.tabel+self.question2+"'"+i+"'"+self.question3)
                        self.connection.commit()
                        count+=1
                        continue
                print(self.cursor.rowcount, "Records inserted successfully:")
                msg2 = QMessageBox()
                msg2.setWindowTitle("Potwierdzenie")
                msg2.setText("Pomyślnie przesłano "+str(count)+" rekord(y).")
                display = msg2.exec_()
                self.cursor.close()
                print("Connection closed")


        
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()