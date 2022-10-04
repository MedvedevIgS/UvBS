from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator
import sys
import graphviz
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





def Tree(C1, T1, n, m, Tz):
    TreeMass = []
    okT = []
    okC = []
    min_massT = []
    for i in range(n):
        ind = minCT(T1[i], m)
        min_massT.append(float(T1[i][ind]))
    min_massC = []
    for i in range(n):
        ind = minCT(C1[i], m)
        min_massC.append(float(C1[i][ind]))
    inexmass = []
    for i in range(n):
        print('++++++++++++++++++++++++++++++++++++++++++')
        print('inexmass')
        print(inexmass)
        TreeMass.append([])
        ROWIND=-1
        for j in range(m):
            print(C1[i][j])
            if C1[i][j] != '#':
                ROWIND = ROWIND+1
                TreeMass[i].append([])
                sumT = 0
                sumC = 0
                print('ДО')
                print('sumT='+str(sumT)+' sumC='+str(sumC))
                for w in range(i+1, n):
                    sumT = sumT + min_massT[w]
                    sumC = sumC + min_massC[w]
                print('sumT=' + str(sumT) + ' sumC=' + str(sumC))
                for w in range(i):
                    sumT = sumT + okT[w]
                    sumC = sumC + okC[w]
                print('sumT=' + str(sumT) + ' sumC=' + str(sumC))

                sumT = sumT + float(T1[i][j])
                sumC = sumC + float(C1[i][j])
                print('После')
                print('sumT='+str(sumT) + ' sumC='+str(sumC))
                TreeMass[i][ROWIND].append(sumC)
                TreeMass[i][ROWIND].append(sumT)
                print("TreeMass[i]")
                print(TreeMass[i])
                bufindex = inexmass.copy()
                print('bufindex')
                print(bufindex)
                bufindex.append(j)
                print(bufindex)
                TreeMass[i][ROWIND].append(bufindex)
                print("TreeMass[i]")
                print(TreeMass[i])
        print('--------------------------------')
        print('inexmass')
        print(inexmass)
        ind_min = 0
        for j in range(len(TreeMass[i])):
            min_C_row = TreeMass[i][0][0]
            print('min_C_row')
            print(min_C_row)
            print(str(TreeMass[i][j][1])+'<='+str(Tz))
            print(str(min_C_row) + '<=' + str(TreeMass[i][j][0]))
            print(TreeMass[i][j][1] <= Tz and min_C_row >= TreeMass[i][j][0])
            if  TreeMass[i][j][1] <= Tz and min_C_row >= TreeMass[i][j][0]:
                inexmass = TreeMass[i][j][2]
                ind_min = TreeMass[i][j][2][-1]
        print('inexmass')
        print(inexmass)
        print('ind_min')
        print(ind_min)
        okT.append(float(T1[i][ind_min]))
        print('okT')
        print(okT)
        okC.append(float(C1[i][ind_min]))
        print('okC')
        print(okC)
        print('прошли строку')
    for i in TreeMass:
        print(i)
    return TreeMass


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
    min_massT=[]
    print(T0)
    for i in range(n):
        ind=minCT(T0[i], m)
        min_massT.append(float(T0[i][ind]))
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

