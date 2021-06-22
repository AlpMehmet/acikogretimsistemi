# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBYOG(object):
    def setupUi(self, WindowMBYOG):
        WindowMBYOG.setObjectName("WindowMBYOG")
        WindowMBYOG.resize(1119, 424)
        WindowMBYOG.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBYOG)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 10, 1021, 341))
        self.listWidget.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.listWidget.setObjectName("listWidget")
        WindowMBYOG.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBYOG)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBYOG.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBYOG)
        self.statusbar.setObjectName("statusbar")
        WindowMBYOG.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenciDurum""")        
        for veri in im:

            self.listWidget.addItem(str("Salon No=")+str(veri[1])+str(" Sıra No=")+str(veri[2])+str(" Öğrenci ID=")+str(veri[3])) 
        vt.close()
        self.retranslateUi(WindowMBYOG)
        QtCore.QMetaObject.connectSlotsByName(WindowMBYOG)

    def retranslateUi(self, WindowMBYOG):
        _translate = QtCore.QCoreApplication.translate
        WindowMBYOG.setWindowTitle(_translate("WindowMBYOG", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBYOG = QtWidgets.QMainWindow()
    ui = Ui_WindowMBYOG()
    ui.setupUi(WindowMBYOG)
    WindowMBYOG.show()
    sys.exit(app.exec_())

