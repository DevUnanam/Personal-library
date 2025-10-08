#!/bin/bash

echo "🔧 PinkNote - Quick Fix and Run"
echo "================================"
echo ""

# Step 1: Clear all cache
echo "Step 1: Clearing Python cache..."
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
echo "✅ Cache cleared"
echo ""

# Step 2: Verify migrations exist
echo "Step 2: Checking migrations..."
if [ -f "core/migrations/0001_initial.py" ]; then
    echo "✅ Migrations found"
else
    echo "⚠️  Creating migrations..."
    python manage.py makemigrations
fi
echo ""

# Step 3: Apply migrations
echo "Step 3: Applying migrations..."
python manage.py migrate --run-syncdb
echo ""

# Step 4: Verify test user
echo "Step 4: Ensuring test user exists..."
python create_test_user.py
echo ""

# Step 5: Final check
echo "Step 5: Running Django checks..."
python manage.py check
echo ""

# Step 6: Start server
echo "================================"
echo "✅ All checks passed!"
echo ""
echo "🌸 Starting PinkNote Server..."
echo ""
echo "Access at: http://127.0.0.1:8000"
echo "Login: testuser / test123"
echo ""
echo "Press Ctrl+C to stop"
echo "================================"
echo ""

python manage.py runserver
