from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_WindowHTarihSec(object):
    secilitarihID=0
    secilitarihAd=""
    secilisaatAd=""
    def setupUi(self, WindowHTarihSec):
        WindowHTarihSec.setObjectName("WindowHTarihSec")
        WindowHTarihSec.resize(361, 252)
        WindowHTarihSec.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowHTarihSec)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 321, 198))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelTc_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelTc_4.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_4.setObjectName("labelTc_4")
        self.verticalLayout_7.addWidget(self.labelTc_4)
        self.cbSehir_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.cbSehir_2.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.cbSehir_2.setObjectName("cbSehir_2")
        self.verticalLayout_7.addWidget(self.cbSehir_2)
        self.labelTc_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelTc_5.setStyleSheet("     background-color: rgb(49, 38, 170);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    font-color:rgb(160, 246, 255);\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.labelTc_5.setObjectName("labelTc_5")
        self.verticalLayout_7.addWidget(self.labelTc_5)
        self.cbSehir_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.cbSehir_3.setStyleSheet("    background-color: rgb(196, 225, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"    padding: 6px;\n"
"    border-color: rgb(0, 145, 255)")
        self.cbSehir_3.setObjectName("cbSehir_3")
        self.verticalLayout_7.addWidget(self.cbSehir_3)
        self.btOnay = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btOnay.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btOnay.setObjectName("btOnay")
        self.verticalLayout_7.addWidget(self.btOnay)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        WindowHTarihSec.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowHTarihSec)
        self.statusbar.setObjectName("statusbar")
        WindowHTarihSec.setStatusBar(self.statusbar)
        
        self.btOnay.clicked.connect(self.ta)
    
        self.cbSehir_2.activated[str].connect(self.tarih)
        self.cbSehir_3.activated[str].connect(self.saat)
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM sinavTarihleri""") 
        for i in im:         
            self.cbSehir_2.addItem(str(i[2]))
            self.cbSehir_3.addItem(str(i[3]))
        vt.close()  
        
        self.retranslateUi(WindowHTarihSec)
        QtCore.QMetaObject.connectSlotsByName(WindowHTarihSec)
    def ta(self):

        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im2 = vt.cursor()
        im3 = vt.cursor()
        im3.execute("""SELECT * FROM hoca WHERE id='"""+self.girisyapan+"""'""") 
        for j in im3:
            im2.execute("""SELECT * FROM sinavTarihleri WHERE tarih='"""+self.secilitarihAd+"""' and saat='"""+self.secilisaatAd+"""'""") 
            for i in im2:         
                self.secilitarihID=i[0]    
            im.execute("""INSERT INTO  hocaDurum (sinavIstek, hocaId, hocaPuan) VALUES (?,?,?)""",(str(self.secilitarihID),str(self.girisyapan),str(j[6])))   
            im4 = vt.cursor()
            im4.execute("""UPDATE hoca SET puan=puan+'"""+str(1)+"""' WHERE id='"""+self.girisyapan+"""'""")       
            vt.commit()
        vt.close()     
    def tarih(self, text):
        self.secilitarihAd = text
    def saat(self, text):
        self.secilisaatAd = text
    def retranslateUi(self, WindowHTarihSec):
        _translate = QtCore.QCoreApplication.translate
        WindowHTarihSec.setWindowTitle(_translate("WindowHTarihSec", "MainWindow"))
        self.labelTc_4.setText(_translate("WindowHTarihSec", "Tarih"))
        self.labelTc_5.setText(_translate("WindowHTarihSec", "Saat"))
        self.btOnay.setText(_translate("WindowHTarihSec", "Onayla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowHTarihSec = QtWidgets.QMainWindow()
    ui = Ui_WindowHTarihSec()
    ui.setupUi(WindowHTarihSec)
    WindowHTarihSec.show()
    sys.exit(app.exec_())

