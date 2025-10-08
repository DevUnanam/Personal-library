# 📔 Multiple Entries Per Day - Update Documentation

## ✨ What Changed

PinkNote has been updated to allow **multiple diary entries per day**!

Previously, you could only have one entry per date. Now you can create as many entries as you want for any single day.

---

## 🎯 New Features

### 1. Multiple Entries Per Day
- Create unlimited entries for the same date
- Each entry is timestamped individually
- Entries are sorted by creation time (newest first)

### 2. Entries Modal
When you click a date on the calendar, you'll see:
- A modal showing **all entries** for that day
- Preview of each entry (first 200 characters)
- Edit and Delete buttons for each entry
- "Add Another Entry" button to create more entries

### 3. Better Organization
- Entries are ordered by creation time
- Each entry shows when it was created
- Easy navigation between entries

---

## 🔧 Technical Changes

### Database Model
**Changed:**
```python
# BEFORE (only 1 entry per day)
class Meta:
    unique_together = ['user', 'date']

# AFTER (unlimited entries per day)
class Meta:
    ordering = ['-date', '-created_at']
```

### API Changes
**Updated endpoint:** `/api/diary/by-date/?date=YYYY-MM-DD`

**Before:** Returned single entry
```json
{
    "success": true,
    "entry": { ... }
}
```

**After:** Returns array of entries
```json
{
    "success": true,
    "entries": [ ... ],
    "count": 2
}
```

### UI Changes
1. **New Modal:** Entries list modal on dashboard
2. **Calendar Behavior:**
   - Clicking a date shows entries modal (not direct to editor)
   - Clicking an event shows entries modal
   - Modal has "Add Another Entry" button
3. **Entry Management:** View, edit, and delete from modal

---

## 📖 How to Use

### Creating Multiple Entries

**Method 1: From Dashboard**
1. Click on any date in the calendar
2. Entries modal opens
3. Click "Add Another Entry for This Day"
4. Create your entry
5. Return to dashboard
6. Click the same date again to add more

**Method 2: Direct Link**
1. Go to "New Entry" from dashboard
2. Select date
3. Create entry
4. Click "Back to Dashboard"
5. Click "+ New Entry" again for same date

### Viewing Multiple Entries

1. Click any date on the calendar
2. Modal shows all entries for that day
3. See entry titles, previews, and timestamps
4. Click "Edit" to modify any entry
5. Click "Delete" to remove any entry

### Calendar Display

- Calendar shows events for days with entries
- Multiple entries per day still show as one event
- Click the event or date to see all entries

---

## 🎨 New UI Components

### Entries Modal
```
┌─────────────────────────────────────┐
│ Entries for Monday, October 7, 2024 │
│                                     │
│  ┌────────────────────────────────┐│
│  │ Morning Thoughts        [Edit] ││
│  │ Today I woke up and...  [Del]  ││
│  │ Created: 8:30 AM               ││
│  └────────────────────────────────┘│
│                                     │
│  ┌────────────────────────────────┐│
│  │ Afternoon Update        [Edit] ││
│  │ Had lunch with...       [Del]  ││
│  │ Created: 2:15 PM               ││
│  └────────────────────────────────┘│
│                                     │
│  [+ Add Another Entry for This Day]│
└─────────────────────────────────────┘
```

---

## 🔄 Migration Applied

A database migration has been applied to remove the unique constraint:

**Migration:** `core/migrations/0002_alter_diaryentry_options_and_more.py`

**Changes:**
- Removed `unique_together = ['user', 'date']`
- Updated ordering to include `created_at`

**Status:** ✅ Applied successfully

---

## ✅ Testing the Feature

### Test Case 1: Create Multiple Entries
1. Start server: `python manage.py runserver`
2. Login to your account
3. Click today's date on calendar
4. Create first entry: "Morning thoughts"
5. Save and return to dashboard
6. Click today's date again
7. See your first entry in the modal
8. Click "Add Another Entry"
9. Create second entry: "Evening reflection"
10. Return to dashboard
11. Click today's date
12. **Expected:** See both entries in modal ✅

