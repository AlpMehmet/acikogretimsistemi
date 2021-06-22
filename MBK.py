# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBK.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBK(object):
    def setupUi(self, WindowMBK):
        WindowMBK.setObjectName("WindowMBK")
        WindowMBK.resize(1119, 424)
        WindowMBK.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBK)
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
        WindowMBK.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBK)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBK.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBK)
        self.statusbar.setObjectName("statusbar")
        WindowMBK.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM kitapcik""")        
        for veri in im:

            self.listWidget.addItem(str("ID=")+str(veri[0])+str(" Kitapcık No=")+str(veri[1])) 
        vt.close()
        


        self.retranslateUi(WindowMBK)
        QtCore.QMetaObject.connectSlotsByName(WindowMBK)

    def retranslateUi(self, WindowMBK):
        _translate = QtCore.QCoreApplication.translate
        WindowMBK.setWindowTitle(_translate("WindowMBK", "Kitapcıklar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBK = QtWidgets.QMainWindow()
    ui = Ui_WindowMBK()
    ui.setupUi(WindowMBK)
    WindowMBK.show()
    sys.exit(app.exec_())

