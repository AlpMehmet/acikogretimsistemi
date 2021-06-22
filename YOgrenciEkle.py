# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YOgrenciEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowYOEkle(object):
    seciliIlId=""
    seciliIlAd=""
    def setupUi(self, WindowYOEkle):
        WindowYOEkle.setObjectName("WindowYOEkle")
        WindowYOEkle.resize(367, 490)
        WindowYOEkle.setMinimumSize(QtCore.QSize(367, 447))
        WindowYOEkle.setMaximumSize(QtCore.QSize(367, 490))
        WindowYOEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYOEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 0, 321, 440))
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
        self.leAd = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leAd.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leAd.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leAd.setObjectName("leAd")
        self.verticalLayout_3.addWidget(self.leAd)
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
        self.leSoy = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leSoy.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leSoy.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leSoy.setObjectName("leSoy")
        self.verticalLayout_4.addWidget(self.leSoy)
        self.labelTc_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTc_2.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_2.setObjectName("labelTc_2")
        self.verticalLayout_4.addWidget(self.labelTc_2)
        self.leSifre = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leSifre.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leSifre.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leSifre.setObjectName("leSifre")
        self.verticalLayout_4.addWidget(self.leSifre)
        self.labelCep_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelCep_3.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_3.setObjectName("labelCep_3")
        self.verticalLayout_4.addWidget(self.labelCep_3)
        self.leNo = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leNo.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leNo.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leNo.setObjectName("leNo")
        self.verticalLayout_4.addWidget(self.leNo)
        self.labelTc_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelTc_3.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_3.setObjectName("labelTc_3")
        self.verticalLayout_4.addWidget(self.labelTc_3)
        self.cbSehir = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cbSehir.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.cbSehir.setObjectName("cbSehir")
        self.verticalLayout_4.addWidget(self.cbSehir)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.btSE = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btSE.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSE.setObjectName("btSE")
        self.verticalLayout_2.addWidget(self.btSE)
        WindowYOEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYOEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 23))
        self.menubar.setObjectName("menubar")
        WindowYOEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYOEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYOEkle.setStatusBar(self.statusbar)

       
        self.btSE.clicked.connect(self.se)
              
        self.cbSehir.activated[str].connect(self.il)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM il""") 
        for i in im:         
            self.cbSehir.addItem(str(i[1]))

        vt.close()  

        self.retranslateUi(WindowYOEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYOEkle)
    def se(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM il WHERE ilAd='"""+self.seciliIlAd+"""'""") 
        for i in im2:         
            self.seciliIlId=i[0]
    
        im.execute("""INSERT INTO  ogrenci (isim, soyisim, ogrenciNo, sehri, sifre) VALUES (?,?,?,?,?)""",(str(self.leAd.text()),str(self.leSoy.text()),str(self.leNo.text()),str(self.seciliIlId),str(self.leSifre.text())))   
        vt.commit()
        vt.close()       
#        for j in range(1,81):
#            vt = sqlite3.connect('VT.db')
#            im = vt.cursor()
#            im2 = vt.cursor()
#            im2.execute("""SELECT * FROM il WHERE ilAd='"""+self.seciliIlAd+"""'""") 
#            for i in im2:         
#                self.seciliIlId=i[0]
#        
#            im.execute("""INSERT INTO  ogrenci (isim, soyisim, ogrenciNo, sehri, sifre) VALUES (?,?,?,?,?)""",(str(self.leAd.text()+str(j)),str(self.leSoy.text()+str(j)),str(self.leNo.text()+str(j)),str(j),str(self.leSifre.text()+str(j))))   
#            vt.commit()
#            vt.close()
    def il(self, text):
        self.seciliIlAd = text
    def retranslateUi(self, WindowYOEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYOEkle.setWindowTitle(_translate("WindowYOEkle", "Öğrenci Ekle"))
        self.labelCep.setText(_translate("WindowYOEkle", "İsim:"))
        self.labelTc.setText(_translate("WindowYOEkle", "Soyisim:"))
        self.labelTc_2.setText(_translate("WindowYOEkle", "Şifre:"))
        self.labelCep_3.setText(_translate("WindowYOEkle", "Öğrenci No"))
        self.labelTc_3.setText(_translate("WindowYOEkle", "Şehri:"))
        self.btSE.setText(_translate("WindowYOEkle", "Öğrenci Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYOEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowYOEkle()
    ui.setupUi(WindowYOEkle)
    WindowYOEkle.show()
    sys.exit(app.exec_())

