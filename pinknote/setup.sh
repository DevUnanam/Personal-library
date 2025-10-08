#!/bin/bash

echo "🌸 Setting up PinkNote..."

# Create virtual environment
echo "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create media directory
echo "Creating media directory..."
mkdir -p media/library

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "✅ Setup complete!"
echo ""
echo "To create a superuser, run:"
echo "  python manage.py createsuperuser"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then open your browser and go to: http://127.0.0.1:8000"
