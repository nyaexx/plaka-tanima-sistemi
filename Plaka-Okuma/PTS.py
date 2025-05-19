import cv2
import numpy as np
import matplotlib.pyplot as plt
from plaka_tespiti import plaka_konum_don
from alg2_plaka_tanima import plakaTani

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    if not ret:
        print("Kameradan görüntü alınamıyor!")
        break

    img = cv2.resize(frame, (500, 500))

    try:
        plaka = plaka_konum_don(img)

        plakaImg, plakaKarakter = plakaTani(img, plaka)

        print("Tespit edilen plaka:", plakaKarakter)

        cv2.imshow('Kamera Görüntüsü', frame)

        plt.imshow(cv2.cvtColor(plakaImg, cv2.COLOR_BGR2RGB))  # OpenCV BGR formatını RGB'ye çevir
        plt.title(f"Tespit Edilen Plaka: {plakaKarakter}")
        plt.show()

    except Exception as e:
        print("Hata oluştu:", e)
        cv2.imshow('Kamera Görüntüsü', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
