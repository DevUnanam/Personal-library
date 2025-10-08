@echo off
echo 🌸 Setting up PinkNote...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create media directory
echo Creating media directory...
if not exist media\library mkdir media\library

REM Run migrations
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo ✅ Setup complete!
echo.
echo To create a superuser, run:
echo   python manage.py createsuperuser
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then open your browser and go to: http://127.0.0.1:8000
pause
