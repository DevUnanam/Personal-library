from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DiaryEntry, LibraryItem


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Face Recognition', {'fields': ('face_descriptor',)}),
    )


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'created_at']
    list_filter = ['user', 'date']
    search_fields = ['title', 'body']


@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'genre', 'uploaded_at']
    list_filter = ['user', 'genre', 'uploaded_at']
    search_fields = ['title']
