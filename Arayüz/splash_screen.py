from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar, QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

class SplashScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Başlatılıyor")
        # Tam ekran ve bayraklar
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowState.WindowFullScreen)
        
        # Ana layout - iç içe düzen için
        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(outer_layout)
        
        # Arkaplan container'ı
        container = QWidget()
        container.setObjectName("container")
        container.setStyleSheet("""
            QWidget#container {
                background-color: #1e2124;
            }
        """)
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)
        
        # İçerik için merkez widget
        content = QWidget()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)
        
        # Başlık
        title = QLabel("Plaka Tanıma Sistemi")
        title.setStyleSheet("""
            color: white;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Alt başlık
        subtitle = QLabel("Sistem Başlatılıyor...")
        subtitle.setStyleSheet("""
            color: #787FF5;
            font-size: 18px;
            margin-bottom: 30px;
        """)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setFixedSize(400, 15)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #787FF5;
                border-radius: 7px;
                text-align: center;
                background-color: #2f3136;
            }
            QProgressBar::chunk {
                background-color: #787FF5;
                border-radius: 5px;
            }
        """)
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setTextVisible(False)
        
        # İçeriği düzenle
        content_layout.addStretch()
        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)
        content_layout.addWidget(self.progress, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addStretch()
        
        # Ana container'a ekle
        container_layout.addWidget(content)
        outer_layout.addWidget(container)
        
        # Timer başlat
        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(20)
    
    def update_progress(self):
        self.counter += 1
        self.progress.setValue(self.counter)
        if self.counter >= 100:
            self.timer.stop()
            self.close()
