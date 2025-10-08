# 🔧 PinkNote - Troubleshooting Guide

## Common Issues and Solutions

### Issue: "Dependency on app with no migrations: core"

This error appears when Django's auto-reloader encounters cached migration files.

#### Solution 1: Clear Cache and Restart (Recommended)
```bash
# Clear all Python cache
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null

# Run migrations
python manage.py migrate --run-syncdb

# Start server
python manage.py runserver
```

#### Solution 2: Use the Run Scripts
We've created helper scripts that automatically clear cache:

**Windows:**
```bash
run_server.bat
```

**Linux/Mac:**
```bash
chmod +x run_server.sh
./run_server.sh
```

#### Solution 3: Disable Auto-reloader
If the issue persists, run the server without auto-reload:
```bash
python manage.py runserver --noreload
```

**Note:** With `--noreload`, you'll need to manually restart the server after code changes.

---

### Issue: "Port already in use"

#### Solution: Use a Different Port
```bash
python manage.py runserver 8001
```

Then access: http://127.0.0.1:8001

---

### Issue: Migration Errors

#### Solution 1: Reset Migrations
```bash
# Backup your database first!
cp db.sqlite3 db.sqlite3.backup

# Delete migration files (keep __init__.py)
rm core/migrations/0001_initial.py

# Recreate migrations
python manage.py makemigrations
python manage.py migrate

# Recreate test user
python create_test_user.py
```

#### Solution 2: Fresh Start
```bash
# Delete database
rm db.sqlite3

# Delete migration cache
rm -rf core/migrations/__pycache__

# Recreate everything
python manage.py makemigrations
python manage.py migrate
python create_test_user.py
```

---

### Issue: "Module not found" Errors

#### Solution: Check Virtual Environment
```bash
# Ensure you're in the virtual environment
# You should see (venv) in your prompt

# If not, activate it:
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt
```

---

### Issue: Static Files Not Loading

#### Solution 1: Development Mode
Django serves static files automatically in development when DEBUG=True.

Verify in `config/settings.py`:
```python
DEBUG = True
```

#### Solution 2: Collect Static Files (Production)
```bash
python manage.py collectstatic
```

---

### Issue: Face Recognition Not Working

#### Common Causes:
1. **Browser Compatibility**
   - Use Chrome or Firefox
   - Safari has limited support

2. **Permissions**
   - Allow camera access when prompted
   - Check browser permissions in settings

3. **HTTPS Requirement**
   - Camera requires HTTPS or localhost
   - localhost should work automatically

4. **Model Loading**
   - Face-api.js models load from CDN
   - Check internet connection
   - Check browser console for errors

#### Solution:
```javascript
// Check browser console (F12) for errors
// Models should load from:
https://cdn.jsdelivr.net/npm/@vladmandic/face-api@1.7.12/model
```

---

### Issue: PDF Upload Fails

#### Common Causes:
1. **File Type** - Only PDF files are allowed
2. **File Size** - Very large files may timeout
3. **Permissions** - media/ directory must be writable

#### Solution:
```bash
# Ensure media directory exists and is writable
mkdir -p media/library
chmod 755 media/library  # Linux/Mac only

# Check file type
# Only files ending in .pdf are allowed
```

---

### Issue: Auto-save Not Working

#### Check:
1. Open browser console (F12)
2. Look for JavaScript errors
3. Check network tab for failed requests

#### Common Causes:
- CSRF token missing
- Network connectivity issues
- JavaScript errors

#### Solution:
Clear browser cache and reload:
```
Ctrl + Shift + R (Windows/Linux)
Cmd + Shift + R (Mac)
```

---

### Issue: Calendar Not Displaying

#### Solution 1: Check Browser Console
```
F12 → Console tab
Look for JavaScript errors
```

#### Solution 2: Clear CDN Cache
FullCalendar loads from CDN. Check internet connection.

#### Solution 3: Verify Template
Ensure base.html includes FullCalendar:
```html
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.9/index.global.min.js'></script>
```

---

### Issue: Quill Editor Not Working

#### Solution:
Same as calendar - check CDN connectivity and browser console.

Quill CDN:
```html
<link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
<script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
```

---

### Issue: Login Fails

#### Check:
1. **Correct Credentials**
   - Test user: `testuser` / `test123`

2. **User Exists**
   ```bash
   python create_test_user.py
   ```

3. **Database Migrated**
   ```bash
   python manage.py migrate
   ```

