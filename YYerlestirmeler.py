# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YYerlestirmeler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowYYerlestirmeler(object):
    def setupUi(self, WindowYYerlestirmeler):
        WindowYYerlestirmeler.setObjectName("WindowYYerlestirmeler")
        WindowYYerlestirmeler.resize(680, 589)
        WindowYYerlestirmeler.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYYerlestirmeler)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 10, 651, 251))
        self.listWidget_2.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(20, 270, 651, 261))
        self.listWidget_3.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.listWidget_3.setObjectName("listWidget_3")
        WindowYYerlestirmeler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYYerlestirmeler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 23))
        self.menubar.setObjectName("menubar")
        WindowYYerlestirmeler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYYerlestirmeler)
        self.statusbar.setObjectName("statusbar")
        WindowYYerlestirmeler.setStatusBar(self.statusbar)

        self.retranslateUi(WindowYYerlestirmeler)
        QtCore.QMetaObject.connectSlotsByName(WindowYYerlestirmeler)

    def retranslateUi(self, WindowYYerlestirmeler):
        _translate = QtCore.QCoreApplication.translate
        WindowYYerlestirmeler.setWindowTitle(_translate("WindowYYerlestirmeler", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYYerlestirmeler = QtWidgets.QMainWindow()
    ui = Ui_WindowYYerlestirmeler()
    ui.setupUi(WindowYYerlestirmeler)
    WindowYYerlestirmeler.show()
    sys.exit(app.exec_())

