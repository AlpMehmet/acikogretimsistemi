# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import random
class Ui_WindowYonMenu(object):
    dogruiceriktut=""
    cevap=""
    def setupUi(self, WindowYonMenu):
        WindowYonMenu.setObjectName("WindowYonMenu")
        WindowYonMenu.resize(496, 427)
        WindowYonMenu.setStyleSheet("  background-color: rgb(233, 239, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(WindowYonMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btOgrenciYerlestir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btOgrenciYerlestir.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btOgrenciYerlestir.setObjectName("btOgrenciYerlestir")
        self.verticalLayout.addWidget(self.btOgrenciYerlestir)
        self.btHocaYerlestir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btHocaYerlestir.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btHocaYerlestir.setObjectName("btHocaYerlestir")
        self.verticalLayout.addWidget(self.btHocaYerlestir)
        
        
        self.btKO = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btKO.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btKO.setObjectName("btKO")
        self.verticalLayout.addWidget(self.btKO)        
        

        self.btMail3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btMail3.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btMail3.setObjectName("btMail3")
        self.verticalLayout.addWidget(self.btMail3)
        self.btMail1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btMail1.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btMail1.setObjectName("btMail1")
        self.verticalLayout.addWidget(self.btMail1)
        self.btMail2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btMail2.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btMail2.setObjectName("btMail2")
        self.verticalLayout.addWidget(self.btMail2)
        self.btBaslat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btBaslat.setStyleSheet("    background-color: rgb(51, 191, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 12px;\n"
"    border-color: rgb(0, 145, 255);\n"
"    font: bold 12px;\n"
"    min-width: 10em;\n"
"    padding: 8px;")
        self.btBaslat.setObjectName("btBaslat")
        self.verticalLayout.addWidget(self.btBaslat)
        WindowYonMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowYonMenu)
        self.statusbar.setObjectName("statusbar")
        WindowYonMenu.setStatusBar(self.statusbar)
        self.btKO.clicked.connect(self.KO)
