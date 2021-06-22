# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBak.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from MBO import Ui_WindowMBO
from MBK import Ui_WindowMBK
from MBH import Ui_WindowMBH

from MBOG import Ui_WindowMBOG
from MBYOG import Ui_WindowMBYOG
from MBHOCA import Ui_WindowMBHOCA
from MBYH import Ui_WindowMBYH
class Ui_WindowMBak(object):
    def setupUi(self, WindowMBak):
        WindowMBak.setObjectName("WindowMBak")
        WindowMBak.resize(600, 400)
        WindowMBak.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBak)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 500, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btKBak = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btKBak.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btKBak.setObjectName("btKBak")
        self.verticalLayout.addWidget(self.btKBak)
        self.btSBak = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSBak.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSBak.setObjectName("btSBak")
        self.verticalLayout.addWidget(self.btSBak)
        self.btBak = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btBak.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btBak.setObjectName("btBak")
        self.verticalLayout.addWidget(self.btBak)
        
        self.btBMBOG = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btBMBOG.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btBMBOG.setObjectName("btBMBOG")
        self.verticalLayout.addWidget(self.btBMBOG)

        self.btMBYOG = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btMBYOG.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btMBYOG.setObjectName("btMBYOG")
        self.verticalLayout.addWidget(self.btMBYOG)
        
        self.btBMBHOCA = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btBMBHOCA.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btBMBHOCA.setObjectName("btBMBHOCA")
        self.verticalLayout.addWidget(self.btBMBHOCA)

        self.btBMBYH = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btBMBYH.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btBMBYH.setObjectName("btBMBYH")
        self.verticalLayout.addWidget(self.btBMBYH)

        WindowMBak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 23))
        self.menubar.setObjectName("menubar")
        WindowMBak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBak)
        self.statusbar.setObjectName("statusbar")
        WindowMBak.setStatusBar(self.statusbar)

        self.btKBak.clicked.connect(self.WMBK)
        self.btSBak.clicked.connect(self.WMBH)
        self.btBak.clicked.connect(self.WMBO)
    
        self.btBMBOG.clicked.connect(self.WBMBOG)
        self.btMBYOG.clicked.connect(self.WBMBYOG)
        self.btBMBHOCA.clicked.connect(self.WBMBHOCA)
        self.btBMBYH.clicked.connect(self.WBMBYH)
        
        self.retranslateUi(WindowMBak)
        QtCore.QMetaObject.connectSlotsByName(WindowMBak)
    def WMBO(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBO()
        self.ui.setupUi(self.window)
        self.window.show()
    def WMBK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBK()
        self.ui.setupUi(self.window)
        self.window.show()
    def WMBH(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBH()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def WBMBOG(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBOG()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def WBMBYOG(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBYOG()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def WBMBHOCA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBHOCA()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def WBMBYH(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowMBYH()
        self.ui.setupUi(self.window)
        self.window.show()
   
    def retranslateUi(self, WindowMBak):
        _translate = QtCore.QCoreApplication.translate
        WindowMBak.setWindowTitle(_translate("WindowMBak", "MainWindow"))
        self.btKBak.setText(_translate("WindowMBak", "Kitapçıklara Bak"))
        self.btSBak.setText(_translate("WindowMBak", "Sorulara Bak"))
        self.btBak.setText(_translate("WindowMBak", "Kitapcik Sorularına Bak"))
        
        self.btBMBOG.setText(_translate("WindowMBak", "Öğrencilere Bak"))
        self.btMBYOG.setText(_translate("WindowMBak", "Yerleştirilen Öğrenciler Bak"))
        self.btBMBHOCA.setText(_translate("WindowMBak", "Hocalara Bak"))
        self.btBMBYH.setText(_translate("WindowMBak", "Yerleştirilen Hocalara Bak"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBak = QtWidgets.QMainWindow()
    ui = Ui_WindowMBak()
    ui.setupUi(WindowMBak)
    WindowMBak.show()
    sys.exit(app.exec_())

