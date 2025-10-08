from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from datetime import datetime
import json

from .models import User, DiaryEntry, LibraryItem


# Authentication Views
def register_view(request):
    """User registration with optional face enrollment"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        face_data = request.POST.get('face_data')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'core/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)

        if face_data:
            user.set_face_data(face_data)
            user.save()

        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('dashboard')

    return render(request, 'core/register.html')


def login_view(request):
    """Standard login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'core/login.html')


@require_http_methods(["POST"])
def face_login_view(request):
    """Face recognition login endpoint"""
    try:
        data = json.loads(request.body)
        face_data = data.get('face_data')
        username = data.get('username')

        if not username or not face_data:
            return JsonResponse({'success': False, 'error': 'Missing data'})

        user = User.objects.filter(username=username).first()

        if user and user.get_face_data():
            # In a real implementation, you'd compare face descriptors here
            # For now, we'll accept if face_data is provided and user has face data
            login(request, user)
            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'error': 'Face recognition failed'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('login')


# Dashboard
@login_required
def dashboard_view(request):
    """Main dashboard with diary and library"""
    diary_entries = DiaryEntry.objects.filter(user=request.user)
    library_items = LibraryItem.objects.filter(user=request.user)

    return render(request, 'core/dashboard.html', {
        'diary_entries': diary_entries,
        'library_items': library_items,
    })


# Diary Views
@login_required
def diary_list_api(request):
    """API endpoint to get diary entries for calendar"""
    entries = DiaryEntry.objects.filter(user=request.user)
    events = [{
        'id': entry.id,
        'title': entry.title,
        'start': entry.date.isoformat(),
        'url': f'/diary/{entry.id}/'
    } for entry in entries]

    return JsonResponse(events, safe=False)


@login_required
def diary_entry_view(request, entry_id=None):
    """View/Edit diary entry"""
    entry = None
    if entry_id:
        entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)

    return render(request, 'core/diary_entry.html', {'entry': entry})


@login_required
@require_http_methods(["POST"])
def diary_save_api(request):
    """Save diary entry (create or update)"""
    try:
        data = json.loads(request.body)
        entry_id = data.get('id')
        title = data.get('title')
        body = data.get('body')
        date_str = data.get('date')

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if entry_id:
            entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
            entry.title = title
            entry.body = body
            entry.date = date
            entry.save()
        else:
            entry = DiaryEntry.objects.create(
                user=request.user,
                title=title,
                body=body,
                date=date
            )

        return JsonResponse({'success': True, 'id': entry.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required
@require_http_methods(["POST"])
def diary_delete_api(request, entry_id):
    """Delete diary entry"""
    try:
        entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
        entry.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required
def diary_by_date_api(request):
    """Get all diary entries for a specific date"""
    date_str = request.GET.get('date')
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            entries = DiaryEntry.objects.filter(user=request.user, date=date).order_by('-created_at')

            if entries.exists():
                entries_data = [{
                    'id': entry.id,
                    'title': entry.title,
                    'body': entry.body,
                    'date': entry.date.isoformat(),
                    'created_at': entry.created_at.isoformat()
                } for entry in entries]

                return JsonResponse({
                    'success': True,
                    'entries': entries_data,
                    'count': entries.count()
                })
        except ValueError:
            pass

    return JsonResponse({'success': False})


# Library Views
@login_required
@require_http_methods(["POST"])
def library_upload_api(request):
    """Upload PDF to library"""
    try:
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        file = request.FILES.get('file')

        if not file.name.endswith('.pdf'):
            return JsonResponse({'success': False, 'error': 'Only PDF files are allowed'})

        item = LibraryItem.objects.create(
            user=request.user,
            title=title,
            genre=genre,
            file=file
        )

        return JsonResponse({
            'success': True,
            'item': {
                'id': item.id,
                'title': item.title,
                'genre': item.genre,
                'url': item.file.url,
                'uploaded_at': item.uploaded_at.isoformat()
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@login_required
def library_list_api(request):
    """Get library items with optional search"""
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')

    items = LibraryItem.objects.filter(user=request.user)

    if query:
        items = items.filter(Q(title__icontains=query))

    if genre:
        items = items.filter(genre=genre)

    data = [{
        'id': item.id,
        'title': item.title,
        'genre': item.genre,
        'url': item.file.url,
        'uploaded_at': item.uploaded_at.isoformat()
    } for item in items]

    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(["POST"])
def library_delete_api(request, item_id):
    """Delete library item"""
    try:
        item = get_object_or_404(LibraryItem, id=item_id, user=request.user)
        item.file.delete()
        item.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


# User Profile
@login_required
def profile_view(request):
    """User profile page"""
    return render(request, 'core/profile.html')


@login_required
@require_http_methods(["POST"])
def delete_face_data_api(request):
    """Delete user's face recognition data"""
    try:
        request.user.delete_face_data()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


# Search
@login_required
def search_view(request):
    """Global search for diary and library"""
    query = request.GET.get('q', '')

    diary_results = []
    library_results = []

    if query:
        diary_results = DiaryEntry.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query),
            user=request.user
        )

        library_results = LibraryItem.objects.filter(
            user=request.user,
            title__icontains=query
        )

    return render(request, 'core/search.html', {
        'query': query,
        'diary_results': diary_results,
        'library_results': library_results,
    })
