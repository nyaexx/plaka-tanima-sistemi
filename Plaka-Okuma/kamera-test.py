import cv2
from alg2_plaka_tanima import plakaTani  # Plaka tanıma fonksiyonunun olduğu dosya

# Kamerayı başlat
cap = cv2.VideoCapture(0)

# Kamera çözünürlüğünü ayarlamıyoruz, varsayılan değer kullanılacak

# Pencereyi esnek yapalım
cv2.namedWindow("Plaka Tanıma", cv2.WINDOW_NORMAL)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    if not ret:
        print("Kamera açılmadı!")
        break

    # Plaka koordinatları (manuel olarak geçici verildi)
    plaka_koordinat = (100, 100, 300, 100)

    try:
        # Plaka tanıma işlemi
        sonuc_resim, mevcut_plaka = plakaTani(frame, plaka_koordinat)

        # Sonucu göster
        cv2.imshow("Plaka Tanıma", sonuc_resim)

        if mevcut_plaka:
            print("Tespit Edilen Plaka:", "".join(mevcut_plaka))
    except Exception as e:
        print("Hata oluştu:", e)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
