# 🏗️ PinkNote Architecture

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         Browser                              │
│  ┌───────────┐  ┌──────────┐  ┌──────────┐  ┌───────────┐ │
│  │ Tailwind  │  │FullCalend│  │  Quill   │  │  PDF.js   │ │
│  │   CSS     │  │   ar     │  │  Editor  │  │  Viewer   │ │
│  └─────┬─────┘  └────┬─────┘  └────┬─────┘  └─────┬─────┘ │
│        │             │              │              │        │
│        └─────────────┴──────────────┴──────────────┘        │
│                           │                                  │
│                    ┌──────▼──────┐                          │
│                    │  face-api.js │                         │
│                    │  (Optional)  │                         │
│                    └──────────────┘                         │
└────────────────────────────┬────────────────────────────────┘
                             │
                    HTTP/HTTPS (AJAX + Forms)
                             │
┌────────────────────────────▼────────────────────────────────┐
│                      Django Server                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                     URL Router                        │  │
│  │  /login  /register  /dashboard  /api/diary/*  etc.  │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                      │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │                   Views Layer                         │  │
│  │  ┌──────────┐  ┌───────────┐  ┌──────────────────┐ │  │
│  │  │  Auth    │  │  Diary    │  │    Library       │ │  │
│  │  │  Views   │  │  Views    │  │    Views         │ │  │
│  │  └─────┬────┘  └─────┬─────┘  └────────┬─────────┘ │  │
│  └────────┼─────────────┼─────────────────┼───────────┘  │
│           │             │                 │                │
│  ┌────────▼─────────────▼─────────────────▼───────────┐  │
│  │                  Models Layer                        │  │
│  │  ┌──────────┐  ┌─────────────┐  ┌──────────────┐  │  │
│  │  │   User   │  │ DiaryEntry  │  │ LibraryItem  │  │  │
│  │  │  Model   │  │   Model     │  │    Model     │  │  │
│  │  └────┬─────┘  └──────┬──────┘  └──────┬───────┘  │  │
│  └───────┼────────────────┼─────────────────┼─────────┘  │
│          │                │                 │              │
│  ┌───────▼────────────────▼─────────────────▼─────────┐  │
│  │              Django ORM                             │  │
│  └───────────────────────┬─────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────┘
                           │
                ┌──────────▼──────────┐
                │   SQLite Database   │
                │   (or PostgreSQL)   │
                └─────────────────────┘

┌─────────────────────────────────────┐
│         File System                 │
│  ┌───────────────────────────────┐ │
│  │    media/library/YYYY/MM/     │ │
│  │    (PDF files storage)        │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

## Data Flow Diagrams

### 1. User Registration Flow

```
User → Register Page → Fill Form → [Enable Face?]
                                        │
                            ┌───────────┴────────────┐
                            │                        │
                          YES                       NO
                            │                        │
                    ┌───────▼────────┐              │
                    │ Camera Access  │              │
                    │ Face Capture   │              │
                    │ Store Encrypted│              │
                    └───────┬────────┘              │
                            │                        │
                            └───────────┬────────────┘
                                        │
                                Create User Account
                                        │
                                  Auto Login
                                        │
                                  Dashboard
```

### 2. Diary Entry Flow

```
Dashboard → Click Calendar Date → Entry Editor
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                   Existing Entry              New Entry
                          │                       │
                   Load Content                Empty Form
                          │                       │
                          └───────────┬───────────┘
                                      │
                              User Types Content
                                      │
                              Auto-save (2s delay)
                                      │
                          ┌───────────┴───────────┐
                          │                       │
                      Success                  Continue
                          │                       │
                    Show Status              More Typing
                          │                       │
                          │                       │
                    Manual Save Click              │
                          │                       │
                    Save to Database ◄────────────┘
                          │
                    Back to Dashboard
```

### 3. Library Upload & View Flow

```
Dashboard → Library Tab → Upload Button → Upload Modal
                                              │
                                    Fill Title, Genre
                                              │
                                    Select PDF File
                                              │
                                    Submit Form
                                              │
                                    ┌─────────▼─────────┐
                                    │ Server Validation │
                                    │  - PDF only?      │
                                    │  - File size OK?  │
                                    └─────────┬─────────┘
                                              │
                            ┌─────────────────┴─────────────────┐
                            │                                   │
                        Valid                              Invalid
                            │                                   │
                    Save to Filesystem                   Show Error
                            │                                   │
                    Create DB Record                      Stay Modal
                            │                                   │
                    Show in Library Grid                        │
                            │                                   │
                    User Clicks "View" ◄────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  PDF Modal     │
                    │  Load PDF.js   │
                    │  Render Page 1 │
                    └───────┬────────┘
                            │
                    Navigate Pages
```

### 4. Face Login Flow

```
Login Page → Face Login Tab → Enter Username
                                    │
                            Camera Access
                                    │
                            Click "Verify Face"
                                    │
                    ┌───────────────▼───────────────┐
                    │   Load face-api.js Models     │
                    │   - TinyFaceDetector          │
                    │   - FaceLandmark68Net         │
                    │   - FaceRecognitionNet        │
                    └───────────────┬───────────────┘
                                    │
                            Detect Face in Video
                                    │
                        Extract 128-point Descriptor
                                    │
                        Send to Server (API)
                                    │
                    ┌───────────────▼───────────────┐
                    │    Server Verification        │
                    │  - User exists?               │
                    │  - Has face data?             │
                    │  - Descriptors match?         │
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                Success                         Fail
                    │                               │
            Create Session                    Show Error
                    │                               │
            Redirect Dashboard               Try Again
```

## Component Architecture

### Frontend Components

```
┌────────────────────────────────────────────┐
│            base.html (Layout)              │
│  ┌──────────────────────────────────────┐ │
│  │         Navigation Bar               │ │
│  │  (Logo, Dashboard, Search, Profile)  │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │        Content Block                 │ │
│  │  {% block content %}                 │ │
│  │                                      │ │
│  │  ┌────────────────────────────────┐ │ │
│  │  │    Child Templates:            │ │ │
│  │  │  - register.html               │ │ │
│  │  │  - login.html                  │ │ │
│  │  │  - dashboard.html              │ │ │
│  │  │  - diary_entry.html            │ │ │
│  │  │  - profile.html                │ │ │
│  │  │  - search.html                 │ │ │
│  │  └────────────────────────────────┘ │ │
│  └──────────────────────────────────────┘ │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │         JavaScript Imports           │ │
│  │  - Tailwind Config                   │ │
│  │  - FullCalendar                      │ │
│  │  - Quill                             │ │
│  │  - PDF.js                            │ │
│  │  - face-api.js                       │ │
│  │  - Custom Scripts                    │ │
│  └──────────────────────────────────────┘ │
└────────────────────────────────────────────┘
```

### Backend Architecture

```
┌─────────────────────────────────────────────┐
│            Django Application               │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │         Authentication Layer          │ │
│  │  - User registration                  │ │
│  │  - Password login                     │ │
│  │  - Face login (API)                   │ │
│  │  - Session management                 │ │
│  │  - @login_required decorator          │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │          Business Logic               │ │
│  │                                       │ │
│  │  ┌─────────────────────────────────┐ │ │
│  │  │  Diary Management               │ │ │
│  │  │  - CRUD operations               │ │ │
│  │  │  - Date-based retrieval          │ │ │
│  │  │  - Auto-save handling            │ │ │
│  │  └─────────────────────────────────┘ │ │
│  │                                       │ │
│  │  ┌─────────────────────────────────┐ │ │
│  │  │  Library Management             │ │ │
│  │  │  - File upload & validation     │ │ │
│  │  │  - Genre organization            │ │ │
│  │  │  - Search & filter               │ │ │
│  │  └─────────────────────────────────┘ │ │
│  │                                       │ │
│  │  ┌─────────────────────────────────┐ │ │
│  │  │  Face Recognition               │ │ │
│  │  │  - Encryption/decryption        │ │ │
│  │  │  - Data storage                 │ │ │
│  │  │  - Verification                 │ │ │
│  │  └─────────────────────────────────┘ │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │         Data Access Layer             │ │
│  │  - Django ORM                         │ │
│  │  - Query optimization                 │ │
│  │  - User isolation                     │ │
│  └───────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────┐
│           Security Layers                   │
│                                             │
│  Layer 1: Authentication                    │
│  ┌───────────────────────────────────────┐ │
│  │  - Django session authentication      │ │
│  │  - Password hashing (PBKDF2)          │ │
│  │  - @login_required decorators         │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  Layer 2: Authorization                     │
│  ┌───────────────────────────────────────┐ │
│  │  - User-specific queries              │ │
│  │  - request.user filtering             │ │
│  │  - No cross-user access               │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  Layer 3: Data Protection                   │
│  ┌───────────────────────────────────────┐ │
│  │  - Face data encryption (Fernet)      │ │
│  │  - CSRF tokens on all forms           │ │
│  │  - Secure file storage                │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  Layer 4: Input Validation                  │
│  ┌───────────────────────────────────────┐ │
│  │  - File type validation (PDF only)    │ │
│  │  - Form validation                    │ │
│  │  - SQL injection prevention (ORM)     │ │
│  └───────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

## Database Schema

```
┌────────────────────────────────────────┐
│             core_user                  │
├────────────────────────────────────────┤
│ id (PK)                               │
│ username (UNIQUE)                     │
│ email                                 │
│ password (hashed)                     │
│ face_descriptor (encrypted, nullable) │
│ first_name                            │
│ last_name                             │
│ is_active                             │
│ is_staff                              │
│ date_joined                           │
└───────────┬────────────────────────────┘
            │
            │ 1:N
            │
┌───────────▼────────────────────────────┐
│          core_diaryentry               │
├────────────────────────────────────────┤
│ id (PK)                               │
│ user_id (FK) ─────────────────┐      │
│ title                          │      │
│ body (HTML)                    │      │
│ date (UNIQUE with user_id)     │      │
│ created_at                     │      │
│ updated_at                     │      │
└────────────────────────────────┘      │
                                        │
            ┌───────────────────────────┘
            │
            │ 1:N
            │
┌───────────▼────────────────────────────┐
│         core_libraryitem               │
├────────────────────────────────────────┤
│ id (PK)                               │
│ user_id (FK)                          │
│ title                                 │
│ genre (choices)                       │
│ file (FileField → media/library/)     │
│ uploaded_at                           │
└────────────────────────────────────────┘
```

## Deployment Architecture (Production)

```
┌─────────────────────────────────────────────┐
│              Load Balancer                  │
│              (Optional)                     │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│              Nginx / Apache                 │
│  - Serve static files                       │
│  - Serve media files                        │
│  - SSL termination                          │
│  - Reverse proxy to Django                  │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│              Gunicorn / uWSGI               │
│  - WSGI server                              │
│  - Multiple workers                         │
│  - Process management                       │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│           Django Application                │
│  - Business logic                           │
│  - Request handling                         │
│  - Response generation                      │
└───────────┬───────────────┬─────────────────┘
            │               │
            │               │
┌───────────▼─────┐  ┌──────▼──────────────┐
│   PostgreSQL    │  │   File System       │
│   Database      │  │   (or S3/CDN)       │
│   - User data   │  │   - PDFs            │
│   - Diary       │  │   - Static files    │
│   - Library     │  │                     │
└─────────────────┘  └─────────────────────┘
```

## API Request/Response Flow

### Example: Save Diary Entry

```
Client                    Server                   Database
  │                         │                         │
  │  POST /api/diary/save/  │                         │
  ├────────────────────────>│                         │
  │  {title, body, date}    │                         │
  │                         │  @login_required        │
  │                         │  Check user auth        │
  │                         │  Extract data           │
  │                         │  Validate               │
  │                         │  DiaryEntry.create()    │
  │                         ├────────────────────────>│
  │                         │                         │
  │                         │  Record saved           │
  │                         │<────────────────────────┤
  │                         │                         │
  │  {success: true, id: X} │                         │
  │<────────────────────────┤                         │
  │                         │                         │
  │  Update UI              │                         │
  │  Show success message   │                         │
  │                         │                         │
```

---

This architecture ensures:
- **Scalability**: Modular design allows easy expansion
- **Security**: Multiple layers of protection
- **Maintainability**: Clear separation of concerns
- **Performance**: Efficient data flow and caching strategies
- **User Experience**: Fast, responsive, intuitive interface
