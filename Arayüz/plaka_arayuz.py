# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plaka_arayuz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#plakaarayuz.py

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1398, 657)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #36393E;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #282b30;\n"
" 	border-radius: 6px;\n"
"}")
        self.frame.setMinimumWidth(180)
        self.frame.setMaximumWidth(180)
        self.frame.setMinimumHeight(0)
        self.frame.setMaximumHeight(16777215)
        self.menuLayout = QVBoxLayout(self.frame)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setContentsMargins(8, 8, 8, 8)
        self.menuLayout.setSpacing(8)

        # Butonların ortak stil ve boyut ayarları
        button_style = """
            QPushButton {
                background-color: #68696b;
                color: #111111;
                border-radius: 6px;
                padding: 4px 15px;
                min-width: 0px;
                min-height: 0px;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """

        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setMinimumHeight(40)
        self.btn_home.setMaximumHeight(40)
        self.btn_home.setMinimumWidth(0)
        self.btn_home.setMaximumWidth(16777215)
        self.btn_home.setStyleSheet(button_style)
        self.menuLayout.addWidget(self.btn_home)
        self.btn_plates = QPushButton(self.frame)
        self.btn_plates.setObjectName(u"btn_plates")
        self.btn_plates.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plates.setMinimumHeight(40)
        self.btn_plates.setMaximumHeight(40)
        self.btn_plates.setMinimumWidth(0)
        self.btn_plates.setMaximumWidth(16777215)
        self.btn_plates.setStyleSheet(button_style)
        self.menuLayout.addWidget(self.btn_plates)
        self.btn_about = QPushButton(self.frame)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_about.setMinimumHeight(40)
        self.btn_about.setMaximumHeight(40)
        self.btn_about.setMinimumWidth(0)
        self.btn_about.setMaximumWidth(16777215)
        self.btn_about.setStyleSheet(button_style)
        self.menuLayout.addWidget(self.btn_about)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menuLayout.addItem(self.verticalSpacer)

        self.btn_ayarlar = QPushButton(self.frame)
        self.btn_ayarlar.setObjectName(u"btn_ayarlar")
        self.btn_ayarlar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ayarlar.setMinimumHeight(40)
        self.btn_ayarlar.setMaximumHeight(40)
        self.btn_ayarlar.setMinimumWidth(0)
        self.btn_ayarlar.setMaximumWidth(16777215)
        self.btn_ayarlar.setStyleSheet(button_style)
        self.menuLayout.addWidget(self.btn_ayarlar)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_home = QVBoxLayout(self.page_home)
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")
        self.label_camera = QLabel(self.page_home)
        self.label_camera.setObjectName(u"label_camera")
        self.label_camera.setMinimumSize(QSize(700, 430))
        self.label_camera.setMaximumSize(QSize(700, 430))
        self.label_camera.setSizeIncrement(QSize(70, 90))
        self.label_camera.setStyleSheet(u"QLabel {\n"
"    background-color: #282b30;\n"
" 	border-radius: 6px;\n"
"}")
        self.label_camera.setFrameShape(QFrame.NoFrame)
        self.label_camera.setAlignment(Qt.AlignCenter)

        self.verticalLayout_home.addWidget(self.label_camera, 0, Qt.AlignTop)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(700, 135))
        self.label.setMaximumSize(QSize(700, 135))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #282b30;\n"
" 	border-radius: 6px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.verticalFrame = QFrame(self.page_home)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(600, 135))
        self.verticalFrame.setMaximumSize(QSize(600, 135))
        self.verticalFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #282b30;\n"
