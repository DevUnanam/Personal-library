#!/bin/bash

echo "🌸 Starting PinkNote Server..."
echo ""

# Clear Python cache
echo "Clearing cache..."
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Ensure migrations are applied
echo "Checking migrations..."
python manage.py migrate --run-syncdb

echo ""
echo "✅ Starting server on http://127.0.0.1:8000"
echo ""
echo "Login credentials:"
echo "  Username: testuser"
echo "  Password: test123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start server
python manage.py runserver
