import cv2
import numpy as np
import os
import re
import time  # Zaman kontrolü için time modülü
from plaka_tespiti import plaka_konum_don
from alg2_plaka_tanima import plakaTani
import subprocess  # subprocess modülünü içe aktar

# Veri setinin bulunduğu dizin
veri_dizini = "veriseti"

# Veri setindeki tüm dosyaları listele
veriler = os.listdir(veri_dizini)

# plaka_bilgileri.txt dosyasını temizleyelim (yeni baştan yazalım)
with open("plaka_bilgileri.txt", "w", encoding="utf-8") as dosya:
    dosya.write("")  # Dosyayı sıfırlıyoruz

# Plaka doğrulama dosyasını arka planda çalıştırma
subprocess.Popen(["python", "plaka_dogrulama.py"])  # Bu satır, plaka_dogrulama.py dosyasını başlatır

# Her bir görsel için işlem yap
for isim in veriler:
    # Görseli oku
    img = cv2.imread(os.path.join(veri_dizini, isim))
    if img is None:
        print(f"{isim} dosyası okunamadı.")
        continue  # Bir sonraki görsele geç

    # Görseli boyutlandır
    img = cv2.resize(img, (500, 500))

    # Plaka tespiti yap
    plaka = plaka_konum_don(img)
    if plaka is None:
        print(f"{isim} için plaka tespit edilemedi.")
        continue  # Bir sonraki görsele geç

    # Plaka tanıma işlemi yap
    plakaImg, plakaKarakter = plakaTani(img, plaka)
    if plakaKarakter is None:
        print(f"{isim} için plaka karakterleri tanınamadı.")
        continue  # Bir sonraki görsele geç

    # Sadece harfler ve rakamlar kalacak şekilde temizleme
    temizlenmis_plaka = re.sub(r'[^a-zA-Z0-9]', '', str(plakaKarakter))

    # Plaka bilgisini bir metin dosyasına yazdırma
    with open("plaka_bilgileri.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"{temizlenmis_plaka}\n")  # Dosya adını kaldırdım, sadece plaka bilgisi yazılacak

    print(f"{isim} için plaka bilgisi 'plaka_bilgileri.txt' dosyasına yazıldı.")

    # 10 saniye bekle
    time.sleep(10)

print("Tüm plaka bilgileri 'plaka_bilgileri.txt' dosyasına yazıldı.")
