import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowYHocaEkle(object):
    seciliIlId=""
    seciliIlAd=""
    def setupUi(self, WindowYHocaEkle):
        WindowYHocaEkle.setObjectName("WindowYHocaEkle")
        WindowYHocaEkle.resize(467, 854)
        WindowYHocaEkle.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYHocaEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 451, 791))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelCep_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
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
        self.verticalLayout_5.addWidget(self.labelCep_2)
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
        self.verticalLayout_5.addWidget(self.leSoy)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
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
        self.verticalLayout_6.addWidget(self.labelCep_3)
        self.leMail = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.leMail.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.leMail.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.leMail.setObjectName("leMail")
        self.verticalLayout_6.addWidget(self.leMail)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelCep_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelCep_4.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelCep_4.setObjectName("labelCep_4")
        self.verticalLayout_7.addWidget(self.labelCep_4)
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
        self.verticalLayout_7.addWidget(self.leSifre)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        WindowYHocaEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowYHocaEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 23))
        self.menubar.setObjectName("menubar")
        WindowYHocaEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowYHocaEkle)
        self.statusbar.setObjectName("statusbar")
        WindowYHocaEkle.setStatusBar(self.statusbar)
        
        self.pushButtonEkle.clicked.connect(self.se)
              
        self.comboBoxIl.activated[str].connect(self.il)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM il""") 
        for i in im:         
            self.comboBoxIl.addItem(str(i[1]))

        vt.close()  
        
        self.retranslateUi(WindowYHocaEkle)
        QtCore.QMetaObject.connectSlotsByName(WindowYHocaEkle)
    def se(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM il WHERE ilAd='"""+self.seciliIlAd+"""'""") 
        for i in im2:         
            self.seciliIlId=i[0]
    
        im.execute("""INSERT INTO  hoca (ad, soyad, mail, sifre, ilId) VALUES (?,?,?,?,?)""",(str(self.leAd.text()),str(self.leSoy.text()),str(self.leMail.text()),str(self.leSifre.text()),str(self.seciliIlId)))   
        vt.commit()
        vt.close()       

    def il(self, text):
        self.seciliIlAd = text
        
    def retranslateUi(self, WindowYHocaEkle):
        _translate = QtCore.QCoreApplication.translate
        WindowYHocaEkle.setWindowTitle(_translate("WindowYHocaEkle", "MainWindow"))
        self.pushButtonEkle.setText(_translate("WindowYHocaEkle", "Hoca Ekle"))
        self.labelCep_2.setText(_translate("WindowYHocaEkle", "Soyad"))
        self.labelCep_3.setText(_translate("WindowYHocaEkle", "Mail"))
        self.labelTc.setText(_translate("WindowYHocaEkle", "İl Seçiniz"))
        self.labelCep.setText(_translate("WindowYHocaEkle", "Ad"))
        self.labelCep_4.setText(_translate("WindowYHocaEkle", "Şifre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYHocaEkle = QtWidgets.QMainWindow()
    ui = Ui_WindowYHocaEkle()
    ui.setupUi(WindowYHocaEkle)
    WindowYHocaEkle.show()
    sys.exit(app.exec_())

