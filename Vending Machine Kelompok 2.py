import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from TerimaKasih import Ui_Dialog
import cv2
# Program Vending Machine Tugas Besar Pengenalan Komputasi 2023
# Algorithm & UI made by Adhimas Aryo Bimo (19623142) (@ryonlunar)

# kamus barang
a = {'nama' : 'Hydrococo', 'harga' : "Rp7000", 'stok' : 2}
b = {'nama' : 'Indomilk', 'harga' : "Rp5000", 'stok' : 4}
c = {'nama' : 'Pocky', 'harga' : "Rp6000", 'stok' : 6}
d = {'nama' : 'Nabati', 'harga' : "Rp3000", 'stok' : 7}
e = {'nama' : 'Teh Pucuk', 'harga' : "Rp5000", 'stok' : 10}
f = {'nama' : 'Nutriboost', 'harga' : "Rp8000", 'stok' : 2}

item = [a,b,c,d,e,f]

### ADS WINDOW ###
class AdsWindow(QDialog):
    def __init__(self):
        super(AdsWindow, self).__init__()
        loadUi("ads2.ui", self)
        self.sentuhLayar.clicked.connect(self.gotomenu)

    def gotomenu(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

### MAIN WINDOW ###
class MainWindow(QDialog):
    def __init__ (self):
        super(MainWindow, self).__init__()
        loadUi("altMain1.ui", self)
        
        # nama produk
        self.label_1.setText(item[0]["nama"])
        self.label_2.setText(item[1]["nama"])
        self.label_3.setText(item[2]["nama"])
        self.label_4.setText(item[3]["nama"])

        # harga produk
        self.harga_1.setText(item[0]["harga"])
        self.harga_2.setText(item[1]["harga"])
        self.harga_3.setText(item[2]["harga"])
        self.harga_4.setText(item[3]["harga"])

        # kuantitas produk
        self.quantity_1.setText(str(item[0]["stok"]))
        self.quantity_2.setText(str(item[1]["stok"]))
        self.quantity_3.setText(str(item[2]["stok"]))
        self.quantity_4.setText(str(item[3]["stok"]))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.gotoadsWindow)
        self.timer.start(30000) ## dalam 30 detik akan kembali ke adsWindow

        # button
        def disabledButton(self): ## tombol akan dinonaktifkan apabila stok 0
            if item[0]["stok"] == 0:
                self.buttonBeli_1.setDisabled(True)
            if item[1]["stok"] == 0:
                self.buttonBeli_2.setDisabled(True)
            if item[2]["stok"] == 0:
                self.buttonBeli_3.setDisabled(True)
            if item[3]["stok"] == 0:
                self.buttonBeli_4.setDisabled(True)
            
        disabledButton(self)
        self.buttonBeli_1.clicked.connect(self.gotoqrHydrococo)
        self.buttonBeli_2.clicked.connect(self.gotoqrIndomilk)
        self.buttonBeli_3.clicked.connect(self.gotoqrPocky)
        self.buttonBeli_4.clicked.connect(self.gotoqrNabati)
        self.keMain2.clicked.connect(self.gotoMain2)
    
    def gotoMain2(self):
        self.timer.stop()
        mainwindow2 = MainWindow2()
        widget.addWidget(mainwindow2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrHydrococo(self):
        self.timer.stop()
        qrhydrococo = qrHydrococo()
        widget.addWidget(qrhydrococo)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrIndomilk(self):
        self.timer.stop()
        qrindomilk = qrIndomilk()
        widget.addWidget(qrindomilk)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrPocky(self):
        self.timer.stop()
        qrpocky = qrPocky()
        widget.addWidget(qrpocky)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrNabati(self):
        self.timer.stop()
        qrnabati = qrNabati()
        widget.addWidget(qrnabati)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoadsWindow(self):
        self.timer.stop()
        adswindow = AdsWindow()
        widget.addWidget(adswindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

### MAIN 2 ###
class MainWindow2(QDialog):
    def __init__(self):
        super(MainWindow2, self).__init__()
        loadUi("altMain2.ui", self)

        # nama produk
        self.label_5.setText(item[4]["nama"])
        self.label_6.setText(item[5]["nama"])

        # nama produk
        self.harga_5.setText(item[4]["harga"])
        self.harga_6.setText(item[5]["harga"])

        # kuantitas produk
        self.quantity_5.setText(str(item[4]["stok"]))
        self.quantity_6.setText(str(item[5]["stok"]))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.gotoadsWindow)
        self.timer.start(30000) ## dalam 30 detik akan kembali ke adsWindow

        # button
        def disabledButton(self): ## tombol akan dinonaktifkan apabila stok 0
            if item[4]["stok"] == 0:
                    self.buttonBeli_5.setDisabled(True)
            if item[5]["stok"] == 0:
                    self.buttonBeli_6.setDisabled(True)
        
        disabledButton(self)
        self.buttonBeli_5.clicked.connect(self.gotoqrTehPucuk)
        self.buttonBeli_6.clicked.connect(self.gotoqrNutriBoost)
        self.keMain1.clicked.connect(self.gotoMain)

    def gotoMain(self):
        self.timer.stop()
        widget.addWidget(MainWindow())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrTehPucuk(self):
        self.timer.stop()
        qrtehpucuk = qrTehPucuk()
        widget.addWidget(qrtehpucuk)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoqrNutriBoost(self):
        self.timer.stop()
        qrnutriboost = qrNutriBoost()
        widget.addWidget(qrnutriboost)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoadsWindow(self):
        self.timer.stop()
        adswindow = AdsWindow()
        widget.addWidget(adswindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

### WINDOW QR ####
class qrHydrococo(QDialog):
    def __init__(self):
        super(qrHydrococo, self).__init__()
        loadUi("qrHydrococo.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr = "https://drive.google.com/file/d/13zSSpEyM60MoNjsFDcsaamlksC2FqDCz/view?usp=sharing"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
        
    def beliBarang(self):
        item[0]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[0]["stok"] == 0:
                self.scanButton.setDisabled(True)

    def gotomenu(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class qrIndomilk(QDialog):
    def __init__(self):
        super(qrIndomilk, self).__init__()
        loadUi("qrIndomilk.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr = "https://drive.google.com/file/d/156yB5FinqAC-g3nQl2zdhCDQW90ZxbwL/view?usp=drive_link"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    
    def gotomenu(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def beliBarang(self):
        item[1]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[1]["stok"] == 0:
                self.scanButton.setDisabled(True)

class qrPocky(QDialog):
    def __init__(self):
        super(qrPocky, self).__init__()
        loadUi("qrPocky.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr = "https://drive.google.com/file/d/1K8cOOVmPkXaZiohdX8HKoYCgRRYKv_Y2/view?usp=sharing"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    
    def gotomenu(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def beliBarang(self):
        item[2]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[2]["stok"] == 0:
                self.scanButton.setDisabled(True)

class qrNabati(QDialog):
    def __init__(self):
        super(qrNabati, self).__init__()
        loadUi("qrNabati.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr = "https://drive.google.com/file/d/1lg1Wp-DlBuLAaXKY5Udy8bNX0lhHn6Fp/view?usp=sharing"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    
    
    def gotomenu(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def beliBarang(self):
        item[3]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[3]["stok"] == 0:
                self.scanButton.setDisabled(True)

class qrTehPucuk(QDialog):
    def __init__(self):
        super(qrTehPucuk, self).__init__()
        loadUi("qrTehPucuk.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr ="https://drive.google.com/file/d/1hYzJPoUSQv2yM_gEMso-RmUFVfHml0ev/view?usp=sharing"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    
    def gotomenu(self):
        mainwindow2 = MainWindow2()
        widget.addWidget(mainwindow2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def beliBarang(self):
        item[4]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[4]["stok"] == 0:
                self.scanButton.setDisabled(True)

class qrNutriBoost(QDialog):
    def __init__(self):
        super(qrNutriBoost, self).__init__()
        loadUi("qrNutriBoost.ui", self)
        self.kembaliMenu.clicked.connect(self.gotomenu)
        self.scanButton.clicked.connect(self.scanQR)

    def scanQR(self):
        qr ="https://drive.google.com/file/d/1d9gbCVvlMuRnTdhB5kP2tPyJOEH3F-1x/view?usp=sharing"
        cap=cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img=cap.read()
            data,one,_ = detector.detectAndDecode(img)
            if data == qr:
                self.beliBarang()
                break
            cv2.imshow("QR Scanner", img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
    
    def gotomenu(self):
        mainwindow2 = MainWindow2()
        widget.addWidget(mainwindow2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def beliBarang(self):
        item[5]["stok"] -= 1
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        if item[5]["stok"] == 0:
                self.scanButton.setDisabled(True)

# Adsmain
app = QApplication(sys.argv)
adswindow = AdsWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(adswindow)
widget.setFixedHeight(722)
widget.setFixedWidth(630)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")


