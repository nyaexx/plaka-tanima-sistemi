import sys
import os
import cv2
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout,
    QLabel, QHBoxLayout, QTextEdit, QStackedWidget, QMessageBox
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plaka Tanıma Sistemi")
        self.setGeometry(100, 100, 900, 600)

        self.capture = None  # OpenCV kamera objesi
        self.timer = QTimer()  # Görüntüyü sürekli güncellemek için zamanlayıcı
        self.timer.timeout.connect(self.update_frame)

        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Menü (sol)
        menu_layout = QVBoxLayout()
        main_layout.addLayout(menu_layout, 1)

        self.btn_home = QPushButton("Anasayfa")
        self.btn_plates = QPushButton("Plakalar")
        self.btn_about = QPushButton("Hakkında")

        for btn in [self.btn_home, self.btn_plates, self.btn_about]:
            btn.setFixedHeight(50)
            menu_layout.addWidget(btn)

        menu_layout.addStretch()

        # Sayfa alanı (sağ)
        self.pages = QStackedWidget()
        main_layout.addWidget(self.pages, 4)

        # Sayfaları oluştur
        self.home_page = self.create_home_page()
        self.plates_page = self.create_plates_page()
        self.about_page = self.create_about_page()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.plates_page)
        self.pages.addWidget(self.about_page)

        # Butonlara sayfa geçişi bağla
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.home_page))
        self.btn_plates.clicked.connect(lambda: self.pages.setCurrentWidget(self.plates_page))
        self.btn_about.clicked.connect(lambda: self.pages.setCurrentWidget(self.about_page))

    def create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)

        self.camera_label = QLabel("Kamera Görüntüsü Burada Gözükecek")
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setStyleSheet("background-color: #e0e0e0; font-size: 16px;")
        self.camera_label.setFixedHeight(400)
        layout.addWidget(self.camera_label)

        self.btn_start_camera = QPushButton("🎥 Kamerayı Başlat")
        self.btn_start_camera.clicked.connect(self.start_camera)
        layout.addWidget(self.btn_start_camera)

        # Ek bilgiler
        layout.addWidget(QLabel("Durum: Kamera henüz başlatılmadı."))
        layout.addWidget(QLabel("📌 İpucu: Tanımayı başlatmak için kamerayı başlatın."))

        return page

    def start_camera(self):
        self.capture = cv2.VideoCapture(0)  # 0: Dahili kamera
        if not self.capture.isOpened():
            QMessageBox.critical(self, "Hata", "Kamera başlatılamadı.")
            return
        self.timer.start(30)  # 30 ms'de bir görüntü güncelle

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.camera_label.setPixmap(QPixmap.fromImage(qimg))

    def create_plates_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)

        self.plate_text = QTextEdit()
        layout.addWidget(QLabel("📄 Kayıtlı Plakalar:"))
        layout.addWidget(self.plate_text)

        btn_save_plate = QPushButton("Plakayı Kaydet")
        btn_clear_file = QPushButton("Tümünü Sil")
        layout.addWidget(btn_save_plate)
        layout.addWidget(btn_clear_file)

        btn_save_plate.clicked.connect(self.save_plate)
        btn_clear_file.clicked.connect(self.clear_file)

        self.load_plates()

        return page

    def create_about_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)

        label_title = QLabel("Projeyi Yapanlar")
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(label_title)

        names = ["Ubeyd", "Yunus", "Ömer", "Ali"]
        for name in names:
            lbl = QLabel(name)
            lbl.setAlignment(Qt.AlignCenter)
            layout.addWidget(lbl)

        btn_manual = QPushButton("📘 Kullanım Kılavuzu")
        btn_manual.clicked.connect(self.open_manual)
        layout.addStretch()
        layout.addWidget(btn_manual)

        return page

    def load_plates(self):
        if os.path.exists("plakalar.txt"):
            with open("plakalar.txt", "r", encoding="utf-8") as f:
                self.plate_text.setPlainText(f.read())

    def save_plate(self):
        text = self.plate_text.toPlainText()
        with open("plakalar.txt", "w", encoding="utf-8") as f:
            f.write(text)
        QMessageBox.information(self, "Kaydedildi", "Plakalar kaydedildi.")

    def clear_file(self):
        with open("plakalar.txt", "w", encoding="utf-8") as f:
            f.write("")
        self.plate_text.clear()
        QMessageBox.information(self, "Temizlendi", "Tüm plakalar silindi.")

    def open_manual(self):
        QMessageBox.information(
            self,
            "Kullanım Kılavuzu",
            "Kamera: Ana sayfadan başlatılır.\nPlakalar: Yazıp kaydedin.\nHakkında: Proje bilgileri yer alır.",
        )

    def closeEvent(self, event):
        if self.capture:
            self.timer.stop()
            self.capture.release()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
