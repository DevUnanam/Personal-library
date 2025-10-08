# 🚀 PinkNote Quick Start Guide

## Installation (Choose your method)

### Method 1: Automatic Setup (Recommended)

**Windows:**
```bash
setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Method 2: Manual Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start server:**
   ```bash
   python manage.py runserver
   ```

7. **Open browser:**
   Navigate to `http://127.0.0.1:8000`

## First Steps

1. **Register:** Create your account at the registration page
2. **Optional:** Enable face recognition during registration
3. **Dashboard:** You'll see two tabs - Diary and Library
4. **Diary:** Click on any calendar date to create your first entry
5. **Library:** Upload your first PDF book

## Features at a Glance

### 📔 Diary Features
- ✅ Rich text editor with formatting
- ✅ Auto-save every 2 seconds
- ✅ Interactive calendar view
- ✅ Click any date to create/edit entries
- ✅ Search through all entries

### 📚 Library Features
- ✅ Upload PDF books
- ✅ Organize by 8 genres
- ✅ Built-in PDF viewer
- ✅ Search and filter books
- ✅ Delete unwanted books

### 🔐 Security Features
- ✅ Password authentication
- ✅ Optional face recognition login
- ✅ Encrypted face data storage
- ✅ All data is private to your account
- ✅ Delete face data anytime

## Project Structure

```
pinknote/
├── 📁 config/              # Django settings
├── 📁 core/                # Main app
│   ├── 📄 models.py        # Database models
│   ├── 📄 views.py         # Views and APIs
│   ├── 📄 urls.py          # URL routing
│   └── 📁 templates/       # HTML templates
├── 📁 media/               # Uploaded files
├── 📄 manage.py            # Django management
├── 📄 requirements.txt     # Python packages
├── 📄 README.md            # Full documentation
└── 📄 QUICKSTART.md        # This file
```

## Default URLs

- **Home/Login:** `http://127.0.0.1:8000/`
- **Register:** `http://127.0.0.1:8000/register/`
- **Dashboard:** `http://127.0.0.1:8000/dashboard/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Search:** `http://127.0.0.1:8000/search/`
- **Profile:** `http://127.0.0.1:8000/profile/`

## Troubleshooting

### Camera not working for face recognition?
- Use Chrome or Firefox
- Allow camera permissions
- Use HTTPS or localhost only

### Migrations error?
```bash
python manage.py makemigrations core
python manage.py migrate
```

### Static files not loading?
```bash
python manage.py collectstatic
```

### Port already in use?
```bash
python manage.py runserver 8001
```

## Need Help?

- 📖 Read the full [README.md](README.md)
- 🐛 Check the Troubleshooting section in README
- 💻 Check Django logs in the console

---

**Enjoy your PinkNote experience! 🌸💖**
