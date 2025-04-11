import os
import time

# Önceden belirlenen plakalar
onayli_plakalar = ["41BT996", "34AB123", "06XYZ789"]  # Burada kontrol etmek istediğiniz plakaları ekleyin

# plaka_bilgileri.txt dosyasının son değiştirilme zamanını kaydet
txt_dosya = "plaka_bilgileri.txt"
son_degisiklik_zamani = os.path.getmtime(txt_dosya)

# Dosya değişikliklerini takip et
while True:
    # Dosyanın son değiştirilme zamanını kontrol et
    current_mod_time = os.path.getmtime(txt_dosya)

    # Eğer dosya değişmişse, son plaka bilgisini kontrol et
    if current_mod_time != son_degisiklik_zamani:
        son_degisiklik_zamani = current_mod_time

        # Son satırdaki plaka bilgisini oku
        with open(txt_dosya, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # Son satırdaki plaka bilgisini al
        son_plaka = satirlar[-1].strip()  # Son satırı alıyoruz, strip() boşlukları temizler

        # Plakayı doğrula
        if son_plaka in onayli_plakalar:
            print(f"Plaka Tanındı, Kapı açılıyor: {son_plaka}")
        else:
            print(f"Tanımlanan plaka geçersiz: {son_plaka}")

    # 2 saniye bekle ve tekrar kontrol et
    time.sleep(2)
