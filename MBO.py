# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MBO.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowMBO(object):
    def setupUi(self, WindowMBO):
        WindowMBO.setObjectName("WindowMBO")
        WindowMBO.resize(1119, 424)
        WindowMBO.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowMBO)
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
        WindowMBO.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowMBO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 23))
        self.menubar.setObjectName("menubar")
        WindowMBO.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowMBO)
        self.statusbar.setObjectName("statusbar")
        WindowMBO.setStatusBar(self.statusbar)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM sorular""")        
        for veri in im:

            self.listWidget.addItem(str("ID=")+str(veri[0])+str(" Soru=")+str(veri[1])+str(" A=")+str(veri[2])+str(" B=")+str(veri[3])+str(" C=")+str(veri[4])+str(" D=")+str(veri[5])+str(" E=")+str(veri[6])+str(" Doğru=")+str(veri[7])+str(" Soru Türü=")+str(veri[8])) 
        vt.close()
        self.retranslateUi(WindowMBO)
        QtCore.QMetaObject.connectSlotsByName(WindowMBO)

    def retranslateUi(self, WindowMBO):
        _translate = QtCore.QCoreApplication.translate
        WindowMBO.setWindowTitle(_translate("WindowMBO", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMBO = QtWidgets.QMainWindow()
    ui = Ui_WindowMBO()
    ui.setupUi(WindowMBO)
    WindowMBO.show()
    sys.exit(app.exec_())

