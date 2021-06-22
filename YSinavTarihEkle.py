# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YSinavTarihEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowYSinavTarihEkle(object):
    seciliSalonId=""
    def setupUi(self, WindowYSinavTarihEkle):
        WindowYSinavTarihEkle.setObjectName("WindowYSinavTarihEkle")
        WindowYSinavTarihEkle.resize(348, 360)
        WindowYSinavTarihEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYSinavTarihEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 301))
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
        self.leTarih = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leTarih.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leTarih.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leTarih.setObjectName("leTarih")
        self.verticalLayout_3.addWidget(self.leTarih)
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
        self.leSaat = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leSaat.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leSaat.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leSaat.setObjectName("leSaat")
        self.verticalLayout_4.addWidget(self.leSaat)
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
        self.btTE = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btTE.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btTE.setObjectName("btTE")
        self.verticalLayout_4.addWidget(self.btTE)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        WindowYSinavTarihEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYSinavTarihEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 23))
        self.menubar.setObjectName("menubar")
        WindowYSinavTarihEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYSinavTarihEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYSinavTarihEkle.setStatusBar(self.statusbar)
        
        self.btTE.clicked.connect(self.ste)
              
        self.cbSehir.activated[str].connect(self.salon)

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM salon""") 
        for i in im:         
            self.cbSehir.addItem(str(i[1]))

        vt.close()  
        self.retranslateUi(WindowYSinavTarihEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYSinavTarihEkle)
    def salon(self, text):
        self.seciliSalonId= text
    
    def ste(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""INSERT INTO  sinavTarihleri (salonid, tarih, saat) VALUES (?,?,?)""",(str(self.seciliSalonId),str(self.leTarih.text()),str(self.leTarih.text())))   
        vt.commit()
        vt.close()    
    def retranslateUi(self, WindowYSinavTarihEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYSinavTarihEkle.setWindowTitle(_translate("WindowYSinavTarihEkle", "MainWindow"))
        self.labelCep.setText(_translate("WindowYSinavTarihEkle", "Tarih:"))
        self.labelTc.setText(_translate("WindowYSinavTarihEkle", "Saat:"))
        self.labelTc_3.setText(_translate("WindowYSinavTarihEkle", "salon:"))
        self.btTE.setText(_translate("WindowYSinavTarihEkle", "Sınav Tarihi Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYSinavTarihEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowYSinavTarihEkle()
    ui.setupUi(WindowYSinavTarihEkle)
    WindowYSinavTarihEkle.show()
    sys.exit(app.exec_())

