from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from PyQt6.QtSql import  *
import sqlite3
import sys

def minCT(row, m):
    i=0
    flag=True
    while flag:
        if row[i] != '#':
            minel=row[i]
            index = i
            flag=False
        i=i+1
    for i in range(m):
        if row[i]!='#':
            if float(row[i]) < float(minel):
                minel = row[i]
                index = i
    return index
def CT0(MC, MT, n, m):
    for i in range(n):
        indmin=minCT(MC[i], m)
        for j in range(m):
            if float(MT[i][j])>float(MT[i][indmin]):
                MC[i][j]='#'
                MT[i][j]='#'
    Data=[MC,MT]
    return Data

def CT1(C0, T0, n, m, Tz):
    print('работает')
    min_massT=[]
    for i in range(n):
        ind=minCT(T0[i], m)
        min_massT.append(float(T0[i][ind]))
    print('min_massT')
    print(min_massT)
    for i in range(n):
        sum = 0
        for j in range(i):
            sum=sum+min_massT[j]
        for j in range(i+1,n):
            sum = sum + min_massT[j]
        for j in range(m):
            if T0[i][j]!='#':
                if ((sum+float(T0[i][j]))>float(Tz)):
                    T0[i][j]='#'
                    C0[i][j]='#'
    Data=[C0,T0]
    return Data

def Tree(С1, T1, n, m):
    for



class MainWindow(QMainWindow):
    matrC=[]
    matrT=[]
    n=0
    m=0
    Tz=0
    matrС0=[]
    matrT0=[]
    matrС1 = []
    matrT1 = []
    treeMass=[]
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
        self.LoadData.clicked.connect(self.LoadBrow)
        self.errorN.setVisible(False)
        self.errorM.setVisible(False)
        self.errorTz.setVisible(False)

    def LoadBrow(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'Data\ ', '(*.txt)')
        f = open(fname[0], 'r')
        Data=f.read()
        f.close()
        Data = Data.split('\n\n')
        self.matrC=Data[0].split('\n')
        for i in range(len(self.matrC)):
            self.matrC[i]=self.matrC[i].split(' ')
        self.matrT = Data[1].split('\n')
        for i in range(len(self.matrT)):
            self.matrT[i]=self.matrT[i].split(' ')
        self.Tz=int(Data[2])
        self.TzLine.setText(str(self.Tz))
        self.n=len(self.matrC)
        self.nLine.setText(str(self.n))
        self.m = len(self.matrC[0])
        self.mLine.setText(str(self.m))
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
        for i in range(self.n):
            for j in range(self.m):
                Line0C = QtWidgets.QLineEdit()
                Line0T = QtWidgets.QLineEdit()
                Line0T.setValidator(QDoubleValidator())
                Line0C.setValidator(QDoubleValidator())
                self.CMatr.setCellWidget(i, j, Line0C)
                self.TMatr.setCellWidget(i, j, Line0T)
        for i in range(self.n):
            for j in range(self.m):
                self.CMatr.cellWidget(i, j).setText(self.matrC[i][j])
                self.TMatr.cellWidget(i, j).setText(self.matrT[i][j])


    def clickOk(self):
        if (self.nLine.text()!='' and self.mLine.text()!=''):
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
                        Line0T.setValidator(QDoubleValidator())
                        Line0C.setValidator(QDoubleValidator())
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
        if self.TzLine.text()!='' and self.nLine.text()!='' and self.mLine.text()!='':
            self.Tz=float(self.TzLine.text())
            self.errorTz.setVisible(False)
            self.matrC = []
            self.matrT = []
            for i in range(self.n):
                self.matrC.append([])
                self.matrT.append([])
                for j in range(self.m):
                    self.matrC[i].append(self.CMatr.cellWidget(i, j).text())
                    self.matrT[i].append(self.TMatr.cellWidget(i, j).text())
            for i in range(self.n):
                for j in range(self.m):
                    for b1 in range(len(self.matrC[i][j])):
                        if self.matrC[i][j][b1]==',':
                            bufC =self.matrC[i][j].split(',')
                            self.matrC[i][j]=bufC[0]+'.'+bufC[1]
                    for b2 in range(len(self.matrT[i][j])):
                        if self.matrT[i][j][b2]==',':
                            bufT = self.matrT[i][j].split(',')
                            self.matrT[i][j]=bufT[0]+'.'+bufT[1]
            print('C:')
            for i in self.matrC:
                print(i)
            print('T:')
            for i in self.matrT:
                print(i)


            Data0 = CT0(self.matrC, self.matrT, self.n, self.m)
            self.matrС0 = Data0[0]
            self.matrT0 = Data0[1]


            print('C0:')
            for i in range(self.n):
                print(self.matrС0[i])
            print('T0:')
            for i in range(self.n):
                print(self.matrT0[i])


            Data1 = CT1(self.matrС0, self.matrT0, self.n, self.m, self.Tz)
            self.matrС1=Data1[0]
            self.matrT1 = Data1[1]


            print('C1:')
            for i in range(self.n):
                print(self.matrС1[i])
            print('T1:')
            for i in range(self.n):
                print(self.matrT1[i])






        else:
            self.errorTz.setVisible(True)
            self.errorTz.setText('Заполните данные')



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
