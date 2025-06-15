@echo off
setlocal EnableDelayedExpansion
chcp 65001 > nul
color 0B

:: Hata log dosyası için tarih-saat
set "LOG_DIR=logs"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "LOGS_FILE=%LOG_DIR%\hata_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%.txt"
set "LOGS_FILE=%LOGS_FILE: =0%"

:: Script konumunu al
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

:: Log fonksiyonu
:LogHata
echo %date% %time% - %~1 >> "%LOGS_FILE%"
echo [HATA] %~1
goto :eof

:: Başlık
cls
echo ===============================================
echo            PLAKA TANIMA SISTEMI
echo ===============================================
echo.

:: Python kontrolü
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    color 0C
    call :LogHata "Python bulunamadi! Lutfen Python'u yukleyin."
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    pause
    exit /b 1
)

:: Python sürüm kontrolü
python -c "import sys; sys.exit(0 if sys.version_info >= (3,8) else 1)" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    color 0C
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"
    call :LogHata "Python 3.8 veya ustu gerekli. Mevcut surum: !PYTHON_VERSION!"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    pause
    exit /b 1
)

:: Bağımlılıkları kontrol et
echo [*] Gerekli kutuphaneler kontrol ediliyor...
python -c "import PySide6" 2>nul
if %ERRORLEVEL% neq 0 (
    color 0E
    echo [!] PySide6 kutuphanesi bulunamadi. Yukleniyor...
    pip install PySide6
    if %ERRORLEVEL% neq 0 (
        color 0C
        call :LogHata "PySide6 yuklenemedi!"
        echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
        pause
        exit /b 1
    )
)

:: Gerekli dosyaları kontrol et
set "REQUIRED_FILES=main.py plaka_arayuz.py plakakaydet.py splash_screen.py"
for %%f in (%REQUIRED_FILES%) do (
    if not exist "%%f" (
        color 0C
        call :LogHata "Gerekli dosya bulunamadi: %%f"
        echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
        pause
        exit /b 1
    )
)

:: Arayüz başlatma
color 0A
echo [*] Arayuz baslatiliyor...

:: Ana programı çalıştır ve hataları logla
python main.py 2>>"%LOGS_FILE%"
if %ERRORLEVEL% neq 0 (
    color 0C
    call :LogHata "Arayuz baslatilirken hata olustu!"
    echo Son 5 satir hata logu:
    powershell -Command "Get-Content '%LOGS_FILE%' -Tail 5"
    pause
    exit /b 1
)

echo [+] Program basariyla tamamlandi.
timeout /t 3 >nul
exit /b 0
