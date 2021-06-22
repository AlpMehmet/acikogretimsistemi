from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
seciliDogru=""
seciliturId=""
seciliIlAd=""
class Ui_WindowYSoruEkle(object):
    def setupUi(self, WindowYSoruEkle):

        WindowYSoruEkle.setObjectName("WindowYSoruEkle")
        WindowYSoruEkle.resize(1263, 744)
        WindowYSoruEkle.setMinimumSize(QtCore.QSize(1263, 744))
        WindowYSoruEkle.setMaximumSize(QtCore.QSize(1263, 744))
        WindowYSoruEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYSoruEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1221, 610))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btSE_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSE_3.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btSE_3.setObjectName("btSE_3")
        self.verticalLayout.addWidget(self.btSE_3)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.labelTc_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelTc_7.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_7.setObjectName("labelTc_7")
        self.verticalLayout_22.addWidget(self.labelTc_7)
        self.cbD = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbD.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.cbD.setObjectName("cbD")
        self.verticalLayout_22.addWidget(self.cbD)
        self.verticalLayout.addLayout(self.verticalLayout_22)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.labelCep_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_15.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_15.setObjectName("labelCep_15")
        self.verticalLayout_21.addWidget(self.labelCep_15)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_21.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_21)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.labelCep_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_10.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_10.setObjectName("labelCep_10")
        self.verticalLayout_16.addWidget(self.labelCep_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_16.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.labelCep_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_14.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_14.setObjectName("labelCep_14")
        self.verticalLayout_20.addWidget(self.labelCep_14)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_20.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.labelCep_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_13.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_13.setObjectName("labelCep_13")
        self.verticalLayout_19.addWidget(self.labelCep_13)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_19.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.verticalLayout_19)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.labelCep_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_11.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_11.setObjectName("labelCep_11")
        self.verticalLayout_17.addWidget(self.labelCep_11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_17.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.verticalLayout_17)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.labelCep_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCep_9.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_9.setObjectName("labelCep_9")
        self.verticalLayout_14.addWidget(self.labelCep_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_14.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.verticalLayout_14)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 620, 1221, 76))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.labelTc_6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.labelTc_6.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_6.setObjectName("labelTc_6")
        self.verticalLayout_15.addWidget(self.labelTc_6)
        self.cbT = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbT.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.cbT.setObjectName("cbT")
        self.verticalLayout_15.addWidget(self.cbT)
        WindowYSoruEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYSoruEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1263, 23))
        self.menubar.setObjectName("menubar")
        WindowYSoruEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYSoruEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYSoruEkle.setStatusBar(self.statusbar)

        self.retranslateUi(WindowYSoruEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYSoruEkle)
        self.cbD.addItem(str("A"))
        self.cbD.addItem(str("B"))
        self.cbD.addItem(str("C"))
        self.cbD.addItem(str("D"))
        self.cbD.addItem(str("E"))   
        self.btSE_3.clicked.connect(self.yse)         
        self.cbT.activated[str].connect(self.tur)
        self.cbD.activated[str].connect(self.ders)   
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM soruTur""") 
        for i in im:         
            self.cbT.addItem(str(i[1]))

        vt.close()        
    def yse(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM soruTur WHERE turAd='"""+self.seciliIlAd+"""'""") 
        for i in im2:         
            self.seciliturId=i[0]
    
        im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",
                   (str(self.lineEdit.text()),str(self.lineEdit_2.text()),str(self.lineEdit_3.text()),str(self.lineEdit_4.text()),
                    str(self.lineEdit_5.text()),str(self.lineEdit_6.text()),str(self.seciliDogru),str(self.seciliturId)))   
        vt.commit()
        vt.close()      
#        vt2 = sqlite3.connect('VT.db')
#        im = vt2.cursor()
#        for j in range(1,5):
#            for i in range(1,9):
#                im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",(str(self.lineEdit.text())+str(j*i*2),str(self.lineEdit_2.text())+str(j*i*2),str(self.lineEdit_3.text())+str(j*i*2),str(self.lineEdit_4.text())+str(j*i*2),str(self.lineEdit_5.text())+str(j*i*2),str(self.lineEdit_6.text())+str(j*i*2),str("A"),str(i)))  
#                vt2.commit()
#            for i in range(1,9):
#                im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",(str(self.lineEdit.text())+str(j*i*2),str(self.lineEdit_2.text())+str(j*i*2),str(self.lineEdit_3.text())+str(j*i*2),str(self.lineEdit_4.text())+str(j*i*2),str(self.lineEdit_5.text())+str(j*i*2),str(self.lineEdit_6.text())+str(j*i*2),str("B"),str(i)))  
#                vt2.commit()
#            for i in range(1,9):
#                im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",(str(self.lineEdit.text())+str(j*i*2),str(self.lineEdit_2.text())+str(j*i*2),str(self.lineEdit_3.text())+str(j*i*2),str(self.lineEdit_4.text())+str(j*i*2),str(self.lineEdit_5.text())+str(j*i*2),str(self.lineEdit_6.text())+str(j*i*2),str("C"),str(i)))  
#                vt2.commit()
#            for i in range(1,9):
#                im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",(str(self.lineEdit.text())+str(j*i*2),str(self.lineEdit_2.text())+str(j*i*2),str(self.lineEdit_3.text())+str(j*i*2),str(self.lineEdit_4.text())+str(j*i*2),str(self.lineEdit_5.text())+str(j*i*2),str(self.lineEdit_6.text())+str(j*i*2),str("D"),str(i)))  
#                vt2.commit()
#            for i in range(1,9):
#                im.execute("""INSERT INTO  sorular (soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru, soruturId) VALUES (?,?,?,?,?,?,?,?)""",(str(self.lineEdit.text())+str(j*i*2),str(self.lineEdit_2.text())+str(j*i*2),str(self.lineEdit_3.text())+str(j*i*2),str(self.lineEdit_4.text())+str(j*i*2),str(self.lineEdit_5.text())+str(j*i*2),str(self.lineEdit_6.text())+str(j*i*2),str("E"),str(i)))  
#                vt2.commit()
#        vt2.close()  
    def ders(self, text):
        self.seciliDogru = text
    def tur(self, text):
        self.seciliIlAd = text

    def retranslateUi(self, WindowYSoruEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYSoruEkle.setWindowTitle(_translate("WindowYSoruEkle", "Soru Ekle"))
        self.btSE_3.setText(_translate("WindowYSoruEkle", "Soru Ekle"))
        self.labelTc_7.setText(_translate("WindowYSoruEkle", "Doğru Cevap Hangisi Seçiniz"))
        self.labelCep_15.setText(_translate("WindowYSoruEkle", "Soru"))
        self.labelCep_10.setText(_translate("WindowYSoruEkle", "A"))
        self.labelCep_14.setText(_translate("WindowYSoruEkle", "B"))
        self.labelCep_13.setText(_translate("WindowYSoruEkle", "C"))
        self.labelCep_11.setText(_translate("WindowYSoruEkle", "D"))
        self.labelCep_9.setText(_translate("WindowYSoruEkle", "E"))
        self.labelTc_6.setText(_translate("WindowYSoruEkle", "Tür Seçiniz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYSoruEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowYSoruEkle()
    ui.setupUi(WindowYSoruEkle)
    WindowYSoruEkle.show()
    sys.exit(app.exec_())

