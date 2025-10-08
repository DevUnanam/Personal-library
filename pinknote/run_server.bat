@echo off
echo 🌸 Starting PinkNote Server...
echo.

REM Clear Python cache
echo Clearing cache...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
del /s /q *.pyc 2>nul

REM Ensure migrations are applied
echo Checking migrations...
python manage.py migrate --run-syncdb

echo.
echo ✅ Starting server on http://127.0.0.1:8000
echo.
echo Login credentials:
echo   Username: testuser
echo   Password: test123
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start server
python manage.py runserver
