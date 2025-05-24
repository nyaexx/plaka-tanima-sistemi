@echo off
chcp 65001 > nul
color 0B

:: Hata log dosyası için tarih-saat
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set LOGS_FILE=hata_%datetime:~0,8%_%datetime:~8,6%.txt

:: BURAYA ARAYUZ KLASORUNUN TAM YOLUNU GIRIN
set "ARAYUZ_DIZINI=C:\Users\PC\Desktop\plaka-tanima-sistemi-main\arayuzv1"

:: Log fonksiyonu
:LogHata
echo %date% %time% - %~1 >> %LOGS_FILE%
echo [HATA] %~1
goto :eof

cls
echo ===============================================
echo            PLAKA TANIMA SISTEMI
echo ===============================================
echo.

:: Python surumu kontrolu (minimum 3.8)
python --version > temp.txt 2>&1
set /p PYTHON_VERSION=<temp.txt
del temp.txt
echo %PYTHON_VERSION% | findstr "Python 3.[89]" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    color 0C
    call :LogHata "Python 3.8 veya ustu gerekli. Mevcut surum: %PYTHON_VERSION%"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    pause
    exit /b 1
)

:: Yol kontrolu ve gecis
if not exist "%ARAYUZ_DIZINI%" (
    color 0C
    call :LogHata "Arayuz klasoru bulunamadi: %ARAYUZ_DIZINI%"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    echo Lutfen baslat.bat icindeki ARAYUZ_DIZINI yolunu kontrol edin.
    pause
    exit /b 1
)

:: Dizine gecis ve dogrulama
pushd "%ARAYUZ_DIZINI%" 2>nul
if %ERRORLEVEL% neq 0 (
    color 0C
    call :LogHata "Dizine erisim hatasi: %ARAYUZ_DIZINI%"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    pause
    exit /b 1
)

:: Arayuz dosyasi kontrolu
if not exist "main.py" (
    color 0C
    call :LogHata "main.py dosyasi bulunamadi: %ARAYUZ_DIZINI%\main.py"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
    popd
    pause
    exit /b 1
)

:: Arayuz baslatma
color 0A
echo [*] Arayuz baslatiliyor...
start "" python main.py 2>>%LOGS_FILE%

if %ERRORLEVEL% equ 0 (
    echo [+] Arayuz basariyla baslatildi!
    echo [i] Programi kapatmak icin arayuz penceresini kapatabilirsiniz.
) else (
    color 0C
    call :LogHata "Arayuz baslatilirken hata olustu!"
    echo Hata detaylari %LOGS_FILE% dosyasina kaydedildi.
)

popd
pause

