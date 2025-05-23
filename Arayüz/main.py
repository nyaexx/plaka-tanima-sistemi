# -*- coding: utf-8 -*-

import sys
import os
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QTimer

# Kendi arayüz dosyalarımızı import ediyoruz
from plaka_arayuz import Ui_MainWindow
from plakakaydet import Ui_plakaeklemepenceresi
from splash_screen import SplashScreen  # Yeni import


class PlakaEklemeDialog(QDialog):
    """Plaka ekleme penceresi için dialog sınıfı"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_plakaeklemepenceresi()
        self.ui.setupUi(self)
        
        # Pencere özelliklerini ayarla
        self.setModal(True)  # Modal pencere yap
        self.setWindowTitle("Plaka Ekle")
        
        # Buton bağlantıları
        self.ui.pushButton.clicked.connect(self.reject)  # İptal butonu
        self.ui.pushButton_2.clicked.connect(self.accept)  # Ekle butonu
        
        # Enter tuşu ile de ekleyebilmek için
        self.ui.lineEdit.returnPressed.connect(self.accept)
        
        self.plaka_text = ""
        self.isim_text = ""
        
        # LineEdit'e odaklan
        self.ui.lineEdit.setFocus()
    
    def accept(self):
        """Ekle butonuna basıldığında çalışır"""
        self.plaka_text = self.ui.lineEdit.text().strip().upper()
        self.isim_text = self.ui.lineEdit_isim.text().strip()
        
        if not self.plaka_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir plaka giriniz!")
            self.ui.lineEdit.setFocus()
            return
            
        if not self.isim_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen isim giriniz!")
            self.ui.lineEdit_isim.setFocus()
            return
        
        if self.validate_plate(self.plaka_text):
            super().accept()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen geçerli bir plaka formatı giriniz!\nÖrnek: 34ABC123")
            self.ui.lineEdit.selectAll()
    
    def validate_plate(self, plaka):
        """Basit plaka doğrulaması"""
        # Türk plaka formatı kontrolü (basit)
        if len(plaka) < 6 or len(plaka) > 9:
            return False
        
        # En az bir harf ve bir rakam içermeli
        has_letter = any(c.isalpha() for c in plaka)
        has_digit = any(c.isdigit() for c in plaka)
        
        return has_letter and has_digit
    
    def get_data(self):
        """Girilen plaka ve ismi döndürür"""
        return self.plaka_text, self.isim_text


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Pencere ayarları
        self.setWindowTitle("Plaka Tanıma Sistemi v1.0")
        self.setMinimumSize(1200, 600)
        
        # Plakalar dosyası
        self.plakalar_dosyasi = "plakalar.txt"
        
        # Başlangıçta anasayfayı göster
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        
        # Buton bağlantıları
        self.setup_connections()
        
        # Plakalar sayfasını yükle
        self.load_plates()
        
        # Başlangıç buton stilini ayarla
        self.update_button_styles('home')
        
        # Bariyer durumunu başlat
        self.barrier_open = False
        
        # Plaka sayacı
        self.plate_count = self.get_plate_count()
        
        # Durum çubuğunda bilgi göster
        self.statusBar().showMessage(f"Sistem hazır - Kayıtlı plaka sayısı: {self.plate_count}")
    
    def setup_connections(self):
        """Buton bağlantılarını kurar"""
        # Menü butonları
        self.ui.btn_home.clicked.connect(self.show_home)
        self.ui.btn_plates.clicked.connect(self.show_plates)
        self.ui.btn_about.clicked.connect(self.show_about)
        self.ui.btn_ayarlar.clicked.connect(self.show_settings)
        
        # Plakalar sayfası butonları
        self.ui.btn_save_plate.clicked.connect(self.save_plate)
        self.ui.btn_clear_plate.clicked.connect(self.clear_plates)
        
        # Diğer butonlar
        self.ui.bariyer_kont.clicked.connect(self.toggle_barrier)
        self.ui.btn_manual.clicked.connect(self.show_manual)
    
    def show_home(self):
        """Anasayfa göster"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.update_button_styles('home')
        self.statusBar().showMessage("Anasayfa - Kamera görüntüsü burada gösterilecek")
    
    def show_plates(self):
        """Plakalar sayfasını göster"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_plates)
        self.update_button_styles('plates')
        self.load_plates()
        self.statusBar().showMessage(f"Plakalar - Toplam {self.plate_count} plaka kayıtlı")
    
    def show_about(self):
        """Hakkında sayfasını göster"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_about)
        self.update_button_styles('about')
        self.statusBar().showMessage("Hakkında - Sistem bilgileri")
    
    def show_settings(self):
        """Ayarlar sayfasını göster"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_about)
        self.update_button_styles('settings')
        self.statusBar().showMessage("Ayarlar - Henüz aktif değil")
        QMessageBox.information(self, "Bilgi", "Ayarlar sayfası yakında eklenecektir.")
    
    def update_button_styles(self, active_button):
        """Aktif buton stilini günceller"""
        # Normal stil
        normal_style = """
            QPushButton {
                background-color: #68696b;
                color: #FFFFFF;
                border-radius: 8px;
                padding: 8px 15px;
                min-width: 0px;
                min-height: 0px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #777777;
            }
        """
        
        # Aktif stil
        active_style = """
            QPushButton {
                background-color: #787FF5;
                color: #FFFFFF;
                border-radius: 8px;
                padding: 8px 15px;
                min-width: 0px;
                min-height: 0px;
                font-weight: bold;
                border: 2px solid #6B73E8;
            }
            QPushButton:hover {
                background-color: #6B73E8;
            }
        """
        
        # Tüm butonları normal stile döndür
        buttons = [self.ui.btn_home, self.ui.btn_plates, self.ui.btn_about, self.ui.btn_ayarlar]
        for btn in buttons:
            btn.setStyleSheet(normal_style)
        
        # Aktif butonu vurgula
        if active_button == 'home':
            self.ui.btn_home.setStyleSheet(active_style)
        elif active_button == 'plates':
            self.ui.btn_plates.setStyleSheet(active_style)
        elif active_button == 'about':
            self.ui.btn_about.setStyleSheet(active_style)
        elif active_button == 'settings':
            self.ui.btn_ayarlar.setStyleSheet(active_style)
    
    def save_plate(self):
        """Plaka ekleme dialog'unu aç ve plakayı kaydet"""
        try:
            dialog = PlakaEklemeDialog(self)
            result = dialog.exec()
            
            if result == QDialog.DialogCode.Accepted:
                plaka, isim = dialog.get_data()
                if plaka and isim:
                    if self.add_plate_to_file(plaka, isim):
                        self.plate_count += 1
                        # Tabloyu temizle ve yeniden yükle
                        self.ui.table_plates.setRowCount(0)
                        self.load_plates()
                        self.statusBar().showMessage(f"Plaka '{plaka}' ({isim}) başarıyla kaydedildi")
                        QMessageBox.information(self, "Başarılı", f"Plaka '{plaka}' ({isim}) başarıyla kaydedildi!")
                    else:
                        QMessageBox.warning(self, "Uyarı", "Bu plaka zaten kayıtlı!")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dialog açılırken hata oluştu: {str(e)}")
    
    def add_plate_to_file(self, plaka, isim):
        """Plakayı dosyaya ekler - Duplicate kontrolü ile"""
        try:
            # Önce var olan plakaları kontrol et
            existing_plates = set()
            if os.path.exists(self.plakalar_dosyasi):
                with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                    for line in f:
                        if ' - ' in line:
                            existing_plate = line.split(' - ')[1].strip()
                            existing_plates.add(existing_plate)
            
            # Plaka zaten varsa False döndür
            if plaka in existing_plates:
                return False
            
            # Yeni plakayı ekle
            with open(self.plakalar_dosyasi, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp} - {plaka} - {isim}\n")
            return True
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Plaka kaydedilirken hata oluştu: {str(e)}")
            return False
    
    def get_plate_count(self):
        """Kayıtlı plaka sayısını döndürür"""
        try:
            if os.path.exists(self.plakalar_dosyasi):
                with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                    return len(f.readlines())
            return 0
        except:
            return 0
    
    def load_plates(self):
        """Kaydedilen plakaları yükler"""
        try:
            self.ui.table_plates.setRowCount(0)
            if os.path.exists(self.plakalar_dosyasi):
                with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if lines:
                        for index, line in enumerate(lines):
                            parts = line.strip().split(' - ')
                            if len(parts) >= 3:
                                tarih, plaka, isim = parts[0], parts[1], parts[2]
                                
                                # Yeni satır ekle
                                row_position = self.ui.table_plates.rowCount()
                                self.ui.table_plates.insertRow(row_position)
                                
                                # Verileri ekle
                                self.ui.table_plates.setItem(row_position, 0, QTableWidgetItem(tarih))
                                self.ui.table_plates.setItem(row_position, 1, QTableWidgetItem(plaka))
                                self.ui.table_plates.setItem(row_position, 2, QTableWidgetItem(isim))
                                
                                # Butonlar için widget
                                button_widget = QWidget()
                                button_layout = QHBoxLayout(button_widget)
                                button_layout.setContentsMargins(2, 2, 2, 2)
                                button_layout.setSpacing(4)
                                
                                # Düzenle butonu
                                edit_btn = QPushButton("✏️")
                                edit_btn.setStyleSheet("""
                                    QPushButton {
                                        background-color: #666867;
                                        color: white;
                                        border-radius: 4px;
                                        padding: 4px 8px;
                                        font-weight: bold;
                                        min-width: 24px;
                                    }
                                    QPushButton:hover {
                                        background-color: #666867;
                                    }
                                """)
                                edit_btn.clicked.connect(lambda checked, r=row_position: self.edit_plate_at_row(r))
                                
                                # Sil butonu
                                delete_btn = QPushButton("🗑️")
                                delete_btn.setStyleSheet("""
                                    QPushButton {
                                        background-color: #dc3545;
                                        color: white;
                                        border-radius: 4px;
                                        padding: 4px 8px;
                                        font-weight: bold;
                                        min-width: 24px;
                                    }
                                    QPushButton:hover {
                                        background-color: #c82333;
                                    }
                                """)
                                delete_btn.clicked.connect(lambda checked, r=row_position: self.delete_plate_at_row(r))
                                
                                # Butonları layout'a ekle
                                button_layout.addWidget(edit_btn)
                                button_layout.addWidget(delete_btn)
                                
                                # Widget'ı tabloya ekle
                                self.ui.table_plates.setCellWidget(row_position, 3, button_widget)
                
                # Satır yüksekliklerini ayarla
                self.ui.table_plates.resizeRowsToContents()
                
            self.plate_count = self.ui.table_plates.rowCount()
            self.statusBar().showMessage(f"Toplam {self.plate_count} plaka kayıtlı")
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Plakalar yüklenirken hata oluştu: {str(e)}")

    def edit_plate_at_row(self, row):
        """Seçili satırdaki plakayı düzenler"""
        try:
            plaka = self.ui.table_plates.item(row, 1).text()
            isim = self.ui.table_plates.item(row, 2).text()
            
            dialog = PlakaEklemeDialog(self)
            dialog.ui.lineEdit.setText(plaka)
            dialog.ui.lineEdit_isim.setText(isim)
            
            if dialog.exec() == QDialog.DialogCode.Accepted:
                yeni_plaka, yeni_isim = dialog.get_data()
                
                # Eğer plaka değiştiyse ve yeni plaka zaten varsa
                if yeni_plaka != plaka and self.plaka_exists(yeni_plaka):
                    QMessageBox.warning(self, "Uyarı", "Bu plaka zaten kayıtlı!")
                    return
                
                # Dosyayı güncelle
                if os.path.exists(self.plakalar_dosyasi):
                    with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    with open(self.plakalar_dosyasi, 'w', encoding='utf-8') as f:
                        for line in lines:
                            if f" - {plaka} -" in line:
                                # Tarihi koru, diğer bilgileri güncelle
                                tarih = line.split(' - ')[0]
                                f.write(f"{tarih} - {yeni_plaka} - {yeni_isim}\n")
                            else:
                                f.write(line)
                
                # Tabloyu güncelle
                self.load_plates()
                self.statusBar().showMessage(f"Plaka '{plaka}' başarıyla güncellendi")
                QMessageBox.information(self, "Başarılı", f"Plaka '{plaka}' başarıyla güncellendi!")
        
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Plaka düzenlenirken hata oluştu: {str(e)}")
    
    def plaka_exists(self, plaka):
        """Plaka kayıtlı mı kontrol eder"""
        if os.path.exists(self.plakalar_dosyasi):
            with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                for line in f:
                    if f" - {plaka} -" in line:
                        return True
        return False
    
    def delete_plate_at_row(self, row):
        """Seçili satırdaki plakayı siler"""
        try:
            plaka = self.ui.table_plates.item(row, 1).text()
            reply = QMessageBox.question(
                self,
                "Onay",
                f"'{plaka}' plakasını silmek istediğinizden emin misiniz?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                # Dosyadan plakayı sil
                if os.path.exists(self.plakalar_dosyasi):
                    with open(self.plakalar_dosyasi, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    with open(self.plakalar_dosyasi, 'w', encoding='utf-8') as f:
                        for line in lines:
                            if f" - {plaka} -" not in line:
                                f.write(line)
                
                # Tablodan satırı sil
                self.ui.table_plates.removeRow(row)
                self.plate_count -= 1
                
                self.statusBar().showMessage(f"Plaka '{plaka}' başarıyla silindi")
                QMessageBox.information(self, "Başarılı", f"Plaka '{plaka}' başarıyla silindi!")
        
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Plaka silinirken hata oluştu: {str(e)}")
    
    def clear_plates(self):
        """Tüm plakaları sil"""
        if self.plate_count == 0:
            QMessageBox.information(self, "Bilgi", "Silinecek plaka bulunmamaktadır.")
            return
        
        reply = QMessageBox.question(
            self, 
            "Onay", 
            f"Toplam {self.plate_count} plaka silinecek. Emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                if os.path.exists(self.plakalar_dosyasi):
                    os.remove(self.plakalar_dosyasi)
                    self.plate_count = 0
                    self.ui.table_plates.setRowCount(0)
                    self.statusBar().showMessage("Tüm plakalar başarıyla silindi")
                    QMessageBox.information(self, "Başarılı", "Tüm plakalar başarıyla silindi!")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Plakalar silinirken hata oluştu: {str(e)}")
    
    def toggle_barrier(self):
        """Bariyer kontrolü (toggle)"""
        if not self.barrier_open:
            # Bariyer aç
            self.barrier_open = True
            self.ui.bariyer_kont.setText("Bariyeri Kapat")
            self.ui.bariyer_kont.setStyleSheet("""
                QPushButton {
                    background-color: #dc3545;
                    border-radius: 8px;
                    padding: 10px 20px;
                    color: white;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #c82333;
                }
            """)
            self.statusBar().showMessage("Bariyer AÇIK durumda")
        else:
            # Bariyer kapat
            self.barrier_open = False
            self.ui.bariyer_kont.setText("Bariyeri Aç")
            self.ui.bariyer_kont.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    border-radius: 8px;
                    padding: 10px 20px;
                    color: white;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
            """)
            self.statusBar().showMessage("Bariyer KAPALI durumda")
    
    def show_manual(self):
        """Kullanım kılavuzunu göster"""
        manual_text = """
🚗 PLAKA TANIMA SİSTEMİ KULLANIM KILAVUZU v1.0

📍 ANASAYFA:
• Kamera görüntüsü bu bölümde gösterilir
• Plaka görüntüsü alt kısımda görüntülenir  
• Bariyer kontrolü sağ alt köşededir
• Yeşil buton: Bariyer kapalı (Bariyeri Aç)
• Kırmızı buton: Bariyer açık (Bariyeri Kapat)

📋 PLAKALAR:
• Kaydedilen tüm plakalar tarih/saat ile listelenir
• "Plakayı Kaydet" butonu ile yeni plaka ekleyebilirsiniz
• Plaka formatı kontrol edilir (örn: 34ABC123)
• Aynı plaka tekrar kaydedilmez
• "Hepsini Sil" butonu ile tüm plakaları silebilirsiniz

ℹ️ HAKKINDA:
• Sistem hakkında bilgiler bu bölümde yer alır
• Bu kullanım kılavuzuna buradan ulaşabilirsiniz

⚙️ AYARLAR:
• Sistem ayarları (yakında eklenecek)

💡 İPUÇLARI:
• Plaka eklerken Enter tuşuna basabilirsiniz
• Plakalar otomatik büyük harfe çevrilir
• Durum çubuğundan sistem durumunu takip edebilirsiniz
• Modal pencereler dışarı tıklanarak kapatılabilir

🔧 SİSTEM BİLGİLERİ:
• Versiyon: 1.0
• Platform: PySide6 / Qt
• Dosya formatı: UTF-8 Text
        """
        
        # Daha büyük bir mesaj kutusu için QMessageBox'ın özelliklerini ayarla
        msg = QMessageBox(self)
        msg.setWindowTitle("Kullanım Kılavuzu")
        msg.setText(manual_text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def closeEvent(self, event):
        """Pencere kapatılırken çalışır"""
        reply = QMessageBox.question(
            self,
            "Çıkış",
            "Programdan çıkmak istediğinizden emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    """Ana fonksiyon - Kesin çözüm"""
    app = QApplication(sys.argv)
    
    try:
        # Splash screen oluştur ve ayarla
        splash = SplashScreen()
        splash.setWindowFlags(
            Qt.WindowType.SplashScreen | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.FramelessWindowHint
        )
        splash.show()
        splash.raise_()
        splash.activateWindow()
        app.processEvents()
        
        print("Splash screen gösterildi")
        
        # Ana pencereyi oluştur ama gösterme
        window = MainWindow()
        
        print("Ana pencere oluşturuldu")
        
        def show_main_window():
            """Ana pencereyi göster ve splash'i kapat"""
            try:
                # Splash'i kapat
                splash.close()
                splash.deleteLater()
                
                # Ana pencereyi göster
                window.showMaximized()
                window.raise_()
                window.activateWindow()
                
                print("Ana pencere başarıyla gösterildi")
                
            except Exception as e:
                print(f"Ana pencere gösterilirken hata: {e}")
        
        # 2 saniye sonra ana pencereyi göster
        QTimer.singleShot(2000, show_main_window)
        
        print("Timer başlatıldı")
        
        return app.exec()
        
    except Exception as e:
        error_msg = f"Uygulama başlatılırken hata oluştu:\n{str(e)}"
        print(error_msg)
        QMessageBox.critical(None, "Kritik Hata", error_msg)
        return 1

if __name__ == "__main__":
    sys.exit(main())