---

### Issue: Server Starts But Can't Access

#### Solution 1: Check Firewall
```bash
# Ensure port 8000 is not blocked
# Try accessing: http://127.0.0.1:8000
# Also try: http://localhost:8000
```

#### Solution 2: Check Server Output
```bash
# Server should show:
Starting development server at http://127.0.0.1:8000/
```

---

### Issue: CSS Not Loading (Tailwind)

#### Solution:
Tailwind loads from CDN. Check in base.html:
```html
<script src="https://cdn.tailwindcss.com"></script>
```

Check browser console for CDN errors.

---

## Advanced Troubleshooting

### Check Django Configuration
```bash
python manage.py check
```

### Check Database
```bash
# Open Django shell
python manage.py shell

# Check user count
>>> from core.models import User
>>> User.objects.count()
```

### View Server Logs
The terminal running `python manage.py runserver` shows all logs.

Look for:
- 404 errors (page not found)
- 500 errors (server error)
- Migration warnings

---

## Complete Reset (Nuclear Option)

If nothing works, start completely fresh:

```bash
# 1. Backup your data
cp db.sqlite3 db.sqlite3.backup
cp -r media media.backup

# 2. Delete everything except source code
rm db.sqlite3
rm -rf core/migrations/0001_initial.py
rm -rf core/migrations/__pycache__
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# 3. Recreate from scratch
python manage.py makemigrations
python manage.py migrate
python create_test_user.py

# 4. Start server
python manage.py runserver
```

---

## Getting Help

### Check These First:
1. ✅ Python 3.8+ installed
2. ✅ Virtual environment activated
3. ✅ Requirements installed
4. ✅ Migrations applied
5. ✅ No syntax errors

### Debug Checklist:
- [ ] Browser console clear of errors (F12)
- [ ] Server terminal shows no errors
- [ ] Database exists (db.sqlite3)
- [ ] Migrations applied (python manage.py showmigrations)
- [ ] Test user exists
- [ ] Port 8000 not in use

### Documentation:
- [QUICKSTART.md](QUICKSTART.md) - Setup guide
- [README.md](README.md) - Full documentation
- [INSTALLATION_VERIFIED.md](INSTALLATION_VERIFIED.md) - Verification steps

---

## Specific Error Messages

### "No module named 'core'"
```bash
# Check you're in the right directory
pwd
# Should show: .../pinknote

# Check core app exists
ls core/
# Should show: models.py, views.py, etc.
```

### "CSRF verification failed"
```bash
# Clear cookies for localhost
# In browser: F12 → Application → Cookies → Delete All
```

### "Table doesn't exist"
```bash
# Run migrations
python manage.py migrate
```

### "Permission denied" (Linux/Mac)
```bash
# Fix permissions
chmod +x setup.sh
chmod +x run_server.sh
chmod -R 755 media/
```

---

## Prevention Tips

### Always:
1. ✅ Activate virtual environment before running commands
2. ✅ Run `python manage.py check` before starting server
3. ✅ Keep browser console open during development (F12)
4. ✅ Clear cache when making template changes
5. ✅ Backup database before major changes

### Never:
1. ❌ Delete __init__.py files in migrations/
2. ❌ Edit migration files manually
3. ❌ Commit db.sqlite3 to git
4. ❌ Run as root/administrator
5. ❌ Use DEBUG=True in production

---

## Quick Reference Commands

### Server Management
```bash
# Start server
python manage.py runserver

# Start on different port
python manage.py runserver 8001

# Start without auto-reload
python manage.py runserver --noreload
```

### Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Django shell
python manage.py shell
```

### User Management
```bash
# Create test user
python create_test_user.py

# Create superuser
python manage.py createsuperuser
```

### Maintenance
```bash
# Check for issues
python manage.py check

# Clear cache (Linux/Mac)
find . -type d -name __pycache__ -exec rm -rf {} +

# Clear cache (Windows)
for /d /r . %d in (__pycache__) do @if exist "%d" rd /s /q "%d"
```

---

## Still Having Issues?

1. Check all documentation files
2. Review browser console (F12)
3. Check server terminal output
4. Try the "Complete Reset" procedure above
5. Verify Python version: `python --version` (need 3.8+)

---

**Most issues are resolved by clearing cache and restarting the server!**

Use the helper scripts:
- `run_server.bat` (Windows)
- `run_server.sh` (Linux/Mac)
