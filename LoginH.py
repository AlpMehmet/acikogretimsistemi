# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from HMenu import Ui_WindowHMenu

class Ui_WindowHLogin(object):
    def setupUi(self, WindowHLogin):
        WindowHLogin.setObjectName("WindowHLogin")
        WindowHLogin.resize(375, 421)
        WindowHLogin.setMinimumSize(QtCore.QSize(375, 421))
        WindowHLogin.setMaximumSize(QtCore.QSize(375, 421))
        WindowHLogin.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowHLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 321, 363))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCep = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep.setObjectName("labelCep")
        self.verticalLayout_3.addWidget(self.labelCep)
        self.lineEditAd = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditAd.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEditAd.setObjectName("lineEditAd")
        self.verticalLayout_3.addWidget(self.lineEditAd)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTc = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelTc.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc.setObjectName("labelTc")
        self.verticalLayout_2.addWidget(self.labelTc)
        self.lineEditSifre = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditSifre.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEditSifre.setObjectName("lineEditSifre")
        self.verticalLayout_2.addWidget(self.lineEditSifre)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.pushButtonGiris = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonGiris.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.pushButtonGiris.setObjectName("pushButtonGiris")
        self.verticalLayout.addWidget(self.pushButtonGiris)
        WindowHLogin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowHLogin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 23))
        self.menubar.setObjectName("menubar")
        WindowHLogin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowHLogin)
        self.statusbar.setObjectName("statusbar")
        WindowHLogin.setStatusBar(self.statusbar)
        
        self.pushButtonGiris.clicked.connect(self.gir)

        self.retranslateUi(WindowHLogin)
        QtCore.QMetaObject.connectSlotsByName(WindowHLogin)
    def WHM(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowHMenu()
        self.ui.setupUi(self.window)
        WindowHLogin.hide()
        self.window.show()      
    def gir(self):
        ad=self.lineEditAd.text()
        no=self.lineEditSifre.text()
        print(str(ad))
        print(str(no))
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM hoca""")        
        for veri in im:
            print(str(veri[1]))
            print(str(veri[2]))
            if(str(veri[1]+" "+veri[2])==str(ad) and str(veri[4])==str(no)):                   
                self.WHM()
        vt.close()
    def retranslateUi(self, WindowHLogin):
        _translate = QtCore.QCoreApplication.translate
        WindowHLogin.setWindowTitle(_translate("WindowHLogin", "MainWindow"))
        self.labelCep.setText(_translate("WindowHLogin", "Ad-Soyad Giriniz:"))
        self.labelTc.setText(_translate("WindowHLogin", "Şifre:"))
        self.pushButtonGiris.setText(_translate("WindowHLogin", "Giriş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowHLogin = QtWidgets.QMainWindow()
    ui = Ui_WindowHLogin()
    ui.setupUi(WindowHLogin)
    WindowHLogin.show()
    sys.exit(app.exec_())

