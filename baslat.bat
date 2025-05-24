@echo off
chcp 65001 > nul
color 0B

:: BURAYA ARAYÜZ KLASÖRÜNÜN TAM YOLUNU GİRİN
set "ARAYUZ_DIZINI=C:\Users\PC\Desktop\plaka-tanima-sistemi-main\arayuzv1\main.py"

cls
echo ===============================================
echo            PLAKA TANIMA SISTEMI
echo ===============================================
echo.

:: Python kontrolu
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    color 0C
    echo [HATA] Python bulunamadi! Lutfen Python'u yukleyin.
    pause
    exit /b 1
)

:: Dizin kontrolü ve geçiş
if not exist "%ARAYUZ_DIZINI%" (
    color 0C
    echo [HATA] Arayuz dizini bulunamadi: %ARAYUZ_DIZINI%
    echo Lutfen dosya konumunu kontrol edin.
    pause
    exit /b 1
)

cd /d "%ARAYUZ_DIZINI%"

:: Arayüz dosyası kontrolü
if not exist "main.py" (
    color 0C
    echo [HATA] Arayuz dosyasi (main.py) bulunamadi!
    pause
    exit /b 1
)

:: Arayüzü başlat
color 0A
echo [*] Arayuz baslatiliyor...
start "" python main.py

echo [+] Arayuz baslatildi!
echo.
timeout /t 3 >nul

