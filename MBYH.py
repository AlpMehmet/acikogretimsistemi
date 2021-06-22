# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBYH(object):
    def setupUi(self, WindowMBYH):
        WindowMBYH.setObjectName("WindowMBYH")
        WindowMBYH.resize(1119, 424)
        WindowMBYH.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBYH)
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
        WindowMBYH.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBYH)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBYH.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBYH)
        self.statusbar.setObjectName("statusbar")
        WindowMBYH.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM hocaDurum""")        
        for veri in im:

            self.listWidget.addItem(str("Sınav İstek ID=")+str(veri[1])+str(" Red Durumu=")+str(veri[2])+str(" Hoca ID=")+str(veri[3])+str(" Hoca Puan=")+str(veri[4])) 
        vt.close()
        self.retranslateUi(WindowMBYH)
        QtCore.QMetaObject.connectSlotsByName(WindowMBYH)

    def retranslateUi(self, WindowMBYH):
        _translate = QtCore.QCoreApplication.translate
        WindowMBYH.setWindowTitle(_translate("WindowMBYH", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBYH = QtWidgets.QMainWindow()
    ui = Ui_WindowMBYH()
    ui.setupUi(WindowMBYH)
    WindowMBYH.show()
    sys.exit(app.exec_())

