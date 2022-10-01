from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator
from PyQt6.QtSql import  *
import sqlite3
import sys

class MainWindow(QMainWindow):
    matrC=[]
    matrT=[]
    n=0
    m=0
    Tz=0
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("FormApp.ui", self)
        self.setWindowTitle("LR_UvBS")
        Matr=QtWidgets.QTableWidget()
        Matr = QtWidgets.QPushButton()
        Matr = QtWidgets.QLineEdit()
        Matr.setValidator(QIntValidator())
        self.nLine.setValidator(QIntValidator())
        self.mLine.setValidator(QIntValidator())
        self.TzLine.setValidator(QIntValidator())
        self.ButOk.clicked.connect(self.clickOk)
        self.ButRes.clicked.connect(self.clickRes)
        self.ButClear.clicked.connect(self.clickClear)
        self.errorN.setVisible(False)
        self.errorM.setVisible(False)
        self.errorTz.setVisible(False)

    def clickOk(self):
        if (self.nLine.text()!='' and self.mLine.text()!=''):
            print('работает 1')
            print(int(self.nLine.text())>0 and int(self.mLine.text())>0)
            if (int(self.nLine.text())>0 and int(self.mLine.text())>0):
                self.n = int(self.nLine.text())
                self.m = int(self.mLine.text())
                self.errorN.setVisible(False)
                self.errorM.setVisible(False)
                self.errorN.setText('')
                self.errorM.setText('')
                self.TMatr.setRowCount(self.n)
                self.TMatr.setColumnCount(self.m)
                self.CMatr.setRowCount(self.n)
                self.CMatr.setColumnCount(self.m)
                h = 25 + 30 * self.n
                w = 15 + 39 * self.m
                self.CMatr.resize(QtCore.QSize(w, h))
                self.TMatr.resize(QtCore.QSize(w, h))
                for i in range(self.m):
                    self.TMatr.setColumnWidth(i, 1)
                    self.CMatr.setColumnWidth(i, 1)
                for i in range(int(self.CMatr.rowCount())):
                    for j in range(int(self.CMatr.columnCount())):
                        Line0C = QtWidgets.QLineEdit()
                        Line0C.setText('0')
                        Line0T = QtWidgets.QLineEdit()
                        Line0T.setText('0')
                        Line0T.setValidator(QIntValidator())
                        Line0C.setValidator(QIntValidator())
                        self.CMatr.setCellWidget(i, j, Line0C)
                        self.TMatr.setCellWidget(i, j, Line0T)
            else:
                if int(self.nLine.text())<=0:
                    self.errorN.setVisible(True)
                    self.errorN.setText('Введите число больше 0')
                    if int(self.mLine.text()) <= 0:
                        self.errorM.setVisible(True)
                        self.errorM.setText('Введите число больше 0')
                    else:
                        self.errorM.setVisible(False)
                        self.errorM.setText('')
                if int(self.mLine.text())<=0:
                    self.errorM.setVisible(True)
                    self.errorM.setText('Введите число больше 0')
                    if int(self.nLine.text())<=0:
                        self.errorN.setVisible(True)
                        self.errorN.setText('Введите число больше 0')
                    else:
                        self.errorN.setVisible(False)
                        self.errorN.setText('')
        elif self.nLine.text() == '':
            self.errorN.setVisible(True)
            self.errorN.setText('Введите колличество строк')
            if self.mLine.text() == '':
                self.errorM.setVisible(True)
                self.errorM.setText('Введите колличество столбцов')
            else:
                self.errorM.setVisible(False)
                self.errorM.setText('')
        elif self.mLine.text() == '':
            self.errorM.setVisible(True)
            self.errorM.setText('Введите колличество столбцов')
            if self.nLine.text() == '':
                self.errorN.setVisible(True)
                self.errorN.setText('Введите колличество столбцов')
            else:
                self.errorN.setVisible(False)
                self.errorN.setText('')
    def clickRes(self):
        if self.TzLine.text()!='':
            self.errorTz.setVisible(False)
            self.matrC = []
            self.matrT = []
            print('работает')
            for i in range(self.n):
                self.matrC.append([])
                self.matrT.append([])
                for j in range(self.m):
                    self.matrC[i].append(int(self.CMatr.cellWidget(i, j).text()))
                    self.matrT[i].append(int(self.TMatr.cellWidget(i, j).text()))
            for i in self.matrC:
                print(i)
        else:
            self.errorTz.setVisible(True)
            self.errorTz.setText('Введите Tz')



    def clickClear(self):
        for i in range(self.n):
            for j in range(self.m):
                self.CMatr.cellWidget(i, j).setText('0')
                self.TMatr.cellWidget(i, j).setText('0')



def application():
    app=QApplication(sys.argv)
    window=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setMinimumWidth(780)
    widget.setMinimumHeight(420)
    widget.show()
    app.exec()

if __name__ == "__main__":
    application()





