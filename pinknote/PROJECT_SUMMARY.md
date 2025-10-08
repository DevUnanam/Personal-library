# 🌸 PinkNote - Project Summary

## Overview
PinkNote is a full-featured Django web application combining a personal diary with a PDF library manager, featuring optional face recognition authentication. The app uses a beautiful pink and violet theme inspired by Barbie/Disney princess aesthetics.

## ✅ Completed Features

### 1. Authentication System
- ✅ User registration with username, email, and password
- ✅ Standard login with username/password
- ✅ Face recognition login using face-api.js
- ✅ Encrypted storage of face descriptors
- ✅ Option to delete face data
- ✅ Login required for all diary and library features

### 2. Diary System
- ✅ Create, edit, and delete diary entries
- ✅ Rich text editor (Quill) with formatting options
- ✅ Interactive calendar (FullCalendar) showing all entries
- ✅ Click calendar dates to create/edit entries for that day
- ✅ Auto-save functionality (every 2 seconds)
- ✅ One entry per date per user
- ✅ View past entries
- ✅ Search through diary content

### 3. Library System
- ✅ Upload PDF books
- ✅ Organize by 8 genres (Horror, Comedy, Comics, Romance, Fantasy, Mystery, Sci-Fi, Other)
- ✅ Built-in PDF viewer with page navigation (PDF.js)
- ✅ Search books by title
- ✅ Filter by genre
- ✅ Delete books
- ✅ Secure file storage per user