" 	border-radius: 6px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bariyer_kont = QPushButton(self.verticalFrame)
        self.bariyer_kont.setObjectName(u"bariyer_kont")
        self.bariyer_kont.setMinimumSize(QSize(550, 115))
        self.bariyer_kont.setMaximumSize(QSize(550, 115))
        self.bariyer_kont.setStyleSheet(u"QPushButton {\n"
"    background-color: #377c27;      /* Ba\u015flang\u0131\u00e7 rengi */\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c9628;      /* Ba\u015flang\u0131\u00e7ta hover rengi */\n"
"}\n"
"\n"
"/* \"bas\u0131ld\u0131\" stili \u2192 Python taraf\u0131nda toggle edilince bu s\u0131n\u0131f eklenir */\n"
"QPushButton#active {\n"
"    background-color: #7c2f27;      /* Bas\u0131ld\u0131ktan sonraki rengi */\n"
"}\n"
"\n"
"QPushButton#active:hover {\n"
"    background-color: #962c22;      /* Bas\u0131l\u0131yken hover rengi */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.bariyer_kont)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.verticalFrame, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_home.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page_home)
        self.page_plates = QWidget()
        self.page_plates.setObjectName(u"page_plates")
        self.verticalLayout_plates = QVBoxLayout(self.page_plates)
        self.verticalLayout_plates.setObjectName(u"verticalLayout_plates")
        
        # Plaka tablosu
        self.table_plates = QTableWidget(self.page_plates)
        self.table_plates.setObjectName(u"table_plates")
        self.table_plates.setStyleSheet(u"""
            QTableWidget {
                background-color: #2f3136;
                color: #ffffff;
                border: 2px solid #40444b;
                border-radius: 8px;
                gridline-color: #40444b;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #40444b;
            }
            QTableWidget::item:selected {
                background-color: #787FF5;
            }
            QHeaderView::section {
                background-color: #202225;
                color: #ffffff;
                padding: 5px;
                border: none;
                border-bottom: 2px solid #40444b;
                font-weight: bold;
            }
        """)
        
        # Tablo ayarları
        self.table_plates.setColumnCount(4)
        self.table_plates.setHorizontalHeaderLabels(["Tarih", "Plaka", "İsim", "İşlem"])
        header = self.table_plates.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setDefaultSectionSize(100)
        self.table_plates.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table_plates.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.verticalLayout_plates.addWidget(self.table_plates)
        
        # Butonlar için yatay layout
        self.horizontalLayout_plates = QHBoxLayout()
        
        # Plaka ekle butonu
        self.btn_save_plate = QPushButton(self.page_plates)
        self.btn_save_plate.setObjectName(u"btn_save_plate")
        self.btn_save_plate.setStyleSheet(u"""
            QPushButton {
                background-color: #43b581;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3ca374;
            }
        """)
        self.btn_save_plate.setMinimumHeight(40)
        self.horizontalLayout_plates.addWidget(self.btn_save_plate)
        
        # Boşluk ekle
        self.horizontalLayout_plates.addSpacing(10)
        
        # Hepsini sil butonu
        self.btn_clear_plate = QPushButton(self.page_plates)
        self.btn_clear_plate.setObjectName(u"btn_clear_plate")
        self.btn_clear_plate.setStyleSheet(u"""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.btn_clear_plate.setMinimumHeight(40)
        self.horizontalLayout_plates.addWidget(self.btn_clear_plate)
        
        self.verticalLayout_plates.addLayout(self.horizontalLayout_plates)

        self.stackedWidget.addWidget(self.page_plates)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_about = QVBoxLayout(self.page_about)
        self.verticalLayout_about.setObjectName(u"verticalLayout_about")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame1 = QFrame(self.page_about)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"QFrame {\n"
"    background-color: #282b30;\n"
" 	border-radius: 6px;\n"
"}")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame1)


        self.verticalLayout_about.addLayout(self.verticalLayout_2)

        self.btn_manual = QPushButton(self.page_about)
        self.btn_manual.setObjectName(u"btn_manual")
        self.btn_manual.setStyleSheet(u"QPushButton {\n"
"    background-color: #68696b;       /* Arka plan beyaz */\n"
"    color: #111111;                  /* Yaz\u0131 rengi */\n"
"    border-radius: 8px;              /* K\u00f6\u015fe yumu\u015fatma */\n"
"    padding: 4px 15px;              /* Dikey 10px, Yatay 20px bo\u015fluk */\n"
"    min-width: 0px;                /* Minimum geni\u015flik */\n"
"    min-height: 0px;                /* Minimum y\u00fckseklik */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #777777;\n"
"}\n"
"FAD7B5")

        self.verticalLayout_about.addWidget(self.btn_manual)

        self.stackedWidget.addWidget(self.page_about)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1398, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plaka Tan\u0131ma Sistemi", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Anasayfa", None))
        self.btn_plates.setText(QCoreApplication.translate("MainWindow", u"Plakalar", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Hakk\u0131nda", None))
        self.btn_ayarlar.setText(QCoreApplication.translate("MainWindow", u"Ayarlar", None))
        self.label_camera.setText(QCoreApplication.translate("MainWindow", u"Kamera G\u00f6r\u00fcnt\u00fcs\u00fc Burada", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plaka G\u00f6r\u00fcnt\u00fcs\u00fc", None))
        self.bariyer_kont.setText(QCoreApplication.translate("MainWindow", u"Bariyeri A\u00e7", None))
        self.btn_save_plate.setText(QCoreApplication.translate("MainWindow", u"Plakay\u0131 Kaydet", None))
        self.btn_clear_plate.setText(QCoreApplication.translate("MainWindow", u"Hepsini Sil", None))
        self.btn_manual.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131m K\u0131lavuzu", None))
    # retranslateUi

