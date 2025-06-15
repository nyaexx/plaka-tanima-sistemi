# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plakakaydet.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_plakaeklemepenceresi(object):
    def setupUi(self, plakaeklemepenceresi):
        if not plakaeklemepenceresi.objectName():
            plakaeklemepenceresi.setObjectName(u"plakaeklemepenceresi")
        plakaeklemepenceresi.resize(400, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(plakaeklemepenceresi.sizePolicy().hasHeightForWidth())
        plakaeklemepenceresi.setSizePolicy(sizePolicy)
        plakaeklemepenceresi.setMinimumSize(QSize(400, 500))
        plakaeklemepenceresi.setMaximumSize(QSize(400, 500))
        plakaeklemepenceresi.setStyleSheet(u"QWidget {\n"
"    background-color: #36393E;\n"
"}\n"
"")
        self.frame = QFrame(plakaeklemepenceresi)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(19, 80, 361, 381))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #1e2124;\n"
" 	border-radius: 6px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Plaka giriş alanı
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(12, 26, 331, 51))
        self.lineEdit.setStyleSheet(u"""
            QLineEdit {
                background-color: #2f3136;
                color: #ffffff;
                border: 2px solid #40444b;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit:focus {
                border: 2px solid #787FF5;
                background-color: #36393f;
            }
            QLineEdit:hover {
                border: 2px solid #555555;
            }
        """)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setPlaceholderText("Plaka giriniz (örn: 34ABC123)")
        self.lineEdit.setMaxLength(10)  # Maksimum 10 karakter

        # İsim giriş alanı
        self.lineEdit_isim = QLineEdit(self.frame)
        self.lineEdit_isim.setObjectName(u"lineEdit_isim")
        self.lineEdit_isim.setGeometry(QRect(12, 90, 331, 51))
        self.lineEdit_isim.setStyleSheet(u"""
            QLineEdit {
                background-color: #2f3136;
                color: #ffffff;
                border: 2px solid #40444b;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit:focus {
                border: 2px solid #787FF5;
                background-color: #36393f;
            }
            QLineEdit:hover {
                border: 2px solid #555555;
            }
        """)
        self.lineEdit_isim.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_isim.setPlaceholderText("İsim Soyisim giriniz")
        self.lineEdit_isim.setMaxLength(50)
        
        # Bilgi gösterme alanı
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(15, 160, 321, 120))
        self.textBrowser.setStyleSheet(u"""
            QTextBrowser {
                background-color: #2f3136;
                color: #ffffff;
                border: 2px solid #40444b;
                border-radius: 8px;
                padding: 8px;
                font-size: 12px;
            }
        """)
        self.textBrowser.setHtml(u"""
            <div style='color: #ffffff; font-family: Arial;'>
                <h3 style='color: #787FF5; margin-top: 5px;'>📋 Plaka Giriş Bilgileri:</h3>
                <ul style='margin: 10px 0;'>
                    <li><b>Format:</b> 34ABC123 (il kodu + harfler + rakamlar)</li>
                    <li><b>Uzunluk:</b> 6-9 karakter arası</li>
                    <li><b>İçerik:</b> En az 1 harf ve 1 rakam</li>
                    <li><b>Not:</b> Boşluk ve özel karakter kullanmayın</li>
                </ul>
                <p style='color: #43b581; font-size: 11px;'><b>💡 İpucu:</b> Enter tuşu ile de ekleyebilirsiniz!</p>
            </div>
        """)
        
        # İptal butonu
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 290, 131, 41))
        self.pushButton.setStyleSheet(u"""
            QPushButton {
                background-color: #747f8d;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5d6572;
            }
            QPushButton:pressed {
                background-color: #4a5058;
            }
        """)
        
        # Ekle butonu
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 290, 131, 41))
        self.pushButton_2.setStyleSheet(u"""
            QPushButton {
                background-color: #43b581;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3ca374;
            }
            QPushButton:pressed {
                background-color: #369268;
            }
        """)
        
        # Başlık etiketi
        self.label = QLabel(plakaeklemepenceresi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 19, 361, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(QFont.Weight.Normal)
        self.label.setFont(font)
        self.label.setStyleSheet(u"""
            QLabel {
                background-color: #1e2124;
                color: #ffffff;
                border-radius: 6px;
                padding: 8px;
                border: 2px solid #787FF5;
            }
        """)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Karakter sayacı etiketi
        self.label_counter = QLabel(self.frame)
        self.label_counter.setObjectName(u"label_counter")
        self.label_counter.setGeometry(QRect(15, 240, 321, 25))
        self.label_counter.setStyleSheet(u"""
            QLabel {
                color: #72767d;
                font-size: 12px;
                background: transparent;
            }
        """)
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_counter.setText("0/10 karakter")

        # Enter tuşu bağlantılarını ayarla
        self.lineEdit.returnPressed.connect(lambda: self.lineEdit_isim.setFocus())
        self.lineEdit_isim.returnPressed.connect(lambda: self.pushButton_2.click())

        self.retranslateUi(plakaeklemepenceresi)

        QMetaObject.connectSlotsByName(plakaeklemepenceresi)
    # setupUi

    def retranslateUi(self, plakaeklemepenceresi):
        plakaeklemepenceresi.setWindowTitle(QCoreApplication.translate("plakaeklemepenceresi", u"Plaka Ekle", None))
        self.pushButton.setText(QCoreApplication.translate("plakaeklemepenceresi", u"❌ İptal", None))
        self.pushButton_2.setText(QCoreApplication.translate("plakaeklemepenceresi", u"✅ Ekle", None))
        self.label.setText(QCoreApplication.translate("plakaeklemepenceresi", u"🚗 Plaka Ekle", None))
    # retranslateUi