### Test Case 2: View Multiple Entries
1. Click a date with multiple entries
2. **Expected:** Modal opens showing all entries ✅
3. **Expected:** Each entry shows title, preview, timestamp ✅
4. **Expected:** Edit and Delete buttons visible ✅

### Test Case 3: Edit Specific Entry
1. Open entries modal
2. Click "Edit" on any entry
3. Make changes
4. Save
5. Return to dashboard
6. **Expected:** Only that entry is updated ✅

### Test Case 4: Delete Specific Entry
1. Open entries modal
2. Click "Delete" on any entry
3. Confirm deletion
4. **Expected:** Only that entry is deleted ✅
5. **Expected:** Other entries remain ✅

---

## 🐛 Troubleshooting

### Issue: Still getting "Entry already exists" error

**Solution:** Ensure migration is applied
```bash
python manage.py migrate
```

### Issue: Modal not showing multiple entries

**Solution:** Clear browser cache
```
Ctrl + Shift + R (Windows/Linux)
Cmd + Shift + R (Mac)
```

### Issue: Calendar not updating

**Solution:** Refresh the page after creating entries
```javascript
// Or add this to auto-refresh
location.reload();
```

---

## 📝 Code Examples

### Creating Entry via API
```javascript
const response = await fetch('/api/diary/save/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
        id: null,  // null for new entry
        title: 'My Entry',
        date: '2025-10-07',
        body: '<p>Entry content...</p>'
    })
});
```

### Getting All Entries for Date
```javascript
const response = await fetch('/api/diary/by-date/?date=2025-10-07');
const data = await response.json();

if (data.success) {
    console.log(`Found ${data.count} entries`);
    data.entries.forEach(entry => {
        console.log(entry.title, entry.created_at);
    });
}
```

---

## 🎯 Benefits

### Before (Single Entry Per Day)
- ❌ Limited to one entry per day
- ❌ Had to combine morning/evening thoughts
- ❌ Couldn't separate different topics
- ❌ Less flexible journaling

### After (Multiple Entries Per Day)
- ✅ Unlimited entries per day
- ✅ Separate entries for different times
- ✅ Organize thoughts by topic
- ✅ More flexible and natural journaling
- ✅ Track mood changes throughout day
- ✅ Better for detailed journaling

---

## 💡 Use Cases

### Morning & Evening Journaling
```
October 7, 2025
├─ 8:00 AM - Morning Pages
├─ 12:30 PM - Lunch Break Thoughts
├─ 6:00 PM - Evening Reflection
└─ 10:00 PM - Gratitude List
```

### Project-Based Entries
```
October 7, 2025
├─ Work Project Update
├─ Personal Project Progress
└─ Daily Learning Notes
```

### Different Topics
```
October 7, 2025
├─ Health & Fitness
├─ Relationships
├─ Goals & Plans
└─ Random Thoughts
```

---

## 🚀 Future Enhancements

Possible additions for the future:
- [ ] Tags for entries
- [ ] Entry categories
- [ ] Time-based sorting in modal
- [ ] Entry search within a day
- [ ] Bulk actions (delete all entries for a day)
- [ ] Entry templates
- [ ] Entry linking (reference other entries)

---

## 📚 Related Documentation

- [QUICKSTART.md](QUICKSTART.md) - Getting started
- [README.md](README.md) - Full documentation
- [FEATURES.md](FEATURES.md) - All features
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues

---

## ✨ Summary

**What You Can Do Now:**
- ✅ Create unlimited entries per day
- ✅ View all entries for any date
- ✅ Edit individual entries
- ✅ Delete specific entries
- ✅ Better organization and flexibility

**Database Changes:**
- ✅ Migration applied
- ✅ Unique constraint removed
- ✅ No data loss

**UI Updates:**
- ✅ New entries modal
- ✅ Better date navigation
- ✅ Entry previews
- ✅ Timestamp display

---

**Status:** ✅ Feature Complete and Working

Enjoy your enhanced journaling experience with multiple entries per day! 🌸💖
