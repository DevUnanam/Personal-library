# 🧪 PinkNote Testing Guide

## Pre-Testing Setup

1. **Install and run the application:**
   ```bash
   # Run setup script
   ./setup.sh  # or setup.bat on Windows

   # Start server
   python manage.py runserver
   ```

2. **Open browser:**
   Navigate to `http://127.0.0.1:8000`

3. **Prepare test data:**
   - Have a PDF file ready (any PDF book)
   - Use a device with a camera for face recognition testing
   - Use Chrome or Firefox for best compatibility

---

## Feature Testing Checklist

### ✅ 1. User Registration (Standard)

**Test Case:** Register with username and password only

**Steps:**
1. Navigate to `/register/`
2. Enter username: `testuser`
3. Enter email: `test@example.com`
4. Enter password: `testpass123`
5. Leave "Enable Face Recognition" unchecked
6. Click "Create Account"

**Expected Result:**
- ✅ User is created
- ✅ Automatically logged in
- ✅ Redirected to dashboard
- ✅ Success message displayed

---

### ✅ 2. User Registration (With Face Recognition)

**Test Case:** Register with face enrollment

**Steps:**
1. Navigate to `/register/`
2. Fill in username, email, password
3. Check "Enable Face Recognition Login"
4. Allow camera access when prompted
5. Position face in camera view
6. Click "Capture Face"
7. Wait for "✓ Face captured successfully!" message
8. Click "Create Account"

**Expected Result:**
- ✅ Camera activates
- ✅ Face detection works
- ✅ Success message after capture
- ✅ User registered with face data
- ✅ Redirected to dashboard

**Edge Cases:**
- No face detected: Shows error message
- Camera denied: Shows permission error

---

### ✅ 3. Standard Login

**Test Case:** Login with username and password

**Steps:**
1. Logout if logged in
2. Navigate to `/login/`
3. Enter username: `testuser`
4. Enter password: `testpass123`
5. Click "Login"

**Expected Result:**
- ✅ Successfully logged in
- ✅ Redirected to dashboard
- ✅ Welcome message shows username

**Edge Cases:**
- Wrong password: Error message displayed
- Non-existent user: Error message displayed

---

### ✅ 4. Face Recognition Login

**Test Case:** Login using face verification

**Steps:**
1. Logout if logged in
2. Navigate to `/login/`
3. Click "Face Login" tab
4. Enter username: `testuser` (must have face data)
5. Allow camera access
6. Position face in view
7. Click "Verify Face"
8. Wait for verification

**Expected Result:**
- ✅ Camera activates
- ✅ Face detection runs
- ✅ Models load successfully
- ✅ Login successful if face matches
- ✅ Redirected to dashboard

**Edge Cases:**
- User has no face data: Login fails
- Face not detected: Error message
- Wrong user: Login fails

---

### ✅ 5. Dashboard Display

**Test Case:** View dashboard with both tabs

**Steps:**
1. Login successfully
2. View dashboard at `/dashboard/`
3. Check Diary tab (default)
4. Click Library tab

**Expected Result:**
- ✅ Navigation bar visible
- ✅ User name displayed in welcome message
- ✅ Two tabs visible (Diary, Library)
- ✅ Calendar rendered in Diary tab
- ✅ Library grid shown in Library tab
- ✅ Empty state if no data

---

### ✅ 6. Create Diary Entry (Calendar Click)

**Test Case:** Create entry by clicking calendar date

**Steps:**
1. On dashboard, Diary tab
2. Click any date on calendar
3. Redirected to entry editor
4. Date field auto-filled
5. Enter title: "My First Entry"
6. Enter content in Quill editor
7. Wait 2 seconds (auto-save)
8. Click "Save Entry"

**Expected Result:**
- ✅ Editor opens with correct date
- ✅ Auto-save triggers after typing
- ✅ "Saving..." message appears
- ✅ "✓ Auto-saved" confirmation
- ✅ Manual save successful
- ✅ Redirected to dashboard
- ✅ Entry appears on calendar

---

### ✅ 7. Create Diary Entry (New Entry Button)

**Test Case:** Create entry via new entry button

**Steps:**
1. Click "+ New Entry" on dashboard
2. Select date manually
3. Enter title and content
4. Save

**Expected Result:**
- ✅ Editor opens
- ✅ Can select any date
- ✅ Entry saves successfully
- ✅ Appears on calendar

---

### ✅ 8. Edit Existing Diary Entry

**Test Case:** Edit a previously created entry