#        self.btBaslat.clicked.connect(self.WHE)
        self.btHocaYerlestir.clicked.connect(self.HY)
        self.btMail1.clicked.connect(self.mailyol1)
        self.btMail2.clicked.connect(self.mailyol2)
        self.btMail3.clicked.connect(self.mailyol3)
        self.btOgrenciYerlestir.clicked.connect(self.OY)
        self.retranslateUi(WindowYonMenu)
        QtCore.QMetaObject.connectSlotsByName(WindowYonMenu)

    def HY(self):
        sinavTI=[]
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM sinavTarihleri""") 
        for i in im:
            sinavTI.append(str(i[0]))
        yok=0 
        for j in sinavTI:
            im2 = vt.cursor()
            im2.execute("""SELECT * FROM hocaDurum WHERE sinavIstek='"""+str(j)+"""' ORDER BY hocaPuan DESC """)
            for a in im2:
                im3 = vt.cursor()
                im3.execute("""SELECT * FROM salonDurum """)
                for b in im3:
                    if(str(b[1])==str(a[3]) or str(b[2])==str(j)):
                        yok=yok+1
            
                if(yok==0 and a[2]!=1):
                    im4 = vt.cursor()
                    im4.execute("""INSERT INTO  salonDurum (ogretmenId, sinavtarihleriId) VALUES ('"""+str(a[3])+"""', '"""+str(a[1])+"""')""")  
                    vt.commit()
        vt.close()
    def OY(self):
        saloneklendi=[]
        salonvar=0
        vt = sqlite3.connect('VT.db')
        for i in range(1,81):     
            im = vt.cursor()
            im.execute("""SELECT * FROM salon WHERE ilId='"""+str(i)+"""'""")   
            for j in im:
                say=0
                for var in range(0,len(saloneklendi)):
                    if(str(saloneklendi[var])==str(j[0])):
                        salonvar=1
                if(salonvar!=1):
                    kisiSay=str(j[2])
                    print(kisiSay)
                    im11 = vt.cursor()
                    im11.execute("""SELECT * FROM ogrenci WHERE sehri='"""+str(i) +"""'""")
                    for ogrenci in im11:
                        if(ogrenci[0]==None):
                            continue
                        else:
                            if(int(say)<int(kisiSay)):
                                say=say+1
                                im12 = vt.cursor()
                                im12.execute("""INSERT INTO ogrenciDurum (salonNo, siraNo, ogId) VALUES ('"""+str(j[0])+"""', '"""+str(say)+"""', '"""+str(ogrenci[0])+"""')""")
                                vt.commit()
                saloneklendi.append(j[0])
        vt.close()
    def KO(self):
        dizicevapkar=[]
        vt = sqlite3.connect('VT.db')
        im = vt.cursor()
        sorusayisi=0
        sorutursayisi=8
        im.execute("""SELECT * FROM sorular""")
        dogruindis=0
        for i in im:
            sorusayisi=sorusayisi+1
        kitapciksayisi=sorusayisi/sorutursayisi
        for kitapcik in range(0,int(kitapciksayisi)):
            for tur in range(1,9):
                im2 = vt.cursor()
                im2.execute("""SELECT * FROM sorular WHERE soruturId='"""+str(tur)+"""'""")
                sekizsorutut=0
                for soruekle in im2:
                    sekizsorutut=sekizsorutut+1
                    if(sekizsorutut<4):
                        if(str(soruekle[7])=="A"):
                            self.dogruiceriktut=soruekle[2]
                        if(str(soruekle[7])=="B"):
                            self.dogruiceriktut=soruekle[3]
                        if(str(soruekle[7])=="C"):
                            self.dogruiceriktut=soruekle[4]
                        if(str(soruekle[7])=="D"):
                            self.dogruiceriktut=soruekle[5]
                        if(str(soruekle[7])=="E"):
                            self.dogruiceriktut=soruekle[6]
                        dizicevapkar.append(soruekle[2])
                        dizicevapkar.append(soruekle[3])
                        dizicevapkar.append(soruekle[4])
                        dizicevapkar.append(soruekle[5])
                        dizicevapkar.append(soruekle[6])
                        random.shuffle(dizicevapkar)
                        random.shuffle(dizicevapkar)
                        random.shuffle(dizicevapkar)
                        for dizibas in range(0,len(dizicevapkar)):
                            print(str(dizicevapkar[dizibas]))
                        for i in range(0,5):
                            if(dizicevapkar[i]==self.dogruiceriktut):
                                dogruindis=i+1
                        if(dogruindis==1):
                            self.cevap="A"
                        if(dogruindis==2):
                            self.cevap="B"
                        if(dogruindis==3):
                            self.cevap="C"
                        if(dogruindis==4):
                            self.cevap="D"
                        if(dogruindis==5):
                            self.cevap="E"
                        imsoruekle = vt.cursor()
                        imsoruekle.execute("""INSERT INTO  kitapcikSoru (kitapcikNo, soru, cvp1, cvp2, cvp3, cvp4, cvp5, dogru) VALUES 
                                           ('"""+str(kitapcik)+"""','"""+str(soruekle[1])+"""', '"""+str(dizicevapkar[0])+"""','"""+str(dizicevapkar[1])+"""','"""+str(dizicevapkar[2])+"""','"""+str(dizicevapkar[3])+"""','"""+str(dizicevapkar[4])+"""','"""+str(self.cevap)+"""')""")  
                        vt.commit()
                        dogruindis=0
                        dizicevapkar.clear()     
            kitapcikekle = vt.cursor()
            kitapcikekle.execute("""INSERT INTO  kitapcik (kitapcikNo) VALUES ('"""+str(kitapcik)+"""')""")  
            vt.commit()
        vt.close()
    def mailyol1(self):
        
        subject = 'subject'
        vt1 = sqlite3.connect('VT.db')
        im4=vt1.cursor()
        im4.execute("""DELETE FROM yoneticiDurum""")
        vt1.commit()
        vt1.close()
        vt2 = sqlite3.connect('VT.db')
        im2 = vt2.cursor()
        im2.execute("""INSERT INTO yoneticiDurum (ilkMail, ikinciMail, ucuncuMail) VALUES (1,0,0)""")   
        im = vt2.cursor()
        im.execute("""SELECT * FROM hoca""")   
        for veri in im:
            msg = MIMEMultipart()
            msg['From'] = 'alpmehmetozturk@gmail.com'
            msg['Subject'] = subject
            msg['To'] = veri[3]
            body = 'İstek tarih ve saat seçiniz'
            msg.attach(MIMEText(body,'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('alpmehmetozturk@gmail.com','01A06m0550alp.')          
            server.sendmail('alpmehmetozturk@gmail.com',veri[3],text)                       
        server.quit()
        vt2.commit()
        vt2.close()
    def mailyol2(self):
        subject = 'subject'
        vt1 = sqlite3.connect('VT.db')
        im4=vt1.cursor()
        im4.execute("""DELETE FROM yoneticiDurum""")
        vt1.commit()
        vt1.close()
        vt2 = sqlite3.connect('VT.db')
        im2 = vt2.cursor()
        im2.execute("""INSERT INTO yoneticiDurum (ilkMail, ikinciMail, ucuncuMail) VALUES (0,1,0)""")   
        im = vt2.cursor()
        im.execute("""SELECT * FROM hoca""")   
        for veri in im:
            msg = MIMEMultipart()
            msg['From'] = 'alpmehmetozturk@gmail.com'
            msg['Subject'] = subject
            msg['To'] = veri[3]
            body = 'Kabul Veya Red Ediniz'
            msg.attach(MIMEText(body,'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('alpmehmetozturk@gmail.com','01A06m0550alp.')          
            server.sendmail('alpmehmetozturk@gmail.com',veri[3],text)                       
        server.quit()
        vt2.commit()
        vt2.close()       
    def mailyol3(self):
        subject = 'subject'
        vt1 = sqlite3.connect('VT.db')
        im4=vt1.cursor()
        im4.execute("""DELETE FROM yoneticiDurum""")
        vt1.commit()
        vt1.close()
        vt2 = sqlite3.connect('VT.db')
        im2 = vt2.cursor()
        im2.execute("""INSERT INTO yoneticiDurum (ilkMail, ikinciMail, ucuncuMail) VALUES (0,1,0)""")   
        im = vt2.cursor()
        im.execute("""SELECT * FROM hoca""")   
        for veri in im:
            msg = MIMEMultipart()
            msg['From'] = 'alpmehmetozturk@gmail.com'
            msg['Subject'] = subject
            msg['To'] = veri[3]
            body = 'Kabul Etme Veya Red Etme Süreniz Bitmiştir'
            msg.attach(MIMEText(body,'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login('alpmehmetozturk@gmail.com','01A06m0550alp.')          
            server.sendmail('alpmehmetozturk@gmail.com',veri[3],text)                       
        server.quit()
        vt2.commit()
        vt2.close()
        self.HY()   
    def retranslateUi(self, WindowYonMenu):
        _translate = QtCore.QCoreApplication.translate
        WindowYonMenu.setWindowTitle(_translate("WindowYonMenu", "Menü"))
        self.btOgrenciYerlestir.setText(_translate("WindowYonMenu", "Öğrencileri Yerleştir"))
        self.btKO.setText(_translate("WindowYonMenu", "Kitapcık Oluştur"))
        self.btHocaYerlestir.setText(_translate("WindowYonMenu", "Hocaları Yerleştir"))
        self.btMail3.setText(_translate("WindowYonMenu", "Kabul Veya Red Etme Sürelerini Bitirip Red Edilenler Yerine Oto Yerleştir"))
        self.btMail1.setText(_translate("WindowYonMenu", "Hocalara Sisteme Girip Tarih Seçmeleri İçin Mail Yolla"))
        self.btMail2.setText(_translate("WindowYonMenu", "Hocalara Sisteme Girip Kabul Veya Red Etmeleri İçin Mail Yolla"))
        self.btBaslat.setText(_translate("WindowYonMenu", "Başlat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowYonMenu = QtWidgets.QMainWindow()
    ui = Ui_WindowYonMenu()
    ui.setupUi(WindowYonMenu)
    WindowYonMenu.show()
    sys.exit(app.exec_())

