# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(10, 10, 641, 391))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")

        self.btn_start_camera = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_camera.setGeometry(QtCore.QRect(670, 120, 121, 31))
        self.btn_start_camera.setObjectName("btn_start_camera")

        self.btn_recognize_plate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_recognize_plate.setGeometry(QtCore.QRect(670, 20, 121, 31))
        self.btn_recognize_plate.setObjectName("btn_recognize_plate")

        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(670, 70, 121, 31))
        self.btn_save.setObjectName("btn_save")

        self.text_plate_result = QtWidgets.QTextEdit(self.centralwidget)
        self.text_plate_result.setGeometry(QtCore.QRect(10, 450, 641, 91))
        self.text_plate_result.setObjectName("text_plate_result")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plaka Tanıma Sistemi"))
        self.btn_start_camera.setText(_translate("MainWindow", "Kamerayı Başlat"))
        self.btn_recognize_plate.setText(_translate("MainWindow", "Tanı"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))

