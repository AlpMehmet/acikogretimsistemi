# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from YSoruEkle import Ui_WindowYSoruEkle
from YSinavTarihEkle import Ui_WindowYSinavTarihEkle
from YYEkle import Ui_WindowYYEkle
from YSalonEkle import Ui_WindowYSalonEkle
from YHocaEkle import Ui_WindowYHocaEkle
from YOgrenciEkle import Ui_WindowYOEkle
class Ui_WindowMEkle(object):
    def setupUi(self, WindowMEkle):
        WindowMEkle.setObjectName("WindowMEkle")
        WindowMEkle.resize(442, 447)
        WindowMEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 411, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btSoruEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSoruEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSoruEkle.setObjectName("btSoruEkle")
        self.verticalLayout.addWidget(self.btSoruEkle)
        self.btSTEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSTEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSTEkle.setObjectName("btSTEkle")
        self.verticalLayout.addWidget(self.btSTEkle)
        self.btYonEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btYonEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btYonEkle.setObjectName("btYonEkle")
        self.verticalLayout.addWidget(self.btYonEkle)
        self.btOgrenciEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btOgrenciEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btOgrenciEkle.setObjectName("btOgrenciEkle")
        self.verticalLayout.addWidget(self.btOgrenciEkle)
        self.btSalonEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSalonEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSalonEkle.setObjectName("btSalonEkle")
        self.verticalLayout.addWidget(self.btSalonEkle)
        self.btHocaEkle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btHocaEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btHocaEkle.setObjectName("btHocaEkle")
        self.verticalLayout.addWidget(self.btHocaEkle)
        WindowMEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 23))
        self.menubar.setObjectName("menubar")
        WindowMEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMEkle)
        self.statusbar.setObjectName("statusbar")
        WindowMEkle.setStatusBar(self.statusbar)
        
        self.btHocaEkle.clicked.connect(self.WHE)
        self.btSalonEkle.clicked.connect(self.WYSE)
        self.btSoruEkle.clicked.connect(self.WSE)
        self.btSTEkle.clicked.connect(self.WSTE)
        self.btYonEkle.clicked.connect(self.WYE)
        self.btOgrenciEkle.clicked.connect(self.WOE)
        self.retranslateUi(WindowMEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowMEkle)
        
    def WSE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYSoruEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def WSTE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYSinavTarihEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def WYE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYYEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def WYSE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYSalonEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def WHE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYHocaEkle()
        self.ui.setupUi(self.window)
        self.window.show()    
    def WOE(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYOEkle()
        self.ui.setupUi(self.window)
        self.window.show()   
    def retranslateUi(self, WindowMEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowMEkle.setWindowTitle(_translate("WindowMEkle", "MainWindow"))
        self.btSoruEkle.setText(_translate("WindowMEkle", "Soru Ekle"))
        self.btSTEkle.setText(_translate("WindowMEkle", "Sınav Tarihi Ekle"))
        self.btYonEkle.setText(_translate("WindowMEkle", "Yönetici Ekle"))
        self.btOgrenciEkle.setText(_translate("WindowMEkle", "Öğrenci Ekle"))
        self.btSalonEkle.setText(_translate("WindowMEkle", "Salon Ekle"))
        self.btHocaEkle.setText(_translate("WindowMEkle", "Hoca Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowMEkle()
    ui.setupUi(WindowMEkle)
    WindowMEkle.show()
    sys.exit(app.exec_())

