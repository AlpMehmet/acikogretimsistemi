# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YSoru.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowYSoru(object):
    def setupUi(self, WindowYSoru):
        WindowYSoru.setObjectName("WindowYSoru")
        WindowYSoru.resize(1201, 381)
        WindowYSoru.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYSoru)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 1181, 321))
        self.listWidget.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.listWidget.setObjectName("listWidget")
        WindowYSoru.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYSoru)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 23))
        self.menubar.setObjectName("menubar")
        WindowYSoru.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYSoru)
        self.statusbar.setObjectName("statusbar")
        WindowYSoru.setStatusBar(self.statusbar)

        self.retranslateUi(WindowYSoru)
        QtCore.QMetaObject.connectSlotsByName(WindowYSoru)

    def retranslateUi(self, WindowYSoru):
        _translate = QtCore.QCoreApplication.translate
        WindowYSoru.setWindowTitle(_translate("WindowYSoru", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYSoru = QtWidgets.QMainWindow()
    ui = Ui_WindowYSoru()
    ui.setupUi(WindowYSoru)
    WindowYSoru.show()
    sys.exit(app.exec_())

