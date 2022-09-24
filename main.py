from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtSql import  *
import sqlite3
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("FormApp.ui", self)
        self.setWindowTitle("LR_UvBS")
        Matr=QtWidgets.QTableWidget()
        Matr.setColumnCount(3)
        Matr.setColumnWidth(0, 1)
        Matr = QtWidgets.QPushButton()
        Matr = QtWidgets.QLineEdit()
        Matr.setValidator(QIntValidator())
        self.nLine.setValidator(QIntValidator())
        self.mLine.setValidator(QIntValidator())
        self.TzLine.setValidator(QIntValidator())
        self.ButOk.clicked.connect(self.clickOk)
        self.errorN.setVisible(False)
        self.errorM.setVisible(False)
        #self.TMatr.setRowCount(3)
        #self.TMatr.setColumnCount(3)

    def clickOk(self):
        if (self.nLine.text()!='' and self.mLine.text()!=''):
            self.errorN.setVisible(False)
            self.errorM.setVisible(False)
            self.errorN.setText('')
            self.errorM.setText('')
            self.TMatr.setRowCount(int(self.nLine.text()))
            self.TMatr.setColumnCount(int(self.mLine.text()))
            self.CMatr.setRowCount(int(self.nLine.text()))
            self.CMatr.setColumnCount(int(self.mLine.text()))
            for i in range(int(self.mLine.text())):
                self.TMatr.setColumnWidth(i, 1)
                self.CMatr.setColumnWidth(i, 1)
        if self.nLine.text() == '':
            self.errorN.setVisible(True)
            self.errorN.setText('Введите колличество строк')
        else:
            self.errorN.setVisible(False)
            self.errorN.setText('')
        if self.mLine.text() == '':
            self.errorM.setVisible(True)
            self.errorM.setText('Введите колличество столбцов')
        else:
            self.errorM.setVisible(False)
            self.errorM.setText('')


def application():
    app=QApplication(sys.argv)
    window=MainWindow()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setMinimumWidth(1100)
    widget.setMinimumHeight(600)
    widget.show()
    app.exec()

if __name__ == "__main__":
    application()





