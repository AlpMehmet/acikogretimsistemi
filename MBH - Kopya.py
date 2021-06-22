# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBH.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBH(object):
    def setupUi(self, WindowMBH):
        WindowMBH.setObjectName("WindowMBH")
        WindowMBH.resize(1119, 424)
        WindowMBH.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBH)
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
        WindowMBH.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBH)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBH.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBH)
        self.statusbar.setObjectName("statusbar")
        WindowMBH.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM kitapcikSoru""")        
        for veri in im:

            self.listWidget.addItem(str("ID=")+str(veri[0])+str(" Kitapcik No=")+str(veri[1])+str(" Soru=")+str(veri[2])+str(" A=")+str(veri[3])+str(" B=")+str(veri[4])+str(" C=")+str(veri[5])+str(" D=")+str(veri[6])+str(" E=")+str(veri[7])+str(" Doğru=")+str(veri[8])) 
        vt.close()
        self.retranslateUi(WindowMBH)
        QtCore.QMetaObject.connectSlotsByName(WindowMBH)

    def retranslateUi(self, WindowMBH):
        _translate = QtCore.QCoreApplication.translate
        WindowMBH.setWindowTitle(_translate("WindowMBH", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBH = QtWidgets.QMainWindow()
    ui = Ui_WindowMBH()
    ui.setupUi(WindowMBH)
    WindowMBH.show()
    sys.exit(app.exec_())