### 4. User Interface
- ✅ Pink and violet gradient theme (#ff6fb5, #8a4fff, #ffd1e8)
- ✅ Tailwind CSS integration
- ✅ Responsive mobile design
- ✅ Smooth animations and transitions
- ✅ Rounded corners and soft shadows
- ✅ Tab-based dashboard interface
- ✅ Modal windows for uploads and PDF preview
- ✅ Clean navigation bar

### 5. Security Features
- ✅ Password-protected access
- ✅ User-specific data isolation
- ✅ Encrypted face recognition data (Fernet encryption)
- ✅ CSRF protection
- ✅ Secure file uploads (PDF only)
- ✅ Django authentication system

## 📁 Project Structure

```
pinknote/
├── config/                          # Django project configuration
│   ├── __init__.py
│   ├── settings.py                 # Main settings with custom user model
│   ├── urls.py                     # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── core/                            # Main application
│   ├── models.py                   # User, DiaryEntry, LibraryItem models
│   ├── views.py                    # All views and API endpoints
│   ├── urls.py                     # App URL patterns
│   ├── admin.py                    # Django admin configuration
│   ├── apps.py
│   ├── tests.py
│   ├── __init__.py
│   │
│   ├── templates/core/             # HTML templates
│   │   ├── base.html              # Base template with Tailwind, libraries
│   │   ├── register.html          # Registration with face enrollment
│   │   ├── login.html             # Login (password + face options)
│   │   ├── dashboard.html         # Main dashboard (diary + library tabs)
│   │   ├── diary_entry.html       # Diary entry editor with Quill
│   │   ├── profile.html           # User profile and settings
│   │   └── search.html            # Search results page
│   │
│   ├── static/                     # Static files (CSS, JS)
│   │   ├── css/
│   │   └── js/
│   │
│   └── migrations/                 # Database migrations
│       └── __init__.py
│
├── media/                           # User uploads
│   └── library/                    # PDF storage (organized by year/month)
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── README.md                        # Full documentation
├── QUICKSTART.md                    # Quick start guide
├── PROJECT_SUMMARY.md              # This file
├── .gitignore                      # Git ignore rules
├── .env.example                    # Environment variables template
├── setup.sh                        # Linux/Mac setup script
└── setup.bat                       # Windows setup script
```

## 🔧 Technology Stack

### Backend
- **Django 4.2.7** - Web framework
- **SQLite** - Database (default, can use PostgreSQL)
- **Cryptography** - Face data encryption
- **Pillow** - Image processing

### Frontend
- **Tailwind CSS** - Styling framework
- **FullCalendar 6.1.9** - Interactive calendar
- **Quill 1.3.6** - Rich text editor
- **PDF.js 3.11.174** - PDF viewer
- **face-api.js 1.7.12** - Face recognition
- **Vanilla JavaScript** - Frontend logic

## 📊 Database Models

### User Model
```python
- username (CharField)
- email (EmailField)
- password (CharField, hashed)
- face_descriptor (BinaryField, encrypted, nullable)
+ set_face_data()
+ get_face_data()
+ delete_face_data()
```

### DiaryEntry Model
```python
- user (ForeignKey to User)
- title (CharField, max 200)
- body (TextField, HTML content)
- date (DateField, unique per user)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### LibraryItem Model
```python
- user (ForeignKey to User)
- title (CharField, max 200)
- genre (CharField, choices)
- file (FileField, PDF)
- uploaded_at (DateTimeField)
```

## 🌐 API Endpoints

### Authentication
- `GET/POST /register/` - User registration
- `GET/POST /login/` - Password login
- `POST /api/face-login/` - Face recognition login
- `GET /logout/` - Logout

### Diary
- `GET /dashboard/` - Main dashboard
- `GET /diary/new/` - New entry form
- `GET /diary/<id>/` - View/edit entry
- `GET /api/diary/list/` - List entries (JSON)
- `GET /api/diary/by-date/?date=YYYY-MM-DD` - Get entry by date
- `POST /api/diary/save/` - Create/update entry
- `POST /api/diary/delete/<id>/` - Delete entry

### Library
- `GET /api/library/list/?q=&genre=` - List books with search/filter
- `POST /api/library/upload/` - Upload PDF
- `POST /api/library/delete/<id>/` - Delete book

### User
- `GET /profile/` - User profile page
- `POST /api/profile/delete-face/` - Remove face data

### Search
- `GET /search/?q=` - Search diary and library

## 🎨 Theme Customization

### Colors
```css
Primary Pink: #ff6fb5
Primary Violet: #8a4fff
Light Pink: #ffd1e8
Background Gradient: linear-gradient(135deg, #ffedf5, #f3e8ff)
```

### Fonts
- Primary: Segoe UI, Roboto
- Headings: Bold, gradient text effect
- Body: Regular weight

## 🔐 Security Considerations

1. **Face Data Encryption**
   - Uses Fernet symmetric encryption
   - Key stored in settings (should be in env variable for production)
   - Data stored as binary in database

2. **File Upload Security**
   - Only PDF files allowed
   - User-specific file paths
   - Files served through Django in development

3. **Authentication**
   - Django's built-in authentication system
   - Password hashing (PBKDF2)
   - CSRF protection on all forms

4. **Production Checklist**
   - [ ] Set DEBUG=False
   - [ ] Change SECRET_KEY
   - [ ] Use environment variables for sensitive data
   - [ ] Set up proper media file serving (nginx/apache)
   - [ ] Use HTTPS
   - [ ] Configure ALLOWED_HOSTS
   - [ ] Set up database backups
   - [ ] Use PostgreSQL instead of SQLite

## 📝 Usage Flow

### New User Journey
1. Visit site → redirected to login
2. Click "Register" → registration form
3. Optionally enable face recognition
4. Dashboard appears with empty diary and library
5. Click calendar date → create first diary entry
6. Click "Library" tab → upload first book

### Returning User Journey
1. Visit site → login page
2. Choose password or face login
3. Dashboard shows existing entries and books
4. Calendar displays all diary entries
5. Click date/entry to view/edit
6. Browse library, view PDFs

## 🎯 Key Features Explanation

### Auto-save
- Triggers 2 seconds after user stops typing
- Saves to same entry if exists
- Shows "Saving..." and "✓ Auto-saved" status
- No data loss on accidental navigation

### Calendar Integration
- FullCalendar displays entries as events
- Click date to create entry for that day
- Click entry to edit
- Color-coded events with pink/violet theme

### Face Recognition
- Captures 128-point face descriptor
- Stored encrypted in database
- Compared on login (simplified implementation)
- Can be deleted anytime from profile

### PDF Viewer
- Modal overlay with PDF.js
- Page-by-page navigation
- Responsive canvas rendering
- Zoom support (1.5x scale)

## 🚀 Deployment Guide

### Local Development
```bash
python manage.py runserver
```

### Production (Basic)
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# Set up nginx as reverse proxy
# Configure static/media file serving
# Set up SSL certificate
```

## 📈 Future Enhancement Ideas

### Short Term
- [ ] Export diary entries to PDF
- [ ] Bulk delete for library
- [ ] Tags for diary entries
- [ ] Favorites/bookmarks in library
- [ ] Reading progress tracker

### Medium Term
- [ ] Dark mode toggle
- [ ] Multiple diary books/categories
- [ ] Library statistics dashboard
- [ ] Backup/restore functionality
- [ ] Email notifications

### Long Term
- [ ] Mobile app (React Native/Flutter)
- [ ] Cloud storage integration (S3, Dropbox)
- [ ] Multi-language support
- [ ] Social features (private sharing)
- [ ] AI-powered search and insights
- [ ] Voice notes for diary
- [ ] OCR for scanned documents

## 🐛 Known Limitations

1. **Face Recognition**
   - Simplified implementation
   - Real production app needs sophisticated matching
   - Requires good lighting conditions
   - Works best in Chrome/Firefox

2. **Single User System**
   - Designed for personal use
   - No multi-user admin panel
   - No user permissions/roles

3. **File Storage**
   - Uses local filesystem
   - No cloud backup
   - May need cleanup for large libraries

4. **Performance**
   - SQLite suitable for single user only
   - PDF rendering can be slow for large files
   - Calendar loads all entries at once

## 📞 Support & Maintenance

### Regular Maintenance
- Keep Django and dependencies updated
- Regular database backups
- Monitor media storage size
- Check error logs
- Test face recognition periodically

### Troubleshooting Resources
- Check Django error messages
- Browser console for JS errors
- Network tab for API failures
- Django debug toolbar (development)

## ✨ Conclusion

PinkNote is a fully functional, beautifully designed personal diary and library application. It successfully combines:
- Modern web technologies (Django, Tailwind, modern JS libraries)
- Innovative features (face recognition, auto-save, PDF viewer)
- Beautiful, cohesive design (pink/violet theme)
- Secure, user-friendly experience

The codebase is well-organized, documented, and ready for both personal use and further development.

---

**Built with 💖 for personal journaling and reading**
