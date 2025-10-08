# 🌸 PinkNote - Personal Diary & Library

A beautiful pink and violet themed personal diary and library application with optional face recognition login.

## ✨ Features

### 📔 Diary
- Create, edit, and delete diary entries
- Interactive calendar view (FullCalendar)
- Rich text editor with formatting (Quill)
- Auto-save functionality
- Click on any calendar date to create/view entries
- Search through diary entries

### 📚 Library
- Upload and manage PDF books
- Organize by genre (Horror, Comedy, Comics, Romance, Fantasy, Mystery, Sci-Fi, Other)
- Built-in PDF viewer with page navigation
- Search and filter books by title and genre
- Secure file storage

### 🔐 Authentication
- Standard username/password login
- Optional face recognition login (face-api.js)
- Single user system (no multi-user admin needed)
- Encrypted face data storage
- Delete face recognition data anytime

### 🎨 Design
- Pink and violet Barbie/Disney princess theme
- Tailwind CSS for responsive design
- Soft gradients and rounded corners
- Mobile-friendly interface
- Beautiful UI with smooth animations

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Modern web browser with camera support (for face recognition)

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd pinknote
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000`
   - Register a new account to get started

## 📁 Project Structure

```
pinknote/
├── config/                 # Django project settings
│   ├── settings.py        # Main settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py
├── core/                   # Main application
│   ├── models.py          # User, DiaryEntry, LibraryItem models
│   ├── views.py           # All view functions and API endpoints
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin configuration
│   ├── templates/         # HTML templates
│   │   └── core/
│   │       ├── base.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── diary_entry.html
│   │       ├── profile.html
│   │       └── search.html
│   └── static/            # Static files (CSS, JS)
├── media/                 # User uploads (PDFs)
├── manage.py
├── requirements.txt
└── README.md
```

## 🔧 Configuration

### Face Recognition Encryption Key
The face data is encrypted using Fernet encryption. To use a custom encryption key in production:

1. Generate a new key:
   ```python
   from cryptography.fernet import Fernet
   print(Fernet.generate_key().decode())
   ```

2. Set the environment variable:
   ```bash
   export FACE_ENCRYPTION_KEY="your-generated-key"
   ```

### Media Files
Media files (uploaded PDFs) are stored in the `media/library/` directory. Make sure this directory has proper permissions.

## 🎯 Usage

### Creating Diary Entries
1. Log in to your account
2. Click on the "Diary" tab on the dashboard
3. Click on any date in the calendar to create an entry for that day
4. Write your entry using the rich text editor
5. Entries are auto-saved every 2 seconds
6. Click "Save Entry" to finalize

### Managing Library
1. Click on the "Library" tab on the dashboard
2. Click "+ Upload PDF" to add a new book
3. Fill in the title, select a genre, and choose your PDF file
4. Click "Upload" to add it to your library
5. Use the search bar or genre filter to find books
6. Click "View" to read a book in the built-in PDF viewer
7. Click "Delete" to remove a book

### Face Recognition Login
1. During registration, check "Enable Face Recognition Login"
2. Allow camera access when prompted
3. Position your face in the camera view
4. Click "Capture Face" to enroll your face
5. On future logins, click "Face Login" tab
6. Enter your username and click "Verify Face"
7. Your face will be verified for login

### Search
- Use the search page to find diary entries and books
- Search works across diary titles, content, and book titles

## 🔒 Security Notes

- Face data is encrypted using Fernet encryption
- All uploaded files are restricted to the logged-in user
- CSRF protection is enabled for all forms
- Change the `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Use HTTPS in production
- Implement proper database backups

## 🎨 Customization

### Theme Colors
The theme uses these primary colors:
- Pink Main: `#ff6fb5`
- Violet Main: `#8a4fff`
- Pink Light: `#ffd1e8`

To change colors, edit the Tailwind config in `templates/core/base.html`.

### Database
The project uses SQLite by default. For production, consider using PostgreSQL:

```python
# In config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pinknote',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📝 API Endpoints

### Authentication
- `POST /register/` - Register new user
- `POST /login/` - Login with username/password
- `POST /api/face-login/` - Login with face recognition
- `GET /logout/` - Logout user

### Diary
- `GET /api/diary/list/` - Get all diary entries (for calendar)
- `GET /api/diary/by-date/?date=YYYY-MM-DD` - Get entry by date
- `POST /api/diary/save/` - Create or update entry
- `POST /api/diary/delete/<id>/` - Delete entry
- `GET /diary/<id>/` - View/edit entry page
- `GET /diary/new/` - Create new entry page

### Library
- `GET /api/library/list/?q=search&genre=genre` - Get library items
- `POST /api/library/upload/` - Upload PDF
- `POST /api/library/delete/<id>/` - Delete library item

### Profile
- `GET /profile/` - View profile
- `POST /api/profile/delete-face/` - Remove face data

### Search
- `GET /search/?q=query` - Search diary and library

## 🐛 Troubleshooting

### Face recognition not working
- Ensure you're using HTTPS or localhost
- Grant camera permissions in your browser
- Check browser console for errors
- Face-api.js models must load correctly

### PDF uploads failing
- Check file size limits in your web server configuration
- Ensure the `media/` directory exists and is writable
- Verify PDF file is not corrupted

### Calendar not displaying
- Check browser console for JavaScript errors
- Ensure FullCalendar CDN is accessible
- Verify diary entries are being returned by the API

## 📄 License

This project is open source and available for personal use.

## 🙏 Credits

- **Django** - Web framework
- **Tailwind CSS** - Styling
- **FullCalendar** - Calendar component
- **Quill** - Rich text editor
- **PDF.js** - PDF viewer
- **face-api.js** - Face recognition
- **Cryptography** - Encryption library

## 💡 Future Enhancements

- Export diary entries to PDF
- Dark mode toggle
- Backup and restore functionality
- Tags for diary entries
- Reading progress tracker for books
- Mobile app (React Native/Flutter)
- Cloud storage integration
- Multiple language support

---

Made with 💖 for personal journaling and reading
