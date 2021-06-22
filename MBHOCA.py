# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBHOCA(object):
    def setupUi(self, WindowMBHOCA):
        WindowMBHOCA.setObjectName("WindowMBHOCA")
        WindowMBHOCA.resize(1119, 424)
        WindowMBHOCA.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBHOCA)
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
        WindowMBHOCA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBHOCA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBHOCA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBHOCA)
        self.statusbar.setObjectName("statusbar")
        WindowMBHOCA.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM hoca""")        
        for veri in im:

            self.listWidget.addItem(str("ID=")+str(veri[0])+str(" İsim=")+str(veri[1])+str(" Soyad=")+str(veri[2])+str(" Mail=")+str(veri[3])+str(" Sehri=")+str(veri[4])+str(" Puan=")+str(veri[5])) 
        vt.close()
        self.retranslateUi(WindowMBHOCA)
        QtCore.QMetaObject.connectSlotsByName(WindowMBHOCA)

    def retranslateUi(self, WindowMBHOCA):
        _translate = QtCore.QCoreApplication.translate
        WindowMBHOCA.setWindowTitle(_translate("WindowMBHOCA", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBHOCA = QtWidgets.QMainWindow()
    ui = Ui_WindowMBHOCA()
    ui.setupUi(WindowMBHOCA)
    WindowMBHOCA.show()
    sys.exit(app.exec_())

