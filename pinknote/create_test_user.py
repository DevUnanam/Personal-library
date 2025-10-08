#!/usr/bin/env python
"""
Quick script to create a test user for PinkNote
Run this after migrations to quickly test the application
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User

# Create test user
username = 'testuser'
email = 'test@pinknote.com'
password = 'test123'

# Check if user exists
if User.objects.filter(username=username).exists():
    print(f"✅ User '{username}' already exists!")
    user = User.objects.get(username=username)
else:
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Created test user:")
    print(f"   Username: {username}")
    print(f"   Email: {email}")
    print(f"   Password: {password}")

print(f"\n🌸 You can now login at: http://127.0.0.1:8000/login/")
print(f"   Username: {username}")
print(f"   Password: {password}")