class ResWindow(QMainWindow):
    n=0
    m=0
    T0=[]
    C0=[]
    C1=[]
    T1=[]
    def __init__(self):
        super(ResWindow, self).__init__()
        uic.loadUi("FormRes.ui", self)
        self.setWindowTitle("Результат")
        f = open("Res\\res.txt", 'r')
        Data=f.read()
        f.close()
        Data=Data.split('\n\n')
        self.C0=Data[0]
        self.C0=self.C0.split('\n')
        for i in range(len(self.C0)):
            self.C0[i]=self.C0[i].split(' ')

        self.n=len(self.C0)
        self.m = len(self.C0[0])
        self.T0 = Data[1]
        self.T0 = self.T0.split('\n')
        for i in range(len(self.T0)):
            self.T0[i] = self.T0[i].split(' ')

        self.C1 = Data[2]
        self.C1 = self.C1.split('\n')
        for i in range(len(self.C1)):
            self.C1[i] = self.C1[i].split(' ')

        self.T1= Data[3]
        self.T1 = self.T1.split('\n')
        for i in range(len(self.T1)):
            self.T1[i] = self.T1[i].split(' ')

        self.T0Matr.setRowCount(self.n)
        self.T0Matr.setColumnCount(self.m)
        self.C0Matr.setRowCount(self.n)
        self.C0Matr.setColumnCount(self.m)
        self.T1Matr.setRowCount(self.n)
        self.T1Matr.setColumnCount(self.m)
        self.C1Matr.setRowCount(self.n)
        self.C1Matr.setColumnCount(self.m)
        h = 25 + 30 * self.n
        w = 15 + 39 * self.m
        print(h)
        print(w)
        self.C0Matr.resize(QtCore.QSize(w, h))
        self.T0Matr.resize(QtCore.QSize(w, h))
        self.C1Matr.resize(QtCore.QSize(w, h))
        self.T1Matr.resize(QtCore.QSize(w, h))
        for i in range(self.m):
            self.T1Matr.setColumnWidth(i, 1)
            self.C1Matr.setColumnWidth(i, 1)
            self.T0Matr.setColumnWidth(i, 1)
            self.C0Matr.setColumnWidth(i, 1)
        for i in range(self.n):
            for j in range(self.m):
                Line0C0 = QtWidgets.QLineEdit()
                Line0T0 = QtWidgets.QLineEdit()
                Line0C1 = QtWidgets.QLineEdit()
                Line0T1 = QtWidgets.QLineEdit()
                Line0T0.setValidator(QDoubleValidator())
                Line0C0.setValidator(QDoubleValidator())
                Line0T1.setValidator(QDoubleValidator())
                Line0C1.setValidator(QDoubleValidator())
                self.C0Matr.setCellWidget(i, j, Line0C0)
                self.T0Matr.setCellWidget(i, j, Line0T0)
                self.C1Matr.setCellWidget(i, j, Line0C1)
                self.T1Matr.setCellWidget(i, j, Line0T1)
        for i in range(self.n):
            for j in range(self.m):
                self.C0Matr.cellWidget(i, j).setText(self.C0[i][j])
                self.T0Matr.cellWidget(i, j).setText(self.T0[i][j])
                self.C1Matr.cellWidget(i, j).setText(self.C1[i][j])
                self.T1Matr.cellWidget(i, j).setText(self.T1[i][j])




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
            flagTz=True
            while flagTz:
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
                            if self.matrC[i][j][b1] == ',':
                                bufC = self.matrC[i][j].split(',')
                                self.matrC[i][j] = bufC[0] + '.' + bufC[1]
                        for b2 in range(len(self.matrT[i][j])):
                            if self.matrT[i][j][b2] == ',':
                                bufT = self.matrT[i][j].split(',')
                                self.matrT[i][j] = bufT[0] + '.' + bufT[1]
                print('C:')
                for i in self.matrC:
                    print(i)
                print('T:')
                for i in self.matrT:
                    print(i)
                Data0 = CT0(self.matrC, self.matrT, self.n, self.m)
                self.matrC0 = Data0[0]
                self.matrT0 = Data0[1]
                fw = open("Res\\res.txt", 'w')
                print('C0:')
                for i in self.matrC0:
                    print(i)

                for i in range(self.n):
                    stroka = ''
                    for j in range(self.m):
                        stroka = stroka + self.matrC0[i][j] + ' '
                    stroka = stroka[:-1] + '\n'
                    fw.write(stroka)
                fw.write('\n')
                print('T0:')
                for i in self.matrT0:
                    print(i)

                for i in range(self.n):
                    stroka = ''
                    for j in range(self.m):
                        stroka = stroka + self.matrT0[i][j] + ' '
                    stroka = stroka[:-1] + '\n'
                    fw.write(stroka)
                fw.write('\n')

                Data1 = CT1(self.matrC0, self.matrT0, self.n, self.m, self.Tz)
                self.matrC1 = Data1[0]
                self.matrT1 = Data1[1]
                flagempty_row = True
                i=0
                while flagempty_row and i < self.n:
                    flagempty_row = False
                    for j in range(self.m):
                        if self.matrC1[i][j] != '#':
                            flagempty_row = True
                    i = i + 1
                if flagempty_row:
                    flagTz=False
                else:
                    print('Подбор')
                    self.errorTz.setVisible(True)
                    self.errorTz.setText('Подбор минимальной Tз')
                    print('Подбор')
                    self.Tz=self.Tz+0.5
                    print('Подбор')
                    print(flagTz)

            self.TzLine.setText(str(self.Tz))
            print('C1:')
            for i in self.matrC1:
                print(i)

            for i in range(self.n):
                stroka = ''
                for j in range(self.m):
                    stroka = stroka + self.matrC1[i][j] + ' '
                stroka = stroka[:-1] + '\n'
                fw.write(stroka)
            fw.write('\n')

            print('T1:')
            for i in self.matrT1:
                print(i)

            for i in range(self.n):
                stroka = ''
                for j in range(self.m):
                    stroka = stroka + self.matrT1[i][j] + ' '
                if i == self.n - 1 and j == self.m - 1:
                    stroka = stroka[:-1]
                else:
                    stroka = stroka[:-1] + '\n'
                fw.write(stroka)
            fw.close()
            self.treeMass = Tree(self.matrC1, self.matrT1, self.n, self.m, self.Tz)
            global widget2
            Res = ResWindow()
            widget2 = QtWidgets.QStackedWidget()
            widget2.addWidget(Res)
            widget2.setMinimumWidth(795)
            widget2.setMinimumHeight(595)
            widget2.show()

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
