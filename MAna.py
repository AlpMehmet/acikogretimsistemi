# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAna.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from MEkle import Ui_WindowMEkle
from YMenu import Ui_WindowYonMenu
from MBak import Ui_WindowMBak

class Ui_WindowMAna(object):
    def setupUi(self, WindowMAna):
        WindowMAna.setObjectName("WindowMAna")
        WindowMAna.resize(525, 205)
        WindowMAna.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMAna)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btTS_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btTS_2.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btTS_2.setObjectName("btTS_2")
        self.verticalLayout.addWidget(self.btTS_2)
        self.btOgrenciYerlestir_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btOgrenciYerlestir_2.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btOgrenciYerlestir_2.setObjectName("btOgrenciYerlestir_2")
        self.verticalLayout.addWidget(self.btOgrenciYerlestir_2)
        self.btTS_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btTS_3.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btTS_3.setObjectName("btTS_3")
        self.verticalLayout.addWidget(self.btTS_3)
        WindowMAna.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowMAna)
        self.statusbar.setObjectName("statusbar")
        WindowMAna.setStatusBar(self.statusbar)
        
        self.btTS_2.clicked.connect(self.WME)
        self.btOgrenciYerlestir_2.clicked.connect(self.WYM)
        self.btTS_3.clicked.connect(self.WMB)

        self.retranslateUi(WindowMAna)
        QtCore.QMetaObject.connectSlotsByName(WindowMAna)
    def WME(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def WYM(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowYonMenu()
        self.ui.setupUi(self.window)
        self.window.show()
    def WMB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBak()
        self.ui.setupUi(self.window)
        self.window.show()
    def retranslateUi(self, WindowMAna):
        _translate = QtCore.QCoreApplication.translate
        WindowMAna.setWindowTitle(_translate("WindowMAna", "MainWindow"))
        self.btTS_2.setText(_translate("WindowMAna", "Ekleme Kısımları "))
        self.btOgrenciYerlestir_2.setText(_translate("WindowMAna", "Yerleştirme, Mail Atma İşlemleri Ve Başlatma Kısmı"))
        self.btTS_3.setText(_translate("WindowMAna", "Bakma Kısımları"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMAna = QtWidgets.QMainWindow()
    ui = Ui_WindowMAna()
    ui.setupUi(WindowMAna)
    WindowMAna.show()
    sys.exit(app.exec_())

