# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HBilgilerim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowHBilgilerim(object):
    def setupUi(self, WindowHBilgilerim):
        WindowHBilgilerim.setObjectName("WindowHBilgilerim")
        WindowHBilgilerim.resize(896, 348)
        WindowHBilgilerim.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowHBilgilerim)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 871, 301))
        self.listWidget.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.listWidget.setObjectName("listWidget")
        WindowHBilgilerim.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowHBilgilerim)
        self.statusbar.setObjectName("statusbar")
        WindowHBilgilerim.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM hoca""")        
        for veri in im:
            self.listWidget.addItem(str("ID=")+str(veri[0])+str(" Ad=")+str(veri[1])+str(" Soyad=")+str(veri[2])+str(" Mail=")+str(veri[3])+str(" Şifre=")+str(veri[4])+str(" Şehir=")+str(veri[5])+str(" Puan=")+str(veri[6])) 
        vt.close()
        self.retranslateUi(WindowHBilgilerim)
        QtCore.QMetaObject.connectSlotsByName(WindowHBilgilerim)

    def retranslateUi(self, WindowHBilgilerim):
        _translate = QtCore.QCoreApplication.translate
        WindowHBilgilerim.setWindowTitle(_translate("WindowHBilgilerim", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowHBilgilerim = QtWidgets.QMainWindow()
    ui = Ui_WindowHBilgilerim()
    ui.setupUi(WindowHBilgilerim)
    WindowHBilgilerim.show()
    sys.exit(app.exec_())

