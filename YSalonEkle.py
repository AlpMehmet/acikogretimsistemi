# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YSalonEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowYSalonEkle(object):
    seciliIlId=""
    seciliIlAd=""
    def setupUi(self, WindowYSalonEkle):
        WindowYSalonEkle.setObjectName("WindowYSalonEkle")
        WindowYSalonEkle.resize(373, 470)
        WindowYSalonEkle.setMinimumSize(QtCore.QSize(373, 470))
        WindowYSalonEkle.setMaximumSize(QtCore.QSize(373, 470))
        WindowYSalonEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYSalonEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 321, 363))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCep = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelCep.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep.setObjectName("labelCep")
        self.verticalLayout_3.addWidget(self.labelCep)
        self.lineEditKisiSay = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditKisiSay.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEditKisiSay.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEditKisiSay.setObjectName("lineEditKisiSay")
        self.verticalLayout_3.addWidget(self.lineEditKisiSay)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelTc = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTc.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc.setObjectName("labelTc")
        self.verticalLayout_4.addWidget(self.labelTc)
        self.comboBoxIl = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBoxIl.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.comboBoxIl.setObjectName("comboBoxIl")
        self.verticalLayout_4.addWidget(self.comboBoxIl)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.pushButtonEkle = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonEkle.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.pushButtonEkle.setObjectName("pushButtonEkle")
        self.verticalLayout_2.addWidget(self.pushButtonEkle)
        WindowYSalonEkle.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowYSalonEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYSalonEkle.setStatusBar(self.statusbar)
        
        self.pushButtonEkle.clicked.connect(self.se)
              
        self.comboBoxIl.activated[str].connect(self.il)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM il""") 
        for i in im:         
            self.comboBoxIl.addItem(str(i[1]))

        vt.close()  
        self.retranslateUi(WindowYSalonEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYSalonEkle)
    def se(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM il WHERE ilAd='"""+self.seciliIlAd+"""'""") 
        for i in im2:         
            self.seciliIlId=i[0]
    
        im.execute("""INSERT INTO  salon (ilId, kisiSay) VALUES (?,?)""",(str(self.seciliIlId),str(self.lineEditKisiSay.text())))   
        vt.commit()
        vt.close()       

    def il(self, text):
        self.seciliIlAd = text

    def retranslateUi(self, WindowYSalonEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYSalonEkle.setWindowTitle(_translate("WindowYSalonEkle", "MainWindow"))
        self.labelCep.setText(_translate("WindowYSalonEkle", "Kişi Sayısı Giriniz"))
        self.labelTc.setText(_translate("WindowYSalonEkle", "İl Seçiniz"))
        self.pushButtonEkle.setText(_translate("WindowYSalonEkle", "Salon Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYSalonEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowYSalonEkle()
    ui.setupUi(WindowYSalonEkle)
    WindowYSalonEkle.show()
    sys.exit(app.exec_())

