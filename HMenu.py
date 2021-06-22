# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from HTarihSec import Ui_WindowHTarihSec
from HKabul import Ui_WindowHKabul
from HBilgilerim import Ui_WindowHBilgilerim

class Ui_WindowHMenu(object):
    def setupUi(self, WindowHMenu):
        WindowHMenu.setObjectName("WindowHMenu")
        WindowHMenu.resize(359, 183)
        WindowHMenu.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowHMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 341, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btHYonlendir = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btHYonlendir.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btHYonlendir.setObjectName("btHYonlendir")
        self.verticalLayout_7.addWidget(self.btHYonlendir)
        self.btHBilgilerim = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btHBilgilerim.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btHBilgilerim.setObjectName("btHBilgilerim")
        self.verticalLayout_7.addWidget(self.btHBilgilerim)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        WindowHMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowHMenu)
        self.statusbar.setObjectName("statusbar")
        WindowHMenu.setStatusBar(self.statusbar)
      
        self.btHYonlendir.clicked.connect(self.yonlendir)
        self.btHBilgilerim.clicked.connect(self.WHB)

        self.retranslateUi(WindowHMenu)
        QtCore.QMetaObject.connectSlotsByName(WindowHMenu)
    
    def yonlendir(self):
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM yoneticiDurum""") 
        for i in im:
            a=i[1]
            b=i[2]
        vt.close()
        if(int(b)==1):
            self.WHK()
        if(int(a)==1):
            self.WHTS()
    def WHK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowHKabul()
        self.ui.setupUi(self.window)
        self.window.show() 
    def WHTS(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowHTarihSec()
        self.ui.setupUi(self.window)
        self.window.show()    
    def WHB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowHBilgilerim()
        self.ui.setupUi(self.window)
        self.window.show()    
    def retranslateUi(self, WindowHMenu):
        _translate = QtCore.QCoreApplication.translate
        WindowHMenu.setWindowTitle(_translate("WindowHMenu", "MainWindow"))
        self.btHYonlendir.setText(_translate("WindowHMenu", "Yönlendir"))
        self.btHBilgilerim.setText(_translate("WindowHMenu", "Bilgilerim"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowHMenu = QtWidgets.QMainWindow()
    ui = Ui_WindowHMenu()
    ui.setupUi(WindowHMenu)
    WindowHMenu.show()
    sys.exit(app.exec_())

