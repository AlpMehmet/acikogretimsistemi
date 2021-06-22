# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YYEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowYYEkle(object):
    def setupUi(self, WindowYYEkle):
        WindowYYEkle.setObjectName("WindowYYEkle")
        WindowYYEkle.resize(339, 406)
        self.centralwidget = QtWidgets.QWidget(WindowYYEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 321, 363))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCep = QtWidgets.QLabel(self.verticalLayoutWidget_2)
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
        self.leAd = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leAd.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leAd.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leAd.setObjectName("leAd")
        self.verticalLayout_3.addWidget(self.leAd)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelTc = QtWidgets.QLabel(self.verticalLayoutWidget_2)
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
        self.verticalLayout_4.addWidget(self.labelTc)
        self.leSifre = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leSifre.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leSifre.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leSifre.setObjectName("leSifre")
        self.verticalLayout_4.addWidget(self.leSifre)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.btSE = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btSE.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSE.setObjectName("btSE")
        self.verticalLayout_2.addWidget(self.btSE)
        WindowYYEkle.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowYYEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYYEkle.setStatusBar(self.statusbar)
        self.btSE.clicked.connect(self.ye)

        self.retranslateUi(WindowYYEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYYEkle)
    def ye(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()

        im.execute("""INSERT INTO  yonetici (isim,sifre) VALUES (?,?)""",(str(self.leAd.text()),str(self.leSifre.text())))   
        vt.commit()
        vt.close()
    def retranslateUi(self, WindowYYEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYYEkle.setWindowTitle(_translate("WindowYYEkle", "WindowYYEkle"))
        self.labelCep.setText(_translate("WindowYYEkle", "İsim:"))
        self.labelTc.setText(_translate("WindowYYEkle", "Şifre"))
        self.btSE.setText(_translate("WindowYYEkle", "Yönetici Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYYEkle = QtWidgets.QWindowYYEkle()
    ui = Ui_WindowYYEkle()
    ui.setupUi(WindowYYEkle)
    WindowYYEkle.show()
    sys.exit(app.exec_())