**Steps:**
1. Click on existing entry in calendar
2. Editor opens with existing content
3. Modify title or content
4. Auto-save triggers
5. Click "Save Entry"

**Expected Result:**
- ✅ Existing data loads
- ✅ Quill editor shows formatted content
- ✅ Changes auto-save
- ✅ Manual save updates entry
- ✅ Updated entry visible on calendar

---

### ✅ 9. Delete Diary Entry

**Test Case:** Delete an entry

**Steps:**
1. Open existing entry in editor
2. Click "🗑️ Delete" button
3. Confirm deletion

**Expected Result:**
- ✅ Confirmation dialog appears
- ✅ Entry deleted from database
- ✅ Redirected to dashboard
- ✅ Entry removed from calendar

---

### ✅ 10. Rich Text Formatting

**Test Case:** Use Quill editor features

**Steps:**
1. Create or edit diary entry
2. Try each formatting option:
   - Bold, italic, underline
   - Headers (H1, H2, H3)
   - Lists (ordered, unordered)
   - Blockquote
   - Links
   - Colors

**Expected Result:**
- ✅ All formatting tools work
- ✅ Content styled in editor
- ✅ Formatting preserved on save
- ✅ Formatting visible when reopening

---

### ✅ 11. Upload PDF to Library

**Test Case:** Upload a book

**Steps:**
1. Switch to Library tab
2. Click "+ Upload PDF"
3. Fill in form:
   - Title: "Test Book"
   - Genre: "Comics"
   - Select PDF file
4. Click "Upload"

**Expected Result:**
- ✅ Modal opens
- ✅ Form fields present
- ✅ File upload works
- ✅ Upload successful message
- ✅ Book appears in library grid
- ✅ Modal closes

**Edge Cases:**
- Non-PDF file: Error message
- Empty fields: Validation error

---

### ✅ 12. View PDF in Browser

**Test Case:** Open PDF viewer

**Steps:**
1. In Library tab
2. Click "View" on any book
3. PDF modal opens
4. Use navigation:
   - Click "Next"
   - Click "Previous"
5. Click "Close"

**Expected Result:**
- ✅ Modal opens with PDF
- ✅ First page renders
- ✅ Page info shows (Page X of Y)
- ✅ Navigation buttons work
- ✅ Previous disabled on page 1
- ✅ Next disabled on last page
- ✅ Close button works

---

### ✅ 13. Search Library

**Test Case:** Search for books by title

**Steps:**
1. In Library tab
2. Enter search term in search box
3. Results filter automatically (debounced)

**Expected Result:**
- ✅ Search filters books in real-time
- ✅ Only matching titles shown
- ✅ Clear search shows all books
- ✅ "No books found" if no matches

---

### ✅ 14. Filter Library by Genre

**Test Case:** Filter books using genre dropdown

**Steps:**
1. In Library tab
2. Select "Horror" from genre filter
3. Select "All Genres"

**Expected Result:**
- ✅ Only Horror books shown
- ✅ All books shown when "All Genres" selected
- ✅ Combines with search filter

---

### ✅ 15. Delete Library Item

**Test Case:** Remove a book

**Steps:**
1. In Library tab
2. Click "Delete" on any book
3. Confirm deletion

**Expected Result:**
- ✅ Confirmation dialog appears
- ✅ Book removed from library
- ✅ File deleted from server
- ✅ Grid updates immediately

---

### ✅ 16. Global Search

**Test Case:** Search across diary and library

**Steps:**
1. Click "Search" in navigation
2. Enter search term
3. Submit search

**Expected Result:**
- ✅ Search page loads
- ✅ Results shown in two sections
- ✅ Diary entries matching title/content
- ✅ Library items matching title
- ✅ Click entry to view/edit
- ✅ Click book to view PDF

---

### ✅ 17. User Profile

**Test Case:** View profile and manage face data

**Steps:**
1. Click "Profile" in navigation
2. View account information
3. If face data exists, click "Remove Face Data"
4. Confirm deletion

**Expected Result:**
- ✅ Profile page shows username, email
- ✅ Face status displayed (enabled/disabled)
- ✅ Face data deletion works
- ✅ Page reloads after deletion
- ✅ Status updates

---

### ✅ 18. Logout

**Test Case:** Logout functionality

**Steps:**
1. While logged in, click "Logout"

**Expected Result:**
- ✅ Session cleared
- ✅ Redirected to login page
- ✅ Cannot access dashboard without login
- ✅ Direct URL access redirected to login

---

### ✅ 19. Calendar Interaction

**Test Case:** Calendar features

