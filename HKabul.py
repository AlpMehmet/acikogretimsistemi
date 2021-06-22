# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HKabul.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowHKabul(object):
    def setupUi(self, WindowHKabul):
        WindowHKabul.setObjectName("WindowHKabul")
        WindowHKabul.resize(472, 211)
        WindowHKabul.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowHKabul)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCep_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelCep_2.setGeometry(QtCore.QRect(10, 19, 451, 115))
        self.labelCep_2.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_2.setObjectName("labelCep_2")
        self.comboBoxIl_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxIl_2.setGeometry(QtCore.QRect(10, 140, 451, 35))
        self.comboBoxIl_2.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.comboBoxIl_2.setObjectName("comboBoxIl_2")
        self.comboBoxIl_2.addItem("")
        self.comboBoxIl_2.addItem("")
        WindowHKabul.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowHKabul)
        self.statusbar.setObjectName("statusbar")
        WindowHKabul.setStatusBar(self.statusbar)
    
        self.comboBoxIl_2.activated[str].connect(self.durum)


        self.retranslateUi(WindowHKabul)
        QtCore.QMetaObject.connectSlotsByName(WindowHKabul)

    def durum(self, text):
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        if(str(text)=="Kabul"):
            im.execute("""INSERT INTO  hocaDurum (red) VALUES (?)""",(str(0)))   
        else:
            im.execute("""INSERT INTO  hocaDurum (red) VALUES (?)""",(str(1)))   
    def retranslateUi(self, WindowHKabul):
        _translate = QtCore.QCoreApplication.translate
        WindowHKabul.setWindowTitle(_translate("WindowHKabul", "MainWindow"))
        self.labelCep_2.setText(_translate("WindowHKabul", "Tercih ettiğiniz saat ve tarihteki görevi kabul ediyor musunuz?"))
        self.comboBoxIl_2.setItemText(0, _translate("WindowHKabul", "Kabul"))
        self.comboBoxIl_2.setItemText(1, _translate("WindowHKabul", "Red"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowHKabul = QtWidgets.QMainWindow()
    ui = Ui_WindowHKabul()
    ui.setupUi(WindowHKabul)
    WindowHKabul.show()
    sys.exit(app.exec_())