**Steps:**
1. On dashboard, Diary tab
2. Navigate months using arrow buttons
3. Switch to week view
4. Click "Today" button
5. Click on entries

**Expected Result:**
- ✅ Month navigation works
- ✅ Week view displays
- ✅ Today button returns to current date
- ✅ Entries clickable
- ✅ Proper date highlighting

---

### ✅ 20. Responsive Design

**Test Case:** Mobile/tablet view

**Steps:**
1. Open browser dev tools
2. Toggle device toolbar
3. Test on various sizes:
   - Mobile (375px)
   - Tablet (768px)
   - Desktop (1920px)

**Expected Result:**
- ✅ Layout adapts to screen size
- ✅ Navigation usable on mobile
- ✅ Calendar readable on small screens
- ✅ Forms usable on mobile
- ✅ Modals fit screen
- ✅ Text readable on all sizes

---

## Security Testing

### 🔒 Test 1: Authentication Required

**Steps:**
1. Logout
2. Try to access: `/dashboard/`, `/diary/new/`, `/profile/`

**Expected:** Redirected to login page

---

### 🔒 Test 2: CSRF Protection

**Steps:**
1. Try to submit form without CSRF token
2. Check browser dev tools for CSRF errors

**Expected:** Form submission fails without token

---

### 🔒 Test 3: User Data Isolation

**Steps:**
1. Create entries/books as User A
2. Logout and register User B
3. Check if User B can see User A's data

**Expected:** User B sees only their own data

---

### 🔒 Test 4: File Upload Validation

**Steps:**
1. Try to upload .exe, .jpg, .txt file as library item

**Expected:** Only PDF files accepted

---

## Performance Testing

### ⚡ Test 1: Page Load Time

**Steps:**
1. Use browser Network tab
2. Measure dashboard load time
3. Measure diary editor load time

**Target:** < 2 seconds on localhost

---

### ⚡ Test 2: Auto-save Performance

**Steps:**
1. Type rapidly in diary editor
2. Check if auto-save triggers correctly
3. Verify no duplicate saves

**Expected:** Debounced save after 2s idle

---

### ⚡ Test 3: Calendar with Many Entries

**Steps:**
1. Create 50+ diary entries
2. Load dashboard
3. Check calendar rendering

**Expected:** Calendar loads and displays all entries

---

### ⚡ Test 4: Library with Many Books

**Steps:**
1. Upload 20+ PDFs
2. Test search and filter
3. Check scroll performance

**Expected:** Smooth scrolling, fast filtering

---

## Browser Compatibility

Test on:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)

Features to verify:
- Face recognition (Chrome/Firefox best)
- PDF rendering
- Calendar display
- Rich text editor
- File uploads

---

## Error Handling

### Test Error Scenarios

1. **Network Error During Save**
   - Disconnect network
   - Try to save entry
   - Check error message

2. **Large File Upload**
   - Try uploading >10MB PDF
   - Check server response

3. **Invalid Date**
   - Try creating entry with past date
   - Verify handling

4. **Database Connection Error**
   - Stop database
   - Try operations
   - Check error pages

---

## Regression Testing Checklist

After any code changes, verify:
- [ ] Registration works
- [ ] Login works
- [ ] Diary CRUD works
- [ ] Library upload/view works
- [ ] Search works
- [ ] Auto-save works
- [ ] Face recognition works (if changed)
- [ ] No console errors
- [ ] No broken links
- [ ] Styling intact

---

## Test Data Cleanup

After testing:
```bash
# Delete test database
rm db.sqlite3

# Delete uploaded files
rm -rf media/library/*

# Run fresh migrations
python manage.py migrate

# Create new test user
python manage.py createsuperuser
```

---

## Automated Testing (Future)

Consider adding:
- Unit tests for models
- View tests
- API endpoint tests
- Integration tests
- Selenium for UI testing

Example:
```python
# tests/test_diary.py
from django.test import TestCase

class DiaryTestCase(TestCase):
    def test_create_entry(self):
        # Test diary entry creation
        pass
```

---

## Bug Report Template

If you find bugs, report with:
- **Title:** Short description
- **Steps to reproduce:** Detailed steps
- **Expected result:** What should happen
- **Actual result:** What actually happens
- **Browser:** Chrome 120, etc.
- **Console errors:** Any JavaScript errors
- **Screenshots:** If applicable

---

## Testing Completion

✅ All features tested
✅ Security verified
✅ Performance acceptable
✅ Errors handled gracefully
✅ Mobile responsive
✅ Cross-browser compatible

**Application is ready for use! 🌸**
